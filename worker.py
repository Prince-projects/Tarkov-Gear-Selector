from itertools import islice


def lineCheck(linetocheck: str):
    cleaned_str = linetocheck.replace("\n", "")
    cleaned_str2 = cleaned_str.replace('"', "")
    cleaned_str3 = cleaned_str2.replace(",", "")
    cleaned_str4 = cleaned_str3.replace(" ", "")
    cleaned_str5 = cleaned_str4.replace(":", "")
    cleaned_str6 = cleaned_str5.replace("}", "")
    if cleaned_str6.isnumeric():
        return True


file = open("testing_get_all_items.txt", "r")
twoList = [[]]
num1 = 0
num2 = 1
weaponList = []
nameOccurence = True
helmet = False
helmetCat = []
bodyCat = []
rigCat = []
wepCat = []
packCat = []
armorrigCat = []
repairCost = False
faceShield = False
rigLayout = False
heightFace = False
# Iterate through the whole thing first, delete the shit between grid and lines. Save to a working var? idk? adn then do the following logic.
for linesB in file:
    PrimaryKey = lineCheck(linesB)
    # if "Name" in linesB and not "ShortName" in linesB and not "casingName" in linesB and not "GridLayoutName" in linesB and not "RigLayoutName" in linesB:
    if '"5' in linesB[:10]:
        print(linesB)
        num1 += 1
        twoList.append([])
    twoList[num1].append(linesB)

print(twoList[5])
print(twoList[10])
print(twoList[15])
nameDetect = False
for x in range(0, len(twoList)):
    for line in twoList[x]:
        if "RigLayoutName" in line:
            rigLayout = True
        if "Durability" in line:
            repairCost = True
        if "FaceShieldComponent" in line and "true" in line:
            faceShield = True
        if "Height" in line and "1" in line:
            heightFace = True
        if "MaterialType" in line and "Helmet" in line and repairCost and not faceShield:  # headwear Done!
            for linesC in twoList[x]:
                if "_name" in linesC and not nameDetect:
                    helmetCat.append(linesC)
                if "_name" in linesC:
                    nameDetect = True
                if "CreditsPrice" in linesC:
                    helmetCat.append(linesC)
        if "MaterialType" in line and 'BodyArmor' in line and not heightFace:  # Armor
            for linesC in twoList[x]:
                if "_name" in linesC and not nameDetect:
                    bodyCat.append(linesC)
                if "_name" in linesC:
                    nameDetect = True
                if "CreditsPrice" in linesC:
                    bodyCat.append(linesC)
        if "Durability" in line and rigLayout:  # Rig
            for linesC in twoList[x]:
                if "_name" in linesC and not nameDetect:
                    rigCat.append(linesC)
                if "_name" in linesC:
                    nameDetect = True
                if "CreditsPrice" in linesC:
                    rigCat.append(linesC)
        if "weapFireType" in line:
            for linesC in twoList[x]:
                if "_name" in linesC and not nameDetect:
                    wepCat.append(linesC)
                if "_name" in linesC:
                    nameDetect = True
                if "CreditsPrice" in linesC:
                    wepCat.append(linesC)
        if "GridLayoutName" in line:
            for linesC in twoList[x]:
                if "_name" in linesC and not nameDetect:
                    packCat.append(linesC)
                if "_name" in linesC:
                    nameDetect = True
                if "CreditsPrice" in linesC:
                    packCat.append(linesC)
    repairCost = False
    faceShield = False
    rigLayout = False
    heightFace = False
    nameDetect = False


def cleanString(category, endCategory, prices, names):
    for i in category:
        cleaned_str = i.replace("\n", "")
        cleaned_str1 = cleaned_str.replace("_name", "")
        cleaned_str2 = cleaned_str1.replace('"', "")
        cleaned_str3 = cleaned_str2.replace(",", "")
        cleaned_str4 = cleaned_str3.replace(" ", "")
        cleaned_str5 = cleaned_str4.replace(":", "")
        cleaned_str6 = cleaned_str5.replace("CreditsPrice", "")
        endCategory.append(cleaned_str6)
    for i in range(len(endCategory)):
        stringConv = str(endCategory[i])
        if stringConv.isnumeric():
            prices.append(stringConv)
        else:
            names.append(stringConv)
    prices = list(map(float, prices))
    finalDict = zip(prices, names)

    return finalDict


finalHelmetCat = []
helmetCatNames = []
helmetCatPrices = []
helmetDictFinal = dict(cleanString(helmetCat, finalHelmetCat, helmetCatPrices, helmetCatNames))
finalwepCat = []
wepCatNames = []
wepCatPrices = []
wepDictFinal = dict(cleanString(wepCat, finalwepCat, wepCatPrices, wepCatNames))
finalpackCat = []
packCatNames = []
packCatPrices = []
packDictFinal = dict(cleanString(packCat, finalpackCat, packCatPrices, packCatNames))
finalrigCat = []
rigCatNames = []
rigCatPrices = []
rigDictFinal = dict(cleanString(rigCat, finalrigCat, rigCatPrices, rigCatNames))
finalarmorCat = []
armorCatNames = []
armorCatPrices = []
armorDictFinal = dict(cleanString(bodyCat, finalarmorCat, armorCatPrices, armorCatNames))
print(armorDictFinal)
file.close()
# Add Name and _name to same line for dict. Solves issues.
