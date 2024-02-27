# Matchup Picker For LoL
A random matchup League of Legends matchup picker to train your skills in matchup predicting
Via python console, select which lane to be predicted, "top", "mid", "jg", "bot", or "full team", and random picks will be shown to you to predict.
Some real-world stats can be broughten and presented for each matchup, for you to compare and analyze if your guessings are going in the right direction!

## Status: Yet to be finished, 
won't be giving it too much work, just a practicing project
* champion lanes separation not finished
* browser opening mostly done
* repetition of randomizing added
* EXE startup should be broughten in some time, to make it indenpendent of Python installation in the machine.

- More updates on the way..

---

# How-to-use:
To start the program correctly, execute 'startProgram.bat'. The names should be updated correctly, and the main program 'main.py' should be able to execute. Some fields are required to be answered to start randomizing the champions names. 

A first one will be the Lane in focus to have a Matchup randomized. 
You can choose for Top, Mid, Bot, or Full Team\5v5 for all lanes at once.

The second field will ask how many times should it generate new Matchup names in the Lane selected.
Single Lanes can be randomized in a infinite number, but for Full Team you'll need to select between 1 or 3 times.
If you only want it to generate once, just type '1' and hit enter.

Inputting '0' in any of the fields will result in process closure, it is the method for leaving the application.

Additionally, a way of opening Real Worlds stats will show up in every Matchup, before continuing.
Type 'Y'/'N' (or 'Yes'/'No') to choose if you wan't to open the stats in your browser.
If 'Yes', you need to input your browser of choice to be opened. Just type the shortened browser name("chrome", "opera", "firefox"), and it will open automatically in 2 seconds.
- The selected browser will be the default for the rest of the program's execution.