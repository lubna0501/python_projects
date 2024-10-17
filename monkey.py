# Initialization code
def __init__(self):
    """
    Initialize the global variables, and function dictionaries
    """
    self.worldStack = []
    self.goalStack = []
    self.plan = []

    # token to function mappings
    self.formulas = {"height": self.height, "at": self.at}
    self.Operators = {"GO": self.go, "PUSH": self.push,
                      "CLIMB": self.climb}

    # safety net tests are denoted by the following as the first list item.
    self.SafetyTag = "SAFETYTAG"

@staticmethod
def populate(strng, statestack):
    """
    Helper function that parses strng according to expectations
    and adds to the sateStack passed in.
    """
    for x in (strng.lower().replace('(', '').replace(')', '').split(',')):
        ls = x.strip().split(' ')
        statestack.append(ls)
    statestack.reverse()

def populategoal(self, strng):
    """
    Populate the goal stack with data in strng.
    """
    self.populate(strng, self.goalStack)
    # add original safety check
    goalcheck = [self.SafetyTag]
    for g in self.goalStack:
        goalcheck.append(g)
    self.goalStack.insert(0, goalcheck)

def populateworld(self, strng):
    """
    Populate the world state stack with data in strng.
    """
    self.populate(strng, self.worldStack)

# ----------------------------------------------------
# Solver
#   Attempts to solve the problem using the setup
#   goal and world states
# ----------------------------------------------------

def solve(self):
    """
    Attempts to solve the problem using STRIPS Algorithm
    Note: You need to setup the problem prior to running this
          by using populateWorld and populateGoal using a well
          formatted string.
    """
    if (not len(self.worldStack) > 0) or (not len(self.goalStack) > 0):
        print "\nNothing to do.\nMake sure you populate the problem using\n" \
              "populateWorld and populateGoal before calling this function."
        return
    while len(self.goalStack) > 0:
        # if the subgoal is in world state
        if self.top(self.goalStack) in self.worldStack:
            # pop it from the stack
            self.goalStack.pop()
        # if that item is an operator,
        elif self.top(self.goalStack)[0].upper() in self.Operators:
            subgoal = self.goalStack.pop()
            # store it in a "plan"
            self.plan.append(subgoal)
            # and modify the world state as specified
            self.Operators[(subgoal[0])](subgoal)
        # if the item is a safety check
        elif self.SafetyTag == self.top(self.goalStack)[0].upper():
            safetycheck = self.goalStack.pop()
            for check in safetycheck[1:]:
                if not (check in self.worldStack):
                    print " Safety net ripped.n Couldn't contruct a plan. Exiting...", check
                    return
        else:
            # find an operator that will cause the
            # top subgoal to result
            if self.top(self.goalStack)[0] in self.formulas:
                self.formulas[self.top(self.goalStack)[0]]()
            else:
                raise Exception(self.top(self.goalStack)[0] + " not valid formula/subgoal")
                # or add to goal stack and try, but not doing that for now.
    print "\nFinal Plan:\n",
    for step in self.plan:
        print "  ", join(step, " ").upper()

# ----------------------------------------------------
# Predicate logic
# ----------------------------------------------------
def at(self):
    topg = self.top(self.goalStack)
    assert(topg[0] == "at"), "expected at"
    assert(len(topg) == 3), "expected 3 arguments"
    print topg
    x = self.getloc(topg[1])
    if topg[1] == "monkey":
        self.goalStack.append(["GO", x, topg[2]])
        self.goalStack.append([self.SafetyTag, ["at", "monkey", x], ["height", "monkey", "low"]])
        self.goalStack.append(["at", "monkey", x])
        self.goalStack.append(["height", "monkey", "low"])
    else:
        self.goalStack.append(["PUSH", topg[1], x, topg[2]])
        self.goalStack.append([self.SafetyTag, ["at", topg[1], x], ["at", "monkey", x], ["height", "monkey", "low"],
                               ["height", topg[1], "low"], ["handempty"]])
        self.goalStack.append(["at", topg[1], x])
        self.goalStack.append(["at", "monkey", x])
        self.goalStack.append(["height", "monkey", "low"])
        self.goalStack.append(["height", topg[1], "low"])
        self.goalStack.append(["handempty"])

def height(self):
    topg = self.top(self.goalStack)
    print topg
    assert(topg[0] == "height"), "expected height"
    assert(len(topg) == 3), "expected 3 arguments"
    if topg[1] == "monkey":
        x = self.getloc("monkey")
        y = "low" if (self.getheight("monkey") == "low") else "high"
        self.goalStack.append(["CLIMB"])
        self.goalStack.append([self.SafetyTag, ["at", "monkey", x], ["at", "chair", x], ["height", "monkey", y],
                               ["height", "chair", "low"]])
        self.goalStack.append(["at", "chair", x])
        self.goalStack.append(["height", "monkey", y])
        self.goalStack.append(["height", "chair", "low"])
        self.goalStack.append(["at", "monkey", x])

# ----------------------------------------------------
# Operators
# ----------------------------------------------------

def go(self, subgoal):
    # deletion
    self.worldstateremove(["at", "monkey", subgoal[1]])
    # addition
    self.worldstateadd(["at", "monkey", subgoal[2]])

def push(self, subgoal):
    # deletion
    self.worldstateremove(["at", "monkey", subgoal[2]])
    self.worldstateremove(["at", subgoal[1], subgoal[2]])
    # addition
    self.worldstateadd(["at", subgoal[1], subgoal[3]])
    self.worldstateadd(["at", "monkey", subgoal[3]])

def climb(self, subgoal):
    # deletion
    self.worldstateremove(["height", "monkey", "low"])
    # addition
    self.worldstateadd(["height", "monkey", "high"])

# ----------------------------------------------------
# Utility functions
# ----------------------------------------------------

#  Returns the item that is being held in the world state, 0 if not
def getholdingitem(self):
    for x in self.worldStack:
        if x[0] == "holding":
            return x[1]
    return 0

# Return height of object
def getheight(self, item):
    for x in self.worldStack:
        if x[0] == "height" and x[1] == item:
            return x[2]
    raise Exception("Object " + item + " is on nothing!")

# Return location of object
def getloc(self, item):
    for x in self.worldStack:
        if x[0] == "at" and x[1] == item:
            return x[2]
    raise Exception("Object " + item + " has no location!")

# Adds a state to world state if the state isn't already true
def worldstateadd(self, toadd):
    if toadd not in self.worldStack:
        self.worldStack.append(toadd)

# Tries to remove the toRem state from the world state stack.
def worldstateremove(self, torem):
    while torem in self.worldStack:
        self.worldStack.remove(torem)

@staticmethod
def top(lst):
    """
    Returns the item at the end of the given list
    We don't catch an error because that's the error we want it to throw.
    """
    return lst[len(lst) - 1]
