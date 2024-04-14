import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

def welcomeMessage(username, names):
    # Create a Tkinter window
    window = tk.Toplevel(root)
    window.title("Admin Box")
    window.geometry("500x200")

    label_1 = tk.Label(window, text=f"Welcome {username}\n")
    label_1.pack()
    label_2 = tk.Label(window, text="This is GIG Logistics biometrics")
    label_2.pack()
    label_3 = tk.Label(window, text=f"Other names: {names}")
    label_3.pack()



    # Run the Tkinter event Loop
    root.mainloop()

def submit():
    username = username_entry.get()
    password = password_entry.get()
    names = []
    name = ""
    paswod = ""

    officeinfo = {"ADENIRAN": "logistics",
              "ADEWUMI": "accounting",
              "ADOH-AJAGBE": "delivery",
              "AGBAKURU-NWOGU": "accounting",
              "AGBAKWURU": "logistics",
              "AKINDE": "accounting",
              "ARNIKA": "logistics",
              "ATELLY": "delivery",
              "AZOGU": "delivery",
              "BETURE": "delivery",
              "CHUKWUMA": "logistics",
              "EBI": "accounting",
              "EGBORO": "administration",
              "EJEDIMU": "delivery",
              "ELERI": "administration",
              "EZE": "administration",
              "EZEONYE": "logistics",
              "GIWA": "logistics",
              "ICHA": "accounting",
              "IKPATI": "accounting",
              "ILOENYOSI": "delivery",
              "IYAWE": "delivery",
              "NWOKOLO": "logistics",
              "NWOTOKUBO": "logistics",
              "OBASOGIE": "accounting",
              "OBI": "accounting",
              "OBIALOR": "accounting",
              "OGBONNA": "delivery",
              "OIGBOCHIE": "delivery",
              "OKOCHA-OJEAH": "administration",
              "OKOLO": "administration",
              "OKORO": "logistics",
              "OLOWOKERE": "accounting",
              "OLUBUADE": "accounting",
              "OSEMEKE": "accounting",
              "OSSAI": "logistics",
              "PETER": "logistics",
              "QUADRI": "delivery",
              "UDE-IBE": "delivery",
              "UMEH": "administration"}
    for key in officeinfo:
        if officeinfo[key] == password:
            names.append(key)
            if key == username and officeinfo[key]== password:
                name += key
                paswod += officeinfo[key]
    if name == username and paswod == password:
        welcomeMessage(username, names)
    else:
        messagebox.showerror("Login","Invalid username or password")

# Create main window
root = tk.Tk()
root.title("Login Form")
root.geometry("500x200")


# Create username label and entry
username_label = tk.Label(root, text="Username:")
username_label.pack()
username_entry = tk.Entry(root)
username_entry.pack()

# Create password label and entry
password_label = tk.Label(root, text="password:")
password_label.pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()

# Create submit button
submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.pack()

# run the main event loop
root.mainloop()