"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var uniqueRandomArray = require('unique-random-array');
var randomNameGenerator = new Map();
var forceLowerCase = function (str) { return str.toLowerCase(); };
exports.languages = new Set([
    "cs",
    "de",
    "el",
    "en",
    "fr",
    "hu",
    "it",
    "ja",
    "ko",
    "pl",
    "pt",
    "ru",
    "tr",
    "vn",
    "zh-hans",
    "zh-hant"
]);
function capitalizeName(champsName) {
    var regexp = /([A-Za-z\u00C0-\u1FFF\u2800-\uFFFD]+)/gi;
    return champsName.replace(regexp, function (match) { return match.charAt(0).toUpperCase() + match.substring(1); });
}
function determineLangCode(lang) {
    if (lang === void 0) { lang = "en"; }
    var champs = require("../data/" + lang.toLowerCase() + ".json");
    return champs.data;
}
function assembleNameList(champs) {
    return Object.keys(champs).map(function (key) {
        return champs[key].name;
    });
}
function getName(champId, lang) {
    if (lang === void 0) { lang = "en"; }
    var champs = determineLangCode(lang);
    var matched = Object.keys(champs).filter(function (key) {
        return champs[key].id === champId;
    }).toString();
    if (matched === "")
        throw new Error(champId + " does not exists. Please double check the id.");
    return champs[matched].name;
}
exports.getName = getName;
function getChampion(name, lang) {
    if (lang === void 0) { lang = "en"; }
    var champs = determineLangCode(lang);
    var champName = name;
    if (champName.match(' '))
        champName = capitalizeName(name);
    var data = Object.keys(champs).filter(function (key) {
        return champs[key].name === champName || key === champName || forceLowerCase(key) === champName;
    }).toString();
    if (data === "")
        throw new Error(champName + " does not exists. Please double check the name.");
    return champs[data];
}
exports.getChampion = getChampion;
function getId(name, lang) {
    if (lang === void 0) { lang = "en"; }
    var champs = determineLangCode(lang);
    var champName = name;
    if (champName.match(' '))
        champName = capitalizeName(name);
    var matched = Object.keys(champs).filter(function (key) {
        return champs[key].name === champName || key === champName || forceLowerCase(key) === champName;
    }).toString();
    if (matched === "")
        throw new Error(champName + " does not exists. Please double check the name.");
    return champs[matched].id;
}
exports.getId = getId;
function all(lang) {
    if (lang === void 0) { lang = "en"; }
    var champs = determineLangCode(lang);
    var langCode = forceLowerCase(lang);
    if (!langCode || langCode === 'en') {
        return assembleNameList(champs);
    }
    if (!exports.languages.has(langCode)) {
        throw new Error("Localized list for language code '" + langCode + "' does not exist.");
    }
    return assembleNameList(champs);
}
exports.all = all;
function random(lang) {
    if (lang === void 0) { lang = "en"; }
    var langCode = forceLowerCase(lang);
    if (randomNameGenerator.has(langCode))
        return randomNameGenerator.get(langCode)();
    var champs = determineLangCode(lang);
    var random = uniqueRandomArray(assembleNameList(champs));
    randomNameGenerator.set(langCode, random);
    return random();
}
exports.random = random;
