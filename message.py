import tkinter as tk
from tkinter import ttk
from tkinter import *
import worker as work
#dict example
helmets_dict = work.helmetDictFinal
weapon_dict = work.wepDictFinal
tacticalRig_dict = work.rigDictFinal
backpack_dict = work.packDictFinal
Armor_dict = work.armorDictFinal
inpt_bud = 0

#print(helmets_dict[max(k for k in helmets_dict if k <= input_budget)])
root = tk.Tk()
root.title("Tarvov Kit Creator")
root.geometry('350x690')
root.resizable(False, False)
#defines the function that updates the input text box for the overall budget



def update():
        global input_budget
        #HELM ------------------------------------------------------------------------
        #START
        percentage_helm = slider_percentage_helm.get()
        global helmets_dict
        helm_dict = helmets_dict
        try: 
                input_budget = int(input_budget)
                percentage_helm = int(percentage_helm)
                final_budget_item_helm = input_budget * (percentage_helm / 100)
        except:
                pass        
        else:
                final_item_name_helm = helm_dict[max(k for k in helm_dict if k <= final_budget_item_helm)]
                final_price_dict = {v: k for k, v in helm_dict.items()}
                final_price_helm = final_price_dict[final_item_name_helm]
                label_output_name_helm.config(text = "Name: {} | Price: {}".format(final_item_name_helm, final_price_helm))                
        slider_percentage_helm.config(command=lambda e: label_percentage_helm.config(text="Percentage of budget for Helmet:  "f"{(slider_percentage_helm.get()):0.00f}" + "%"))
        percentage_helm = slider_percentage_helm.get()
        #END
        
        #WEP ------------------------------------------------------------------------
        #START
        percentage_wep = slider_percentage_wep.get()
        global weapon_dict
        try: 
                input_budget = int(input_budget)
                percentage_wep = int(percentage_wep)
                final_budget_item_wep = input_budget * (percentage_wep / 100)
        except:
                pass        
        else:        
                wep_dict = weapon_dict
                final_item_name_wep = wep_dict[max(k for k in wep_dict if k <= final_budget_item_wep)]
                final_price_dict = {v: k for k, v in wep_dict.items()}
                final_price_wep = final_price_dict[final_item_name_wep]
                label_output_name_wep.config(text = "Name: {} | Price: {}".format(final_item_name_wep, final_price_wep))                
        
        slider_percentage_wep.config(command=lambda e: label_percentage_wep.config(text="Percentage of budget for Weapon:  "f"{(slider_percentage_wep.get()):0.00f}" + "%"))
        percentage_wep = slider_percentage_wep.get()
        #END
        
        #RIG ------------------------------------------------------------------------
        #START
        percentage_rig = slider_percentage_rig.get()
        global tacticalRig_dict
        try: 
                input_budget = int(input_budget)
                percentage_rig = int(percentage_rig)
                final_budget_item_rig = input_budget * (percentage_rig / 100)
        except:
                pass        
        else:        
                rig_dict = tacticalRig_dict
                final_item_name_rig = rig_dict[max(k for k in rig_dict if k <= final_budget_item_rig)]
                final_price_dict = {v: k for k, v in rig_dict.items()}
                final_price_rig = final_price_dict[final_item_name_rig]
                label_output_name_rig.config(text = "Name: {} | Price: {}".format(final_item_name_rig, final_price_rig))                
        
        slider_percentage_rig.config(command=lambda e: label_percentage_rig.config(text="Percentage of budget for Tacktical Rig:  "f"{(slider_percentage_rig.get()):0.00f}" + "%"))
        percentage_rig = slider_percentage_rig.get()
        #END        
        
        #BACK PACK ------------------------------------------------------------------------
        #START
        percentage_bag = slider_percentage_bag.get()
        global backpack_dict
        try: 
                input_budget = int(input_budget)
                percentage_bag = int(percentage_bag)
                final_budget_item_bag = input_budget * (percentage_bag / 100)
        except:
                pass        
        else:        
                bag_dict = backpack_dict
                final_item_name_bag = bag_dict[max(k for k in bag_dict if k <= final_budget_item_bag)]
                final_price_dict = {v: k for k, v in bag_dict.items()}
                final_price_bag = final_price_dict[final_item_name_bag]
                label_output_name_bag.config(text = "Name: {} | Price: {}".format(final_item_name_bag, final_price_bag))                
        
        slider_percentage_bag.config(command=lambda e: label_percentage_bag.config(text="Percentage of budget for backpack:  "f"{(slider_percentage_bag.get()):0.00f}" + "%"))
        percentage_bag = slider_percentage_bag.get()
        #END        
        #ARMOR ------------------------------------------------------------------------
        #START
        percentage_amr = slider_percentage_amr.get()
        global Armor_dict
        try: 
                input_budget = int(input_budget)
                percentage_amr = int(percentage_amr)
                final_budget_item_amr = input_budget * (percentage_amr / 100)
        except:
                pass        
        else:        
                amr_dict = Armor_dict
                final_item_name_amr = amr_dict[max(k for k in amr_dict if k <= final_budget_item_amr)]
                final_price_dict = {v: k for k, v in amr_dict.items()}
                final_price_amr = final_price_dict[final_item_name_amr]
                label_output_name_amr.config(text = "Name: {} | Price: {}".format(final_item_name_amr, final_price_amr))                
        
        slider_percentage_amr.config(command=lambda e: label_percentage_amr.config(text="Percentage of budget for armor:  "f"{(slider_percentage_amr.get()):0.00f}" + "%"))
        percentage_amr = slider_percentage_amr.get()
        #END
        root.after(200, update)       

