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
        currVal = parseInt(document.getElementById('pcpRace').innerHTML);
        remVal = parseInt(document.getElementById('pcpRemain').innerHTML);
        if (currVal < 8 && remVal > 0) {
            currVal += 1
            remVal -= 1
        }
    }

    pcpRaceDn() {
        currVal = parseInt(document.getElementById('pcpRace').innerHTML);
        remVal = parseInt(document.getElementById('pcpRemain').innerHTML);
    }

    pcpAttrUp() {
        currVal = parseInt(document.getElementById('pcpAttr').innerHTML);
        remVal = parseInt(document.getElementById('pcpRemain').innerHTML);
        if (currVal < 10 && remVal > 0) {
            currVal += 1
            remVal -= 1
        }
    }

    pcpAttrDn() {
        currVal = parseInt(document.getElementById('pcpAttr').innerHTML);
        remVal = parseInt(document.getElementById('pcpRemain').innerHTML);
    }

    pcpSkillsUp() {
        currVal = parseInt(document.getElementById('pcpSkills').innerHTML);
        remVal = parseInt(document.getElementById('pcpRemain').innerHTML);
        if (currVal < 10 && remVal > 0) {
            currVal += 1
            remVal -= 1
        }
    }

    pcpSkillsDn() {
        currVal = parseInt(document.getElementById('pcpSkills').innerHTML);
        remVal = parseInt(document.getElementById('pcpRemain').innerHTML);
    }

    pcpProfsUp() {
        currVal = parseInt(document.getElementById('pcpProfs').innerHTML);
        remVal = parseInt(document.getElementById('pcpRemain').innerHTML);
        if (currVal < 10 && remVal > 0) {
            currVal += 1
            remVal -= 1
        }
    }

    pcpProfsDn() {
        currVal = parseInt(document.getElementById('pcpProfs').innerHTML);
        remVal = parseInt(document.getElementById('pcpRemain').innerHTML);
    }

    pcpWealthUp() {
        currVal = parseInt(document.getElementById('pcpWealth').innerHTML);
        remVal = parseInt(document.getElementById('pcpRemain').innerHTML);
        if (currVal < 10 && remVal > 0) {
            currVal += 1
            remVal -= 1
        }
    }

    pcpWealthDn() {
        currVal = parseInt(document.getElementById('pcpWealth').innerHTML);
        remVal = parseInt(document.getElementById('pcpRemain').innerHTML);
    }

    pcpBoonsUp() {
        currVal = parseInt(document.getElementById('pcpBoons').innerHTML);
        remVal = parseInt(document.getElementById('pcpRemain').innerHTML);
        if (currVal < 10 && remVal > 0) {
            currVal += 1
            remVal -= 1
        }
    }

    pcpBoonsDn() {
        currVal = parseInt(document.getElementById('pcpBoons').innerHTML);
        remVal = parseInt(document.getElementById('pcpRemain').innerHTML);
    }
}

var bController = new BuildController();
