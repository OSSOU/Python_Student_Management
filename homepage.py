import customtkinter as ctk
import subprocess
from tkinter import messagebox

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

login = ctk.CTk()
login.geometry("500*350")
login.title("Username")

def exec_file(nom_fichier):
    try:
        subprocess.run(["python", nom_fichier], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors de l'exécution de {nom_fichier}: {e}")

def connexion():
    print("Bienvenu")
    username = champ1.get()
    password = champ2.get()
    
    VALID_USERNAME = "josue_nickil"
    VALID_PASSWORD = "8081"
    
    # Check credentials
    if username == VALID_USERNAME and password == VALID_PASSWORD:
       exec_file("Student_management.py")
       sys.exit("homepage.py")
    else :
       messagebox.showerror("Incorrect Username or Password , retry")

frame = ctk.CTkFrame(master = login)
frame.pack(pady = 20, padx = 60, fill="both", expand=True)

label = ctk.CTkLabel(master = frame, text="Connect")
label.pack(pady=12, padx=10)

champ1 = ctk.CTkEntry(master = frame, placeholder_text = "Identifiant")
champ1.pack(pady = 12)

champ2 = ctk.CTkEntry(master = frame, placeholder_text = "Mot de passe", show ="*")
champ2.pack(pady = 12)

button = ctk.CTkButton(master = frame, text = "Connexion", command = connexion)
button.pack()

checkbox = ctk.CTkCheckBox(master = frame, text="Se souvenir de moi")
login.mainloop()
