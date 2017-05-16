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
        var pcpToPoints = {1: 26, 2: 29, 3: 32, 4: 35, 5: 38, 6: 40, 7: 42,
                           8: 44, 9: 46, 10: 48};
        let currVal = parseInt(document.getElementById('pcpAttr').innerHTML);
        let remVal = parseInt(document.getElementById('pcpRemain').innerHTML);
        if (currVal < 10 && remVal > 0) {
            currVal += 1;
            remVal -= 1;
        }
        document.getElementById('pcpRemain').innerHTML = remVal;
        document.getElementById('pcpAttr').innerHTML = currVal;
        let spentPoints = 0;
        let attrIds = ['STR', 'AGI', 'END', 'HLT', 'WIL', 'WIT', 'INT', 'PER'];
        for (let aId of attrIds) {
            spentPoints += parseInt(document.getElementById(aId).innerHTML);
        }
        document.getElementById('pcpSpentAttr').innerHTML = currVal;
        document.getElementById('AttrPoints').innerHTML = pcpToPoints[currVal] - spentPoints;
    }

    pcpAttrDn() {
        var pcpToPoints = {1: 26, 2: 29, 3: 32, 4: 35, 5: 38, 6: 40, 7: 42,
                           8: 44, 9: 46, 10: 48};
        let currVal = parseInt(document.getElementById('pcpAttr').innerHTML);
        let remVal = parseInt(document.getElementById('pcpRemain').innerHTML);
        if (currVal > 1) {
            currVal -= 1;
            remVal += 1;
        }
        document.getElementById('pcpRemain').innerHTML = remVal;
        document.getElementById('pcpAttr').innerHTML = currVal;
        let spentPoints = 0;
        let attrIds = ['STR', 'AGI', 'END', 'HLT', 'WIL', 'WIT', 'INT', 'PER'];
        for (let aId of attrIds) {
            spentPoints += parseInt(document.getElementById(aId).innerHTML);
        }
        document.getElementById('pcpSpentAttr').innerHTML = currVal;
        document.getElementById('AttrPoints').innerHTML = pcpToPoints[currVal] - spentPoints;
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
        document.getElementById('pcpSpentSkill').innerHTML = currVal
        document.getElementById('SkillPoints'). innerHTML = (currVal - 1) * 3;
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
        document.getElementById('pcpSpentSkill').innerHTML = currVal
        document.getElementById('SkillPoints'). innerHTML = (currVal - 1) * 3;
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

    attrUp(attrId) {
        let remVal = parseInt(document.getElementById('AttrPoints').innerHTML);
        let currVal = parseInt(document.getElementById(attrId).innerHTML);
        if (currVal < 10 && remVal > 0) {
            remVal -= 1;
            currVal += 1;
        }
        document.getElementById('AttrPoints').innerHTML = remVal;
        document.getElementById(attrId).innerHTML = currVal;
    }

    attrDn(attrId) {
        let remVal = parseInt(document.getElementById('AttrPoints').innerHTML);
        let currVal = parseInt(document.getElementById(attrId).innerHTML);
        if (currVal > 1) {
            remVal += 1;
            currVal -= 1;
        }
        document.getElementById('AttrPoints').innerHTML = remVal;
        document.getElementById(attrId).innerHTML = currVal;
    }

    calcCompound() {
        let agi = parseInt(document.getElementById('AGI').innerHTML);
        let wit = parseInt(document.getElementById('WIT').innerHTML);
        let str = parseInt(document.getElementById('STR').innerHTML);
        let end = parseInt(document.getElementById('END').innerHTML);
        let hlt = parseInt(document.getElementById('HLT').innerHTML);
        let wil = parseInt(document.getElementById('WIL').innerHTML);
        let per = parseInt(document.getElementById('PER').innerHTML);

        let adr = Math.floor((agi + wit)/2);
        let mob = Math.floor((str + agi + end)/2);
        let car = str + end;
        let tou = Math.floor((str + end + hlt)/3);
        let cha = Math.floor((wil + per + wit)/2);
        let grit = Math.floor(wil/2);

        document.getElementById('ADR').innerHTML = adr;
        document.getElementById('MOB').innerHTML = mob;
        document.getElementById('CAR').innerHTML = car;
        document.getElementById('TOU').innerHTML = tou;
        document.getElementById('CHA').innerHTML = cha;
        document.getElementById('GRIT').innerHTML = grit;
    }

    addSkill() {
        let skillName = document.getElementById('skillSelector').value;
        let skillLevel = parseInt(document.getElementById('levelSkill').value);
        let SkillPoints = parseInt(document.getElementById('SkillPoints').innerHTML);
        if (skillLevel > SkillPoints) {
            alert("Desired skill level higher than available skill points");
        } else {
            document.getElementById('SkillPoints').innerHTML = SkillPoints - skillLevel;
            let newRow = document.createElement('tr')
            let sName = document.createElement('td')
            let sLvl = document.createElement('td')
            sName.innerHTML = skillName;
            sLvl.innerHTML = skillLevel;
            newRow.appendChild(sName);
            newRow.appendChild(sLvl);
            document.getElementById('skillTable').appendChild(newRow);
        }
    }
}

var bController = new BuildController();
