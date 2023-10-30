# 1.1 a random matchuper for league of legends lane phase thinking training
# Operated buy inputs in terminal.
#! should be divided by Lanes

import secrets
import os
import time

#Data----------------------------------------------
with open("./data/names.txt", 'r') as namesFile: #change path to correct source
    allChamps = namesFile.read().split(",")

dividedChamps = {};

#Main execution------------------------------------
iterationCounter = 1 #for repeating
#* random picker into local names stored
def pickMatchup( lane, totalLanes = 1 ): 
    global blue_one, blue_two, red_one, red_two

    if lane in ["top", "mid", "jungle"]:                #*every other then botlane
        blue_one = secrets.choice(allChamps)
        red_one = secrets.choice(allChamps)

        print(blue_one, " X ", red_one, "?")
        statsOpener(lane)
    elif lane == "bot":                                 #*generates ADC and SUP
        blue_one = secrets.choice(allChamps)
        blue_two = secrets.choice(allChamps)
        
        red_one = secrets.choice(allChamps)
        red_two = secrets.choice(allChamps)
        print(blue_one, " and ", blue_two, " X ", red_one, " and ", red_two, "?")
        statsOpener(lane)
    elif lane.lower() in ["5v5", "full team"]:          #*Full team generation
        blue_one_top = secrets.choice(allChamps)
        blue_two_jg = secrets.choice(allChamps)
        blue_thr_mid = secrets.choice(allChamps)
        blue_four_bot = secrets.choice(allChamps)
        blue_fiv_bot = secrets.choice(allChamps)

        red_one_top = secrets.choice(allChamps)
        red_two_jg = secrets.choice(allChamps)          #? i think opening stats for all of these would not be good... unless the IO wants it.
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
    if lane in ["bot", "top", "mid", "jungle"]:  #to iterate more than one time, use only a single lane.
        while iterationCounter < totalLanes :
            iterationCounter += 1
            pickMatchup(lane)
    elif lane in ["full team", "5v5"]: #for full teams, limited to 3 times.
        if totalLanes > 3 or totalLanes < 0: 
            print("Can't repeat more then 3 times, Only values between 1 and 3 allowed!\nCODE_2 ")
            return "Code 2"
        else:
            while iterationCounter < totalLanes:
                iterationCounter += 1
                pickMatchup("5v5")
    else:
        print("Invalid option in pickMatchup()! \nCODE_3")    
        return "Code 3"
    #!don't matter the exception, one iteration will ocurr always.

#*: Open realtime stats in OP.GG website
def statsOpener(laneCompare):
    print("")
    statsOpener = input("Do you wanna open OP.GG stats? (Y/N): ")
    if(statsOpener == 'Y'):
        browser = str(input("Type the name of your browser: ")) #! should check correct typing
        if(laneCompare in ["top, mid, jungle"]):
            print("Opening browser in 4 seconds..."); time.sleep(4);
            os.system(f"start {browser} \"https://www.op.gg/champions/{blue_one}/build/{laneCompare}?region=global&tier=diamond_plus&target_champion={red_one}\"")
        elif(laneCompare == "bot"):
            print("Opening two browsers in 4 seconds..."); time.sleep(4);
            os.system(f"start {browser} \"https://www.op.gg/champions/{blue_one}/build/bot?region=global&tier=diamond_plus&target_champion={red_one}\"")
            os.system(f"start {browser} \"https://www.op.gg/champions/{blue_two}/build/support?region=global&tier=diamond_plus&target_champion={red_two}\"")
    elif(statsOpener == "N"):
        print("ok, proceeding...")
    else: print("Invalid option in statsOpener! Code 4")

print("Insert bellow some infos to begin the your code execution."); time.sleep(1)
print("Inputting \"0\" in any of the spaces will stop the execution."); time.sleep(1)

while True:
    print("**********************")
    inputLane = str(input("Which lane do you desire to try?: "))
    inputNumReps = str(input("How many times do you wan't to repeat it?: "))

    #formatting to ideal
    if inputLane == "jg": inputLane = "jungle";
    inputLane.strip().lower(); inputNumReps.strip().lower();

    if "0" in [inputLane, inputNumReps]:#decide where the program stops
        print("")
        print("Program stopped by user. Code 0");
        break;
    else:
        print("")
        pickMatchup(inputLane, totalLanes= int(inputNumReps))


#Ending============================================
input("Press enter to close CMD...")