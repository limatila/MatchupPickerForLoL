//run in node
const fs = require('fs');
const lolChamps = require ('lol-champs');

champions = lolChamps.all().sort();

fs.writeFile('C:\\Users\\Atila\\Desktop\\programacionez\\MatchupPickerForLoL\\data\\names.txt', champions.toString(),
                err => {
                    if(err){ throw err };
                });
console.log("Content registered succesfully!")

function missingChampsCheck(champ){
    console.log(`If false, champions released after ${champ} are missing:`, champions.includes(champ))
}
missingChampsCheck("Pyke")
