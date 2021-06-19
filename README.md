# Tarkov-Gear-Selector
A tarkov gear selector made in python by Prince and Ethasia. Using https://pypi.org/project/pykov-eft/ as a base, thank you! They are 100% a more competent coder than myself or ethaisa.

For contact: Prince#1428 OR ethaisa123#1396

This program will take a budget that you give it, and the percentages via a tkinter GUI and give you the ID for the item that is the most expensive according to your budget allocation.

It achieves this via sending a POST request to the tarkov items endpoint and running that data through some filtering rules.

Example: 100k budget split between 5 items (rig, helm, armor, wep, backpack). 20k per item. It'll get the most expensive item on the flea market that is under 20k. At the time of writing, the output was:

Helmet: SSH-68
Wep: Vepr KM 136
Rig: Bear 6g112
Pack: Sanitar_Medbag
Armor: Ushanka (Not really armour but 20k is a little cheap for armor, don't you think?)

WARNING: This does ping a tarkov API. If you ping it too much, there's a chance yoyu may be banned because they think you're a bot. USE AT YOUR OWN RISK WE ARE NOT LIABLE FOR ANY NEGATIVE EFFECTS.

Usage instructions:
Download all the files and chuck them into the same folder.
Head over to exmaple.py and input your tarkov details in the relevant fields (it uses it to auth on the website and is saved in that file only.)
Run example.py.
??
Profit.
