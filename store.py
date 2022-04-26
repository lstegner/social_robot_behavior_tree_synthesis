#!/usr/bin/env python3

class Behavior:
    def __init__(self, n="",precons=[],postcons=[]):
        self.name = n
        self.preconditions = precons
        self.postconditions = postcons

class BehaviorBank:
    def __init__(self):
        self.behaviors = []
        self.behaviors.append(Behavior("Greet",{"humanReady":True,"greetOccurred":False},[{"greetOccurred":True}]))
        self.behaviors.append(Behavior("Announce",{"humanReady":False},[{"humanReady":True},{"humanReady":False}]))
        self.behaviors.append(Behavior("OfferHelp",{"humanReady":True,"greetOccurred":True},[{"offeredHelp":True}]))

        

    def get_behavior(self, name):
        for behavior in self.behaviors:
            if behavior.name == name:
                return behavior


class BehaviorBank_backup:
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

    