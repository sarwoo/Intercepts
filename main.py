import json
import tkinter as tk
from tkinter.ttk import Combobox
from tkinter import messagebox

# ---------------------------- UI SETUP ------------------------------- #


def save_entry():
    name = name_entry.get()
    location = location_entry.get()
    address = address_entry.get()
    postcode = postcode_entry.get()
    telephone = telephone_entry.get()

    new_data = {
        f"{postcode}_{name}": {
            "name": name,
            "location": location,
            "address": address,
            "postcode": postcode,
            "telephone": telephone
        }
    }

    if len(name) == 0 or len(location) == 0 or len(postcode) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
        return
    else:
        try:
            with open("data.json", "r") as file:
                data = json.load(file)
                print("open")
        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
                print("New file")
        else:
            data.update(new_data)
            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)
                print("update")
        finally:
            print("...")


def populate_names():
    return ['Asda', 'Co-op', 'Farmfoods', 'Morrisons', 'Tesco']


# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title("Interception")
window.config(padx=36, pady=36)

# Field labels
name_label = tk.Label(text="Name:")
name_label.grid(column=0, row=0, sticky="e")

location_label = tk.Label(text="Location:")
location_label.grid(column=0, row=1, sticky="e")

address_label = tk.Label(text="Address:")
address_label.grid(column=0, row=2, sticky="e")

postcode_label = tk.Label(text="Postcode:")
postcode_label.grid(column=0, row=3, sticky="e")

telephone_label = tk.Label(text="Telephone:")
telephone_label.grid(column=0, row=4, sticky="e")

# Field entry
name_entry = Combobox()
name_entry['values'] = populate_names()
name_entry.grid(column=1, row=0, sticky="w")

location_entry = Combobox()
location_entry.grid(column=1, row=1, sticky="nsw")

address_entry = tk.Entry()
address_entry.grid(column=1, row=2, sticky="w")

postcode_entry = tk.Entry()
postcode_entry.grid(column=1, row=3, sticky="w")

telephone_entry = tk.Entry()
telephone_entry.grid(column=1, row=4, sticky="w")

# Buttons
save_button = tk.Button(text="Save", command=save_entry)
save_button.grid(column=0, row=5, sticky="nesw")

window.mainloop()
