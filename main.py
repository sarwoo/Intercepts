import json
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.ttk import Combobox, Style
from tkinter import messagebox

# ---------------------------- Functionality ------------------------------- #


def save_entry():
    company = company_entry.get()
    location = location_entry.get()
    address = address_entry.get()
    postcode = postcode_entry.get()
    telephone = telephone_entry.get()

    compact_postcode = postcode.replace(" ", "")

    new_data = {
        f"{compact_postcode}_{company}": {
            "company": company,
            "location": location,
            "address": address,
            "postcode": postcode,
            "telephone": telephone
        }
    }

    if len(company) == 0 or len(location) == 0 or len(postcode) == 0:
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


def populate_company():
    return ['Asda', 'Co-op', 'Farmfoods', 'Lidl', 'Morrisons', 'Tesco']


# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title("Interception")
window.config(padx=36, pady=36)

# Field labels
company_label = tk.Label(text="Company:")
company_label.grid(column=0, row=0, sticky="e")

location_label = tk.Label(text="Location:")
location_label.grid(column=0, row=1, sticky="e")

address_label = tk.Label(text="Address:")
address_label.grid(column=0, row=2, sticky="e")

postcode_label = tk.Label(text="Postcode:")
postcode_label.grid(column=0, row=3, sticky="e")

telephone_label = tk.Label(text="Telephone:")
telephone_label.grid(column=0, row=4, sticky="e")

# Field entry
style = ttk.Style()
style.theme_use('default')

company_entry = Combobox()
company_entry['values'] = populate_company()
company_entry.grid(column=1, row=0, sticky="w")

location_entry = Combobox()
location_entry.grid(column=1, row=1, sticky="w")

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
