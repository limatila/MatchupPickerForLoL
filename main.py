# a random matchuper for league of legends lane phase thinking training
# should be divided by Lanes

#?should execute with node prompts

import secrets;

with open("./data/names.txt", 'r') as namesFile: #change path to correct source
    allChamps = namesFile.read().split(",")

iterationCounter = 1
def pickMatchup( lane, totalLanes = 1 ):
    if lane == "bot":
        blue_one = secrets.choice(allChamps)
        blue_two = secrets.choice(allChamps)
        
        red_one = secrets.choice(allChamps)
        red_two = secrets.choice(allChamps)
        print(blue_one, " and ", blue_two, " X ", red_one, " and ", red_two, "?")
    elif lane == "": #every other then botlane
        blue_one = secrets.choice(allChamps)
        red_one = secrets.choice(allChamps)
        print(blue_one, " X ", red_one, "?")
    elif lane.lower() in ["5v5", "full team"]:
        blue_one_top = secrets.choice(allChamps)
        blue_two_jg = secrets.choice(allChamps)
        blue_thr_mid = secrets.choice(allChamps)
        blue_four_bot = secrets.choice(allChamps)
        blue_fiv_bot = secrets.choice(allChamps)

        red_one_top = secrets.choice(allChamps)
        red_two_jg = secrets.choice(allChamps)
        red_thr_mid = secrets.choice(allChamps)
        red_four_bot = secrets.choice(allChamps)
        red_fiv_bot = secrets.choice(allChamps)
        print(f"""TOP: {blue_one_top} X {red_one_top}?
JUNGLE: {blue_two_jg} X {red_two_jg}?
MIDDLE: {blue_thr_mid} X {red_thr_mid}?
BOTTOM and SUPPORT: {blue_four_bot} and {blue_fiv_bot} X {red_four_bot} and {red_fiv_bot}?

""")
        global iterationCounter;
    
    #To repeat operations
    if lane in ["bot", ""]:  #to iterate more than one time, use only a single lane.
        while iterationCounter < totalLanes :
            iterationCounter += 1
            pickMatchup(lane)
    elif lane in ["full team", "5v5"]:
        if totalLanes > 3 or totalLanes < 0:
            raise Exception(" Can't repeat more then 3 times, Only values between 1 and 3 allowed!\nCODE_1 ")
        else:
            while iterationCounter < totalLanes:
                iterationCounter += 1
                pickMatchup("5v5")
    else:
        raise Exception(" Invalid option! \nCODE_2")    
    #!don't matter the exception, one iteration will ocurr always.

pickMatchup("full team", totalLanes= -2)