#defines and places the items above the helmet line
frameOne = ttk.LabelFrame(text = "Type your overall budget here", padding = 10)
frameOne.place(x = 10, y = 10)
ttk.Label(root, text = "Helmet", ).place(x = 150, y = 70)
ttk.Label(root, text = "weapon", ).place(x = 150, y = 170)
ttk.Label(root, text = "Rig", ).place(x = 150, y = 270)
ttk.Label(root, text = "Backpack", ).place(x = 150, y = 370)
ttk.Label(root, text = "Armor", ).place(x = 150, y = 470)

#def and place sepporators
sep = ttk.Separator(root,  orient = tk.HORIZONTAL)
sep2 = ttk.Separator(root,  orient = tk.HORIZONTAL)
sep3 = ttk.Separator(root,  orient = tk.HORIZONTAL)
sep4 = ttk.Separator(root,  orient = tk.HORIZONTAL)
sep5 = ttk.Separator(root,  orient = tk.HORIZONTAL)
sep6 = ttk.Separator(root,  orient = tk.HORIZONTAL)

sep.place(x = 0, y = 90, relwidth = 1.0)
sep2.place(x = 0, y = 190, relwidth = 1.0)
sep3.place(x = 0, y = 290, relwidth = 1.0)
sep4.place(x = 0, y = 390, relwidth = 1.0)
sep5.place(x = 0, y = 490, relwidth = 1.0)
sep6.place(x = 0, y = 590, relwidth = 1.0)

#defines button and other labels

input_budget_txt = ttk.Entry(frameOne)
input_budget_txt.pack()
ttk.Label(root, text = "tarkov kit creator 1.14.4", ).place(x = 10, y = 660)


def update_2():
        global input_budget
        input_budget = input_budget_txt.get()


button = ttk.Button(root, text = "        confirm        ", command = update_2)
button.place(y =45 , x = 200,)

#HELMETS ----------------------------------------------------------------------

#defines percentage label and the final name and price label as well as the slider
label_percentage_helm = ttk.Label(root, text = "Percentage of budget for Helmet: 0%")
label_output_name_helm = ttk.Label(root, text = "Name:  | Price: 0")
slider_percentage_helm = ttk.Scale(root, from_= 0, to=100, orient=tk.HORIZONTAL, length = 300)
#places the percentage label and the final name and price label as well as the slider
slider_percentage_helm.place(x = 10, y = 100)
label_percentage_helm.place(x = 10, y = 130)
label_output_name_helm.place(x = 10, y = 150)


#WEAPONS ----------------------------------------------------------------------


#defines percentage label and the final name and price label as well as the slider
label_percentage_wep = ttk.Label(root, text = "Percentage of budget for Weapon: 0%")
label_output_name_wep = ttk.Label(root, text = "Name:  | Price: 0")
slider_percentage_wep = ttk.Scale(root, from_= 0, to=100, orient=tk.HORIZONTAL, length = 300)
#places the percentage label and the final name and price label as well as the slider
slider_percentage_wep.place(x = 10, y = 200)
label_percentage_wep.place(x = 10, y = 230)
label_output_name_wep.place(x = 10, y = 250)

#Rig ----------------------------------------------------------------------

#defines percentage label and the final name and price label as well as the slider
label_percentage_rig = ttk.Label(root, text = "Percentage of budget for Tacktical Rig: 0%")
label_output_name_rig = ttk.Label(root, text = "Name:  | Price: 0")
slider_percentage_rig = ttk.Scale(root, from_= 0, to=100, orient=tk.HORIZONTAL, length = 300)
#places the percentage label and the final name and price label as well as the slider
slider_percentage_rig.place(x = 10, y = 300)
label_percentage_rig.place(x = 10, y = 330)
label_output_name_rig.place(x = 10, y = 350)

#Bag ----------------------------------------------------------------------

#defines percentage label and the final name and price label as well as the slider
label_percentage_bag = ttk.Label(root, text = "Percentage of budget for Tacktical Rig: 0%")
label_output_name_bag = ttk.Label(root, text = "Name:  | Price: 0")
slider_percentage_bag = ttk.Scale(root, from_= 0, to=100, orient=tk.HORIZONTAL, length = 300)
#places the percentage label and the final name and price label as well as the slider
slider_percentage_bag.place(x = 10, y = 400)
label_percentage_bag.place(x = 10, y = 430)
label_output_name_bag.place(x = 10, y = 450)

#armor ----------------------------------------------------------------------

#defines percentage label and the final name and price label as well as the slider
label_percentage_amr = ttk.Label(root, text = "Percentage of budget for Tacktical Rig: 0%")
label_output_name_amr = ttk.Label(root, text = "Name:  | Price: 0")
slider_percentage_amr = ttk.Scale(root, from_= 0, to=100, orient=tk.HORIZONTAL, length = 300)
#places the percentage label and the final name and price label as well as the slider
slider_percentage_amr.place(x = 10, y = 500)
label_percentage_amr.place(x = 10, y = 530)
label_output_name_amr.place(x = 10, y = 550)



update()
root.mainloop()
