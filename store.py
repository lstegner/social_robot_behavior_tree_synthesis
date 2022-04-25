#!/usr/bin/env python3

class WorldStates:
    def __init__(self):
        # # World States
        # self.humanReady = False
        # self.greetOccurred = False

        # # HumanJustSpoke
        # self.humanAffirm = False
        # self.humanDeny = False
        # self.humanAskInfo = False
        # self.humanAskDirections = False
        # self.humanGoodbye = False
        # self.humanNotUnderstood = False

        # # RobotJustActed
        # self.robotPrompt = False
        # self.robotValidate = False
        # self.robotListen = False
        # self.robotAnswerInfo = False
        # self.robotAnswerDirections = False
        # self.robotAskToRepeat = False
        # self.robotHelp = False
        # self.robotFarewell = False

        self.state_list = ["humanReady","greetOccurred",
        "humanAffirm","humanDeny","humanAskInfo","humanAskDirections","humanGoodbye","humanNotUnderstood",
        "robotPrompt","robotValidate","robotListen","robotAnswerInfo","robotAnswerDirections","robotAskToRepeat","robotHelp","robotFarewell"]

        self.humanJustSpoke = ["humanAffirm","humanDeny","humanAskInfo","humanAskDirections","humanGoodbye","humanNotUnderstood"]
        self.robotJustActed = ["robotPrompt","robotValidate","robotListen","robotAnswerInfo","robotAnswerDirections","robotAskToRepeat","robotHelp","robotFarewell"]

    # def HumanJustSpoke(self):
    #     if self.humanAffirm or self.humanDeny or self.humanAskInfo or self.humanAskDirections or self.humanGoodbye or self.humanNotUnderstood:
    #         return True
    #     else:
    #         return False

    # def RobotJustActed(self):
    #     if self.robotPrompt or self.robotValidate or self.robotListen or self.robotAnswerInfo or self.robotAnswerDirections or self.robotAskToRepeat or self.robotHelp or self.robotFarewell:
    #         return True
    #     else:
    #         return False


class Behavior:
    def __init__(self, n="",precons=[],postcons=[]):
        self.name = n
        self.preconditions = precons
        self.postconditions = postcons

    # def get_preconditions(self):
    #     precons = []
    #     for precon in self.preconditions:
    #         precons.append(precon[0])

    #     return precons

    # def get_postconditions(self):
    #     postcons = []
    #     for postcon in self.postconditions:
    #         postcons.append(postcon[0])

    #     return postcons

class BehaviorBank:
    def __init__(self):
        self.behaviors = []
        self.behaviors.append(Behavior("Greet",{"humanReady":True,"greetOccurred":False},[{"greetOccurred":True}]))
        self.behaviors.append(Behavior("Answer",{"humanReady":True,"greetOccurred":False},[{"greetOccurred":True}]))
        self.behaviors.append(Behavior("AskToRepeat",{"humanNotUnderstood":True},[{}]))
        self.behaviors.append(Behavior("Help",{"humanNotUnderstood":True},[{}]))
        self.behaviors.append(Behavior("Prompt",{"humanReady":True,"humanAffirm":False,"humanDeny":False,"humanAskInfo":False,"humanAskDirections":False,"humanGoodbye":False,"humanNotUnderstood":False},[{}]))
        
        self.behaviors.append(Behavior("Validate",{"humanAskInfo":True},[{"humanAffirm":True},{"humanDeny":True},{"humanNotUnderstood":True}]))
        self.behaviors.append(Behavior("Fact",{"humanAskInfo":True},[{"robotAnswerInfo":True}]))
        self.behaviors.append(Behavior("Farewell",{"humanGoodbye":True, "robotFarewell":False},[{"END":True}]))
        self.behaviors.append(Behavior("Listen",{"robotPrompt":True,"robotValidate":True,"robotListen":True,"robotAnswerInfo":True,"robotAnswerDirections":True,"robotAskToRepeat":True,"robotHelp":True,"robotFarewell":True},
            [{"humanAffirm":True,"humanDeny":True,"humanAskInfo":True,"humanAskDirections":True,"humanGoodbye":True,"humanNotUnderstood":True},{"humanReady":False}]))
        self.behaviors.append(Behavior("Guide",{"humanAskDirections":True},[{"robotDirections":True}]))
        self.behaviors.append(Behavior("Approach",{"humanReady":False},[{"humanReady":True},{"humanReady":False}]))

        #self.behaviors.append(Behavior("Point",{"humanAskDirections":True},[{"robotDirections":True}]))
        #self.behaviors.append(Behavior("Announce",{"humanReady":False},[{"humanReady":True},{"humanReady":False}]))




        



        self.behaviors.append(Behavior("Announce",{"humanAskInfo":True,"humanAffirm":True},[{"robotAnswerInfo":True}]))

    # def print_behavior(self):
    #     print(self.behaviors[0].preconditions)

    def get_behavior(self, name):
        for behavior in self.behaviors:
            if behavior.name == name:
                return behavior


# if __name__ == '__main__':
#     x = BehaviorBank()
#     x.print_behavior()

    