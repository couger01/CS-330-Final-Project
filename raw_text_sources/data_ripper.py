import re, json, fileinput


pattern_hyperref = "\\\\hyperref.*?\}"
pattern_curly_cleanup = "\}"
pattern_nameref = "\\\\nameref\{.*?:"
pattern_curly_clause = "\{.*?\}"
pattern_item = "\\\\item"
pattern_slashes = "\\\\*"

strip_hyperref = re.compile(pattern_hyperref)
strip_loose_curly = re.compile(pattern_curly_cleanup)
strip_nameref = re.compile(pattern_nameref)
strip_curly_clause = re.compile(pattern_curly_clause)
strip_item = re.compile(pattern_item)
strip_slashes = re.compile(pattern_slashes)


def rip_skills():
    skill_file = fileinput.input("skills.txt")
    skills = []
    for line in skill_file:
        clean_line = line.strip()
        clean_line = strip_item.sub("", clean_line)
        clean_line = strip_nameref.sub("", clean_line)
        clean_line = strip_loose_curly.sub("", clean_line)
        if clean_line != "":
            skills.append(clean_line)
    return skills


def rip_boons():
    boon_file = fileinput.input("boons.txt")
    boons = []
    for line in boon_file:
        clean_line = line.strip()
        clean_line = strip_nameref.sub("", clean_line)
        clean_line = strip_loose_curly.sub("", clean_line)
        clean_line = strip_slashes.sub("", clean_line)
        if clean_line != "":
            bits = clean_line.split('&')
            bits = [bits[0].strip(), bits[2].strip()]
            boons.append(bits)
    return boons


def rip_banes():
    bane_file = fileinput.input("banes.txt")
    banes = []
    for line in bane_file:
        clean_line = line.strip()
        clean_line = strip_nameref.sub("", clean_line)
        clean_line = strip_loose_curly.sub("", clean_line)
        clean_line = strip_slashes.sub("", clean_line)
        if clean_line != "":
            bits = clean_line.split('&')
            bits = [bits[0].strip(), bits[2].strip()]
            banes.append(bits)
    return banes


def rip_weapons():
    wep_file = fileinput.input("weapons.txt")
    weps = []
    for line in wep_file:
        clean_line = line.strip()
        clean_line = strip_nameref.sub("", clean_line)
        clean_line = strip_curly_clause.sub("", clean_line)
        clean_line = strip_loose_curly.sub("", clean_line)
        clean_line = strip_slashes.sub("", clean_line)
        if clean_line != "":
            bits = clean_line.split('&')
            del bits[1]
            bits = [bit.strip() for bit in bits]
            weps.append(bits)
    return weps


def rip_armor():
    armor_file = fileinput.input("armor.txt")
    armor = []
    for line in armor_file:
        clean_line = line.strip()
        clean_line = strip_nameref.sub("", clean_line)
        clean_line = strip_hyperref.sub("", clean_line)
        clean_line = strip_curly_clause.sub("", clean_line)
        clean_line = strip_loose_curly.sub("", clean_line)
        clean_line = strip_slashes.sub("", clean_line)
        if clean_line != "":
            bits = clean_line.split('&')
            bits = [bit.strip() for bit in bits]
            armor.append(bits)
    return armor


skills = rip_skills()
boons = rip_boons()
banes = rip_banes()
weapons = rip_weapons()
armor = rip_armor()

j_obj = {'skills': skills, 'boons': boons, 'banes': banes,
         'weapons': weapons, 'armor': armor}

with open('data.json', 'w') as f:
    json.dump(j_obj, f)
