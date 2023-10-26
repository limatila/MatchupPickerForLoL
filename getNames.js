//run in node
const fs = require('fs');
const lolChamps = require ('lol-champs');

champions = lolChamps.all().sort();

fs.writeFile('C:\\Users\\Atila\\Desktop\\programacionez\\MatchupPickerForLoL\\data\\names.txt', champions.toString(),
                err => {
                    if(err){ throw err };
                });

console.log("If false, champs after it are missing:", champions.includes("Pyke"))
console.log("Content registered succesfully!")