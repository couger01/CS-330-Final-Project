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
        document.getElementById('pcpSpentProf').innerHTML = currVal
        document.getElementById('ProfPoints'). innerHTML = (currVal - 1) * 3;
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
        document.getElementById('pcpSpentProf').innerHTML = currVal
        document.getElementById('ProfPoints'). innerHTML = (currVal - 1) * 3;
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
        document.getElementById('pcpSpentBoon').innerHTML = currVal
        document.getElementById('BoonPoints'). innerHTML = (currVal - 4) * 5;
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
        document.getElementById('pcpSpentBoon').innerHTML = currVal
        document.getElementById('BoonPoints'). innerHTML = (currVal - 4) * 5;
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

            fSkill = document.getElementById('skill');
            fSkill.value += skillName + " " + skillLevel + ",";
        }
    }

    addSchool() {
        let school = document.getElementById('schoolSelector').value;
        let cost = {'Scrapper': 0, 'Soldier': 1, 'Officer': 3, 'Noble': 5,
                    'Traditional Fencer': 5, 'Unorthodox Fencer': 5,
                    'Esoteric': 8}
        let sCost = cost[school];
        let points = parseInt(document.getElementById('ProfPoints').innerHTML);
        if (sCost > points) {
            alert("Desired school too expensive")
        }else if (document.getElementById('sButton').disabled == "disabled") {
            alert("There can only be one School")
        } else {
            document.getElementById('ProfPoints'). innerHTML = points - sCost;
            let newRow = document.createElement('tr')
            let sName = document.createElement('td')
            let sLvl = document.createElement('td')
            sName.innerHTML = school;
            sLvl.id = "schoolLevel";
            sLvl.innerHTML = 1;
            newRow.appendChild(sName);
            newRow.appendChild(sLvl);
            document.getElementById('schoolTable').appendChild(newRow);
            document.getElementById('sButton').disabled = "disabled";
        }
    }

    addProf() {
        let prof = document.getElementById('profSelector').value;
        let points = parseInt(document.getElementById('ProfPoints').innerHTML);
        if (points < 1) {
            alert("No more points to spend")
        } else {
            document.getElementById('ProfPoints'). innerHTML = points - 1;
            let newRow = document.createElement('tr')
            let pName = document.createElement('td')
            let pLvl = document.createElement('td')
            pLvl.className = "profLevel";
            pName.innerHTML = prof;
            pLvl.innerHTML = 1;
            newRow.appendChild(pName);
            newRow.appendChild(pLvl);
            document.getElementById('profTable').appendChild(newRow);
        }
    }

    profLvlUp() {
        let points = parseInt(document.getElementById('ProfPoints').innerHTML);
        if (points < 1) {
            alert("No more points to spend")
        } else {
            document.getElementById('ProfPoints'). innerHTML = points - 1;
            let sLvl = parseInt(document.getElementById("schoolLevel").innerHTML);
            let pLvls = document.getElementsByClassName('profLevel');
            sLvl += 1;
            for (let i = 0; i < pLvls.length; i++) {
                pLvls[i].innerHTML = sLvl;
            }
            document.getElementById('schoolLevel').innerHTML = sLvl;
            fSkill = document.getElementById('skill');
            fSkill.value += Name + " " + skillLevel + ",";
        }
    }

    addBB() {
        let points = parseInt(document.getElementById('BoonPoints').innerHTML);
        let boon = document.getElementById('boonRad').checked;
        let bbName = document.getElementById('bbEntry').value;
        let bbCost = parseInt(document.getElementById('bbCost').value);
        if (points > bbCost && boon) {
            document.getElementById('BoonPoints').innerHTML = points - bbCost;
            let newRow = document.createElement('tr');
            let bType = document.createElement('td');
            let bName = document.createElement('td');
            let bCost = document.createElement('td');
            bName.innerHTML = bbName;
            bCost.innerHTML = bbCost;
            bType.innerHTML = "Boon";
            newRow.appendChild(bType);
            newRow.appendChild(bName);
            newRow.appendChild(bCost);
            document.getElementById('bbTable').appendChild(newRow)
        } else if (!boon) {
            document.getElementById('BoonPoints').innerHTML = points + bbCost;
            let newRow = document.createElement('tr');
            let bType = document.createElement('td');
            let bName = document.createElement('td');
            let bCost = document.createElement('td');
            bName.innerHTML = bbName;
            bCost.innerHTML = bbCost;
            bType.innerHTML = "Bane";
            newRow.appendChild(bType);
            newRow.appendChild(bName);
            newRow.appendChild(bCost);
            document.getElementById('bbTable').appendChild(newRow)
        } else {
            alert("Insufficient points to cover Boon cost")
        }
    }

    searchWep() {
        var wepName = document.getElementById('wSearch').value;
        $.ajax({
            url: "http://localhost:5000/api/weapons/search/"+wepName,
            method: "GET"
        }).done(function(data) {
            var weps = JSON.parse(data)
        }).fail(function() {
            alert("unable to search weapons")
        });
        for (let i=0; i < weps.length; i++) {
            let newRow = document.createElement('tr');
            let wId = document.createElement('td');
            let wName = document.createElement('td');
            let wButt = document.createElement('td');
            let addButt = document.createElement('button');

            addButt.className = "btn btn-default";
            addButt.innerHTML = "Add";
            addButt.type = "button";
            addButt.onclick = "bController.addWep("+ weps[i].id +weps[i].name+")"
            wButt.innerHTML = addButt;
            wName.innerHTML = weps[i].name;
            wId.innerHTML = weps[i].id;
            newRow.appendChild(wId);
            newRow.appendChild(wName);
            newRow.appendChild(wButt);
            document.getElementById('wepSearchRes').appendChild(newRow);
        }
    }

    searchArm() {
        var armName = document.getElementById('aSearch').value;
        $.ajax({
            url: "http://localhost:5000/api/armor/search/"+armName,
            method: "GET"
        }).done(function(data) {
            var arms = JSON.parse(data)
        }).fail(function() {
            alert("unable to search weapons")
        });
        for (let i=0; i < arms.length; i++) {
            let newRow = document.createElement('tr');
            let aId = document.createElement('td');
            let aName = document.createElement('td');
            let aButt = document.createElement('td');
            let addButt = document.createElement('button');

            addButt.className = "btn btn-default";
            addButt.innerHTML = "Add";
            addButt.type = "button";
            addButt.onclick = "bController.addArm("+ arms[i].id +arms[i].name+")"
            aButt.innerHTML = addButt;
            aName.innerHTML = arms[i].name;
            waId.innerHTML = arms[i].id;
            newRow.appendChild(aId);
            newRow.appendChild(aName);
            newRow.appendChild(aButt);
            document.getElementById('armSearchRes').appendChild(newRow);
        }
    }

    addWep(wepId, wepName) {
        let newRow = document.createElement('tr');
        let wId = document.createElement('td');
        let wName = document.createElement('td');
        wId.innerHTML = wepId;
        wName.innerHTML = wepName;
        newRow.appendChild(wId);
        newRow.appendChild(wName);
        document.getElementById('selWep').appendChild(newRow);
    }

    addWep(armId, armName) {
        let newRow = document.createElement('tr');
        let aId = document.createElement('td');
        let aName = document.createElement('td');
        aId.innerHTML = armId;
        aName.innerHTML = armName;
        newRow.appendChild(aId);
        newRow.appendChild(aName);
        document.getElementById('selArm').appendChild(newRow);
    }

    popSend() {
        fName = document.getElementById('name');
        fAge = document.getElementById('age');
        fSaga = document.getElementById('saga');
        fEpic = document.getElementById('epic');
        fBelief = document.getElementById('belief');
        fGlory = document.getElementById('glory');
        fFlaw = document.getElementById('flaw');
        fpcp_total = document.getElementById('pcp_total');
        fpcp_race = document.getElementById('pcp_race');
        fpcp_attr = document.getElementById('pcp_attr');
        fpcp_skills = document.getElementById('pcp_skills');
        fpcp_profs = document.getElementById('pcp_profs');
        fpcp_wealth = document.getElementById('pcp_wealth');
        fpcp_boons = document.getElementById('pcp_boons');
        fBio = document.getElementById('bio');
        fRace = document.getElementById('race');
        f_STR = document.getElementById('f_STR');
        f_AGI = document.getElementById('f_AGI');
        f_END = document.getElementById('f_END');
        f_HLT = document.getElementById('f_HLT');
        f_WIL = document.getElementById('f_WIL');
        f_WIT = document.getElementById('f_WIT');
        f_INT = document.getElementById('f_INT');
        f_PER = document.getElementById('f_PER');
        f_ADR = document.getElementById('f_ADR');
        f_MOB = document.getElementById('f_MOB');
        f_CAR = document.getElementById('f_CAR');
        f_TOU = document.getElementById('f_TOU');
        f_CHA = document.getElementById('f_CHA');
        f_GRIT = document.getElementById('f_GRIT');
        fSkill = document.getElementById('skill');
        fSchool = document.getElementById('school');
        fProf = document.getElementById('prof');
        fWep = document.getElementById('weapons');
        fArm = document.getElementById('armour');

        fName.value = document.getElementById('charName').value;
        fAge.value = parseInt(document.getElementById('charAge').value);
        fSaga.value = document.getElementById('charArcSaga').value;
        fEpic.value = document.getElementById('charArcEpic').value;
        fBelief.value = document.getElementById('charArcBelief').value;
        fGlory.value = document.getElementById('charArcGlory').value;
        fFlaw.value = document.getElementById('charArcFlaw').value;

        fpcp_total.value = document.getElementById('pcpSelect').value;
        fpcp_race.value = parseInt(document.getElementById('pcpRace').innerHTML);
        fpcp_attr.value = parseInt(document.getElementById('pcpAttr').innerHTML);
        fpcp_skills.value = parseInt(document.getElementById('pcpSkills').innerHTML);
        fpcp_profs.value = parseInt(document.getElementById('pcpProfs').innerHTML);
        fpcp_wealth.value = parseInt(document.getElementById('pcpWealth').innerHTML);
        fpcp_boons.value = parseInt(document.getElementById('pcpBoons').innerHTML);

        fBio.value = document.getElementById('charBio').value;
        fRace.value = document.getElementById('charRace').value;
        f_STR.value = parseInt(document.getElementById('STR').innerHTML);
        f_AGI.value = parseInt(document.getElementById('AGI').innerHTML);
        f_END.value = parseInt(document.getElementById('END').innerHTML);
        f_HLT.value = parseInt(document.getElementById('HLT').innerHTML);
        f_WIL.value = parseInt(document.getElementById('WIL').innerHTML);
        f_WIT.value = parseInt(document.getElementById('WIT').innerHTML);
        f_INT.value = parseInt(document.getElementById("INT").innerHTML);
        f_PER.value = parseInt(document.getElementById('PER').innerHTML);
        f_ADR.value = parseInt(document.getElementById('ADR').innerHTML);
        f_MOB.value = parseInt(document.getElementById('MOB').innerHTML);
        f_CAR.value = parseInt(document.getElementById('CAR').innerHTML);
        f_TOU.value = parseInt(document.getElementById('TOU').innerHTML);
        f_CHA.value = parseInt(document.getElementById('CHA').innerHTML);
        f_GRIT.value = parseInt(document.getElementById('GRIT').innerHTML);

        document.getElementById('finally').submit();
    }
}

var bController = new BuildController();
