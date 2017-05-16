"use strict";

class BuildController {
    constructor() {

    }

    updatePcpTotal() {
        let val = document.getElementById('pcpSelect').value;
        let pcp;
        let categoryIds = ['pcpRace', 'pcpAttr', 'pcpSkills', 'pcpProfs',
                           'pcpWealth', 'pcpBoons']
        let catSum = 0;
        if (val == 'Gritty (18)') {
            pcp = 18;
        } else if (val == 'Low (22)') {
            pcp = 22;
        } else if (val == 'Medium (26)') {
            pcp = 26;
        } else if (val == 'High (30)') {
            pcp = 30;
        } else if (val == 'Legendary (34)') {
            pcp = 34;
        }
        for (let catId of categoryIds) {
            catSum += parseInt(document.getElementById(catId).innerHTML);
        }
        pcp = pcp - catSum;
        document.getElementById('pcpRemain').innerHTML = pcp;
    }

    pcpRaceUp() {
        let currVal = parseInt(document.getElementById('pcpRace').innerHTML);
        let remVal = parseInt(document.getElementById('pcpRemain').innerHTML);
        if (currVal < 8 && remVal > 0) {
            currVal += 1;
            remVal -= 1;
        }
        document.getElementById('pcpRemain').innerHTML = remVal;
        document.getElementById('pcpRace').innerHTML = currVal;
    }

    pcpRaceDn() {
        let currVal = parseInt(document.getElementById('pcpRace').innerHTML);
        let remVal = parseInt(document.getElementById('pcpRemain').innerHTML);
        if (currVal > 1) {
            currVal -= 1;
            remVal += 1;
        }
        document.getElementById('pcpRemain').innerHTML = remVal;
        document.getElementById('pcpRace').innerHTML = currVal;
    }

    pcpAttrUp() {
        let currVal = parseInt(document.getElementById('pcpAttr').innerHTML);
        let remVal = parseInt(document.getElementById('pcpRemain').innerHTML);
        if (currVal < 10 && remVal > 0) {
            currVal += 1;
            remVal -= 1;
        }
        document.getElementById('pcpRemain').innerHTML = remVal;
        document.getElementById('pcpAttr').innerHTML = currVal;
    }

    pcpAttrDn() {
        let currVal = parseInt(document.getElementById('pcpAttr').innerHTML);
        let remVal = parseInt(document.getElementById('pcpRemain').innerHTML);
        if (currVal > 1) {
            currVal -= 1;
            remVal += 1;
        }
        document.getElementById('pcpRemain').innerHTML = remVal;
        document.getElementById('pcpAttr').innerHTML = currVal;
    }

    pcpSkillsUp() {
        let currVal = parseInt(document.getElementById('pcpSkills').innerHTML);
        let remVal = parseInt(document.getElementById('pcpRemain').innerHTML);
        if (currVal < 10 && remVal > 0) {
            currVal += 1;
            remVal -= 1;
        }
        document.getElementById('pcpRemain').innerHTML = remVal;
        document.getElementById('pcpSkills').innerHTML = currVal;
    }

    pcpSkillsDn() {
        let currVal = parseInt(document.getElementById('pcpSkills').innerHTML);
        let remVal = parseInt(document.getElementById('pcpRemain').innerHTML);
        if (currVal > 1) {
            currVal -= 1;
            remVal += 1;
        }
        document.getElementById('pcpRemain').innerHTML = remVal;
        document.getElementById('pcpSkills').innerHTML = currVal;
    }

    pcpProfsUp() {
        let currVal = parseInt(document.getElementById('pcpProfs').innerHTML);
        let remVal = parseInt(document.getElementById('pcpRemain').innerHTML);
        if (currVal < 10 && remVal > 0) {
            currVal += 1;
            remVal -= 1;
        }
        document.getElementById('pcpRemain').innerHTML = remVal;
        document.getElementById('pcpProfs').innerHTML = currVal;
    }

    pcpProfsDn() {
        let currVal = parseInt(document.getElementById('pcpProfs').innerHTML);
        let remVal = parseInt(document.getElementById('pcpRemain').innerHTML);
        if (currVal > 1) {
            currVal -= 1;
            remVal += 1;
        }
        document.getElementById('pcpRemain').innerHTML = remVal;
        document.getElementById('pcpProfs').innerHTML = currVal;
    }

    pcpWealthUp() {
        let currVal = parseInt(document.getElementById('pcpWealth').innerHTML);
        let remVal = parseInt(document.getElementById('pcpRemain').innerHTML);
        if (currVal < 10 && remVal > 0) {
            currVal += 1;
            remVal -= 1;
        }
        document.getElementById('pcpRemain').innerHTML = remVal;
        document.getElementById('pcpWealth').innerHTML = currVal;
    }

    pcpWealthDn() {
        let currVal = parseInt(document.getElementById('pcpWealth').innerHTML);
        let remVal = parseInt(document.getElementById('pcpRemain').innerHTML);
        if (currVal > 1) {
            currVal -= 1;
            remVal += 1;
        }
        document.getElementById('pcpRemain').innerHTML = remVal;
        document.getElementById('pcpWealth').innerHTML = currVal;
    }

    pcpBoonsUp() {
        let currVal = parseInt(document.getElementById('pcpBoons').innerHTML);
        let remVal = parseInt(document.getElementById('pcpRemain').innerHTML);
        if (currVal < 10 && remVal > 0) {
            currVal += 1;
            remVal -= 1;
        }
        document.getElementById('pcpRemain').innerHTML = remVal;
        document.getElementById('pcpBoons').innerHTML = currVal;
    }

    pcpBoonsDn() {
        let currVal = parseInt(document.getElementById('pcpBoons').innerHTML);
        let remVal = parseInt(document.getElementById('pcpRemain').innerHTML);
        if (currVal > 1) {
            currVal -= 1;
            remVal += 1;
        }
        document.getElementById('pcpRemain').innerHTML = remVal;
        document.getElementById('pcpBoons').innerHTML = currVal;
    }

    checkRaceOptions() {
        var dict = {1:['Human', 'Goblin'], 2:['Dwarf', 'Zell'],
                    3:'No Associated Races', 4:['Burdinadin', 'Ohanedin'],
                    5:'No Associated Races', 6:['Orredin'],
                    7:'No Associated Races',
                    8:['Sarturi Chosen', 'Genosian Paladin',
                       'Dessian Silver Guard']};
        let spentPcp = parseInt(document.getElementById('pcpRace').innerHTML);
        let availRaces = dict[spentPcp];
        let selector = document.getElementById('charRace');
        selector.innerHTML = "";
        for (let raceOpt of availRaces) {
            let newOpt = document.createElement('option');
            newOpt.innerHTML = raceOpt;
            selector.appendChild(newOpt);
        }
    }
}

var bController = new BuildController();
