from random import randint
import tkinter
from tkinter import StringVar


class Initiative:

    def __init__(self, name, init_mod):
        self.name = name
        self.init_mod = init_mod
        self.init_roll = self.roll()

    def roll(self):
        return randint(1, 20) + self.init_mod


def sort_initiative(creatures):
    creatures = sorted(creatures, key=lambda c: c.init_roll, reverse=True)
    return creatures


def roll_initiative():
    for creature in creatures:
        creature.init_roll = creature.roll()
    display_creatures()
    return creatures


def add_creature(a):
    creature_name = creature_entry_box.get()
    creature_init_mod = modifier_entry_box.get()
    if creature_name == '':
        return
    if creature_init_mod == '':
        creature_init_mod = 0
    else:
        try:
            creature_init_mod = int(creature_init_mod)
        except ValueError:
            return
    creature_entry.set('')
    modifier_entry.set('')
    creatures.append(Initiative(creature_name, creature_init_mod))
    creature_entry_box.focus()
    display_creatures()


def display_creatures():
    global creatures
    creature_list.delete(0, 'end')
    creatures = sort_initiative(creatures)
    for item in creatures:
        creature_list.insert('end', item.name + '    ' + str(item.init_roll))


def remove_creature():
    try:
        selection = int(creature_list.curselection()[0])
        del creatures[selection]
        creature_list.delete(selection)
    except IndexError:
        return


creatures = []

root = tkinter.Tk()
root.title("Initiative roller")
creature_entry = StringVar()
modifier_entry = StringVar()

tkinter.Label(root, text="Creature designation:").grid(row=0, column=0)
creature_entry_box = tkinter.Entry(root, textvariable=creature_entry)
creature_entry_box.grid(row=0, column=1)
tkinter.Label(root, text="Initiative modifier:").grid(row=0, column=2)
modifier_entry_box = tkinter.Entry(root, textvariable=modifier_entry, width=3)
modifier_entry_box.grid(row=0, column=3)
creature_list = tkinter.Listbox(root, width=50)
creature_list.grid(row=1, column=0, columnspan=4)
delete_button = tkinter.Button(root, text="Remove Creature", command=remove_creature)
delete_button.grid(row=2, column=0)
initiative_button = tkinter.Button(root, text="Roll Initiative", command=roll_initiative)
initiative_button.grid(row=2, column=2)

creature_entry_box.bind("<Return>", add_creature)
modifier_entry_box.bind("<Return>", add_creature)
creature_entry_box.focus()

root.mainloop()
