import worker as work

armor = work.armorDictFinal
helmets = work.helmetDictFinal
rig = work.rigDictFinal
wep = work.wepDictFinal
armored_rig = work.armorDictFinal
pack = work.packDictFinal

print(armor)
print(helmets)
print(rig)
print(wep)

# VARS
budget_rig = 0
budget_armor = 0
budget_helmet = 0
budget_backpack = 0
budget_wep = 0
x = 0
percent = 100

# PRE STUFF
budget_oval = int(input("what is your overall budget \n>>> "))


# DEF
def main(name, budget_oval, List, percent):
    budget_itempcnt = 0
    percent = percent - int(input("budget percentage for {} \n>>> ".format(name)))
    percentTotal = 100 - percent

    budget_item_price = (percentTotal / 100) * budget_oval
    print(budget_item_price)
    print(budget_itempcnt)

    output = max(k for k in List if k <= budget_item_price)
    print("ITEM: {}".format(List[output]))
    print("PRICE: {}".format(output))


# RIG
main("rig", budget_oval, rig, percent)
# armor
main("armor", budget_oval, armor, percent)
# pack
main("pack", budget_oval, pack, percent)
# wep
main("wep", budget_oval, wep, percent)
# helmet
main("helmet", budget_oval, helmets, percent)