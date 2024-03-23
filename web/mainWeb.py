# 1.1 a random matchuper for league of legends lane phase thinking training
# Have a random per-lane generation, and a realtime stats opener
# Operated buy inputs in terminal.
#! change special names in exibition

import secrets
import os #!running in browser, should open with pyscript
import time
def clearConsole():
    os.system("cls" if "nt" in os.name
            else 'clear') #'nt' = windows
    
clearConsole()
os.system("title Matchup Picker For LoL")

print("Welcome to this program made by Átila Lima")
print("It'll randomly choose matchups from LoL, by names and roles"); time.sleep(2)
print("Starting...")


#Data--------------------------------------------------------
dividedChamps = { #divide lanes and store them here
    'top': [],
    'mid': [],
    'bot': [],
    'sup': [],
    'jungle': [],
};

files = ["bot.txt", "jungle.txt", "mid.txt", "sup.txt", "top.txt"]

for filePath in files:
    with open( ("./data" + filePath), 'r' ) as currentFile: #!Files need to be uploaded to browser.
        currentChamps = currentFile.read().split(",")

        #separar extensão do nome
        currentFinalIndex = filePath.find(".txt")
        storageName = filePath[0:currentFinalIndex]

        for champ in currentChamps:
            dividedChamps[storageName].append(champ)


#Main execution functions------------------------------------
#* random picker into local names stored
def pickMatchup( lane, totalLanes = 1 ): 
    global blue_one, blue_two, red_one, red_two

    if lane in ["top", "mid", "jungle"]:                #*every other then botlane
        blue_one = secrets.choice(dividedChamps[lane])
        red_one = secrets.choice(dividedChamps[lane])

        print(blue_one, " X ", red_one, "?")
        statsOpener(lane)
    elif lane == "bot":                                 #*generates ADC and SUP
        blue_one = secrets.choice(dividedChamps["bot"])
        blue_two = secrets.choice(dividedChamps["sup"])
        
        red_one = secrets.choice(dividedChamps["bot"])
        red_two = secrets.choice(dividedChamps["sup"])
        print(blue_one, " and ", blue_two, " X ", red_one, " and ", red_two, "?")
        statsOpener(lane)
    elif lane.lower() in ["5v5", "full team"]:          #*Full team generation
        blue_one_top = secrets.choice(dividedChamps["top"])
        blue_two_jg = secrets.choice(dividedChamps["jungle"])
        blue_thr_mid = secrets.choice(dividedChamps["mid"])
        blue_four_bot = secrets.choice(dividedChamps["bot"])
        blue_fiv_bot = secrets.choice(dividedChamps["sup"])

        red_one_top = secrets.choice(dividedChamps["top"])
        red_two_jg = secrets.choice(dividedChamps["jungle"])          #? i think opening stats for all of these would not be good... unless the IO wants it.
        red_thr_mid = secrets.choice(dividedChamps["mid"])
        red_four_bot = secrets.choice(dividedChamps["bot"])
        red_fiv_bot = secrets.choice(dividedChamps["sup"])
        print(f"TOP: {blue_one_top} X {red_one_top}? \
                \nJUNGLE: {blue_two_jg} X {red_two_jg}? \
                \nMIDDLE: {blue_thr_mid} X {red_thr_mid}? \
                \nBOTTOM and SUPPORT: {blue_four_bot} and {blue_fiv_bot} X {red_four_bot} and {red_fiv_bot}?\n")
        
    
    #To repeat operations
    global iterationCounter;
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
        print("Invalid option of Lane! Choose a valid lane(Top, Mid, Bot or Full Team/5v5) \nCode 3")
        return "Code 3"

#*: Open realtime stats in OP.GG website
browser = None;
def statsOpener(laneToCompare):
    print("")
    global browser

    inpOpenBrowser = input("Do you wanna open OP.GG stats? (Y/N): ").upper()
    if inpOpenBrowser == 'Y' :
        if browser == None: #*if undefined, grab the desired.
            browser = input("Type the name of your browser: ") #! should check valid typing
        
        if laneToCompare in ["top", "mid", "jungle"]:
            print("\nOpening browser in 2 seconds..."); time.sleep(2.5); #!tudu: if error, should try inserting again 
            os.system(f"start {browser} \"https://www.op.gg/champions/{blue_one}/build/{laneToCompare}?region=global&tier=all&target_champion={red_one}\"")
            print("browser opened! proceeding...")
        elif laneToCompare == "bot":
            print("\nOpening two browsers in 2 seconds..."); time.sleep(2.5); #? maybe select what region would be too slow
            os.system(f"start {browser} \"https://www.op.gg/champions/{blue_one}/build/bot?region=global&tier=all&target_champion={red_one}\"")
            os.system(f"start {browser} \"https://www.op.gg/champions/{blue_two}/build/support?region=global&tier=all&target_champion={red_two}\"")
            print("browser opened! proceeding...")
        
        print("")
    elif inpOpenBrowser == "N" :
        print("ok, proceeding..."); time.sleep(0.3)
    else: 
        raise Exception("Invalid option in statsOpener! Code 4")

print("")
print("Insert bellow some infos to begin the code execution."); time.sleep(1)
print("Inputting a blank space in the lane section or a \"0\" in the repetition section will stop the execution."); time.sleep(1)
print("----------------------")


#Repeatition and usage---------------------------------------
while True:
    iterationCounter = 1 #for repeating

    inpLane = input("Which lane do you desire to try?: ")
    #cleaning
    if inpLane == "clear":
        clearConsole()
        print("Window cleaned.")
        continue
    else:    
        inpNumReps = int(input("How many times do you wan't to repeat it?: "))

    #formatting the entry
    inpLane.strip().lower(); #!Isso não esta formatando para a linha 125
    if inpLane == "jg": inpLane = "jungle";


    #Ending=========================================
    for entry in (inpLane, str(inpNumReps)):
        if entry.isspace() == True: #! Vai jogar uma exceção se spammar Enter.
            print("")
            print("Program stopped by user. Goodbye! \nCode 0")
            break;
        
    if "0" in [inpLane, str(inpNumReps)]:
        print("")
        print("Program stopped by user. Goodbye! \nCode 0")
        break;
    else:   #*don't want to exit? ok, continues.
        print("\nResults: \n")
        pickMatchup(inpLane, inpNumReps)
        print("\n**********************")
    
#main_exec()
