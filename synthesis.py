from anytree import NodeMixin, RenderTree
from store import BehaviorBank

class BT_Node(NodeMixin):
    def __init__(self, name, type, parent=None, children=None):
        self.name = name
        self.type = type
        self.parent = parent
        if children:
            self.children = children

    def print(self, start):
        for pre, fill, node in RenderTree(start):
            treestr = u"%s%s" % (pre, node.name)
            print(treestr.ljust(8), node.type)

    def check(self, start):
        for pre, fill, node in RenderTree(start):
            if "Condition" in node.type:
                print("Found contition! " + node.type)

class Synthesis:
    def __init__(self, goal=[], behavior_bank = None):
        self.end_goal = goal
        self.behavior_bank = behavior_bank

    def find_child_action(self, goal_state, parent, curr_depth, max_depth):
        # if there are multiple goal states, we want them to be joined by a sequence node
        goal_sequence = None
        if len(goal_state) > 1:
            goal_sequence = BT_Node(curr_depth,"Sequence (for multiple goals)",parent)

        # for each var in goal_state:
        for goal_condition in goal_state:
            # find action that results in var
            action_to_add = self.find_correct_action(goal_condition)

            if action_to_add is not None:
                # add stuff to behavior tree

                # replace condition with selector node. condition is left child, action is right child
                new_selector = BT_Node(curr_depth+1,"Selector",parent)
                update_curr_depth = curr_depth
                if goal_sequence is not None:
                    new_selector.parent = goal_sequence
                    update_curr_depth = curr_depth + 1
                else:
                    new_selector.parent = parent
                conditional = BT_Node(update_curr_depth+2,"Condition: " + str(goal_condition),new_selector)
                new_sequence = BT_Node(update_curr_depth+2,"Sequence",new_selector)

                # if action has pre-conditions, 
                # right child should be sequence node with each pre-condition as child and action as right-most child
                if len(list(self.behavior_bank.get_behavior(action_to_add).preconditions)) > 0:
                    for item in self.behavior_bank.get_behavior(action_to_add).preconditions:
                        x = {item: self.behavior_bank.get_behavior(action_to_add).preconditions[item]}
                        if(update_curr_depth < max_depth):
                            self.find_child_action([x], new_sequence, update_curr_depth+2, max_depth)
                        else:
                            new_precon = BT_Node(update_curr_depth+3,str(x), new_sequence)

                # if action has multiple possible post-conditions, discard non-desirable ones and add as a child: 22
                # sequence node, with right child as condition (not desired result) and left child as (offer help)
                if len(self.behavior_bank.get_behavior(action_to_add).postconditions) > 1:
                    unexpected_input_seq = BT_Node(update_curr_depth+3, "Potential undesirable input", new_sequence)
                    extra_response_check = BT_Node(update_curr_depth+4, "Check other post conditions", unexpected_input_seq)
                    extra_responses = BT_Node(update_curr_depth+4, "Offer help", unexpected_input_seq)                   

                # add action as last child
                action_node = BT_Node(update_curr_depth+3,action_to_add,new_sequence)

            # return the behavior tree created
        return parent

    def find_correct_action(self,goal):
        # for each available behavior, check post-conditions for one that works
        # return the first one we get
        for behavior in self.behavior_bank.behaviors:
            for postcon in behavior.postconditions:
                if self.get_first_key(goal) in self.get_keys(postcon):
                    if postcon[self.get_first_key(goal)] == goal[self.get_first_key(goal)]:
                        return behavior.name

        return None

    def get_keys(self, dictionary):
        return [key for key in dictionary.keys()]

    def get_first_key(self, dictionary):
        return [key for key in dictionary.keys()][0]

if __name__ == '__main__':
    # set the goal
    goal = [{"offeredHelp":True}]

    # initialize the behaviorsfind_child_action
    behavior_bank = BehaviorBank()

    # initialize BT
    root = BT_Node("None","root")

    # create the synthesizer
    synthesizer = Synthesis(goal, behavior_bank)

    # run
    tree = synthesizer.find_child_action(goal, root, curr_depth=0, max_depth=3)
    print("------------final tree------------")
    tree.print(root)
    #tree.check(root)

