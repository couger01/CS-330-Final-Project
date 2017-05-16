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
        document.getElementById('pcpRemain').innerHTML = remVal;
        document.getElementById('pcpRace').innerHTML = currVal;
    }

    pcpRaceDn() {
        currVal = parseInt(document.getElementById('pcpRace').innerHTML);
        remVal = parseInt(document.getElementById('pcpRemain').innerHTML);
        if (currVal > 1) {
            currVal -= 1
            remVal == 1
        }
        document.getElementById('pcpRemain').innerHTML = remVal;
        document.getElementById('pcpRace').innerHTML = currVal;
    }

    pcpAttrUp() {
        currVal = parseInt(document.getElementById('pcpAttr').innerHTML);
        remVal = parseInt(document.getElementById('pcpRemain').innerHTML);
        if (currVal < 10 && remVal > 0) {
            currVal += 1
            remVal -= 1
        }
        document.getElementById('pcpRemain').innerHTML = remVal;
        document.getElementById('pcpAttr').innerHTML = currVal;
    }

    pcpAttrDn() {
        currVal = parseInt(document.getElementById('pcpAttr').innerHTML);
        remVal = parseInt(document.getElementById('pcpRemain').innerHTML);
        if (currVal > 1) {
            currVal -= 1
            remVal == 1
        }
        document.getElementById('pcpRemain').innerHTML = remVal;
        document.getElementById('pcpAttr').innerHTML = currVal;
    }

    pcpSkillsUp() {
        currVal = parseInt(document.getElementById('pcpSkills').innerHTML);
        remVal = parseInt(document.getElementById('pcpRemain').innerHTML);
        if (currVal < 10 && remVal > 0) {
            currVal += 1
            remVal -= 1
        }
        document.getElementById('pcpRemain').innerHTML = remVal;
        document.getElementById('pcpSkills').innerHTML = currVal;
    }

    pcpSkillsDn() {
        currVal = parseInt(document.getElementById('pcpSkills').innerHTML);
        remVal = parseInt(document.getElementById('pcpRemain').innerHTML);
        if (currVal > 1) {
            currVal -= 1
            remVal == 1
        }
        document.getElementById('pcpRemain').innerHTML = remVal;
        document.getElementById('pcpSkills').innerHTML = currVal;
    }

    pcpProfsUp() {
        currVal = parseInt(document.getElementById('pcpProfs').innerHTML);
        remVal = parseInt(document.getElementById('pcpRemain').innerHTML);
        if (currVal < 10 && remVal > 0) {
            currVal += 1
            remVal -= 1
        }
        document.getElementById('pcpRemain').innerHTML = remVal;
        document.getElementById('pcpProfs').innerHTML = currVal;
    }

    pcpProfsDn() {
        currVal = parseInt(document.getElementById('pcpProfs').innerHTML);
        remVal = parseInt(document.getElementById('pcpRemain').innerHTML);
        if (currVal > 1) {
            currVal -= 1
            remVal == 1
        }
        document.getElementById('pcpRemain').innerHTML = remVal;
        document.getElementById('pcpProfs').innerHTML = currVal;
    }

    pcpWealthUp() {
        currVal = parseInt(document.getElementById('pcpWealth').innerHTML);
        remVal = parseInt(document.getElementById('pcpRemain').innerHTML);
        if (currVal < 10 && remVal > 0) {
            currVal += 1
            remVal -= 1
        }
        document.getElementById('pcpRemain').innerHTML = remVal;
        document.getElementById('pcpWealth').innerHTML = currVal;
    }

    pcpWealthDn() {
        currVal = parseInt(document.getElementById('pcpWealth').innerHTML);
        remVal = parseInt(document.getElementById('pcpRemain').innerHTML);
        if (currVal > 1) {
            currVal -= 1
            remVal == 1
        }
        document.getElementById('pcpRemain').innerHTML = remVal;
        document.getElementById('pcpWealth').innerHTML = currVal;
    }

    pcpBoonsUp() {
        currVal = parseInt(document.getElementById('pcpBoons').innerHTML);
        remVal = parseInt(document.getElementById('pcpRemain').innerHTML);
        if (currVal < 10 && remVal > 0) {
            currVal += 1
            remVal -= 1
        }
        document.getElementById('pcpRemain').innerHTML = remVal;
        document.getElementById('pcpBoons').innerHTML = currVal;
    }

    pcpBoonsDn() {
        currVal = parseInt(document.getElementById('pcpBoons').innerHTML);
        remVal = parseInt(document.getElementById('pcpRemain').innerHTML);
        if (currVal > 1) {
            currVal -= 1
            remVal == 1
        }
        document.getElementById('pcpRemain').innerHTML = remVal;
        document.getElementById('pcpBoons').innerHTML = currVal;
    }
}

var bController = new BuildController();
