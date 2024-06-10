import tkinter as tk
from tkinter import messagebox

def welcomeMessage(username, names):
    # Create a Tkinter window
    window = tk.Toplevel(root)
    window.title("Admin Box")
    window.geometry("500x200")

    label_1 = tk.Label(window, text=f"Welcome {username}\n")
    label_1.pack()
    label_2 = tk.Label(window, text="This is GIG Logistics biometrics")
    label_2.pack()
    label_3 = tk.Label(window, text=f"Other names: \n{names}")
    label_3.pack()    



    # Run the Tkinter event Loop
    root.mainloop()

def submit():
    username = username_entry.get()
    department = department_entry.get()
    names = []
    
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
        if officeinfo[key] == department:
            names.append(key);
    a = 0;
    for i in officeinfo:
        if username == i and department == officeinfo[i]:
            welcomeMessage(username, names);
        else:
            a+=1;
    if a >= 40:        
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
department_label = tk.Label(root, text="department:")
department_label.pack()
department_entry = tk.Entry(root)
department_entry.pack()

# Create submit button
submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.pack()

# run the main event loop
root.mainloop()