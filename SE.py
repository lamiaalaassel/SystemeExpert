import tkinter as tk
from tkinter import messagebox
from ttkthemes import ThemedTk
from tkinter import ttk

class SystemeExpert:
    def __init__(self):
        self.regles = [
            {"conditions": {"écran noir", "pas de bip au démarrage"}, "action": "problème carte mère"},
            {"conditions": {"écran noir", "bip au démarrage"}, "action": "problème carte graphique"},
            {"conditions": {"ordinateur lent", "grésillement du disque dur"}, "action": "problème disque dur"},
            {"conditions": {"ordinateur lent", "écran bleu"}, "action": "problème mémoire RAM"},
            # Ajoutez d'autres règles ici selon vos besoins
        ]

    def afficher_organes_defectueux(self, symptomes):
        organes_defectueux = []
        for regle in self.regles:
            conditions = regle["conditions"]
            if conditions.issubset(symptomes):  # Utiliser la méthode issubset pour vérifier les conditions
                organes_defectueux.append(regle["action"])
        return organes_defectueux

    # Méthodes pour ajouter, modifier et supprimer des pannes
    def ajouter_panne(self, panne, causes):
        self.regles.append({"conditions": set(causes), "action": panne})

    def modifier_panne(self, ancienne_panne, nouvelle_panne, nouvelles_causes):
        for regle in self.regles:
            if regle["action"] == ancienne_panne:
                regle["action"] = nouvelle_panne
                regle["conditions"] = set(nouvelles_causes)

    def supprimer_panne(self, panne):
        self.regles = [regle for regle in self.regles if regle["action"] != panne]

    def afficher_pannes(self):
        pannes = {}
        for regle in self.regles:
            panne = regle["action"]
            causes = regle["conditions"]
            pannes.setdefault(panne, []).extend(causes)
        return pannes

class ConnexionExpert:
    def __init__(self):
        self.root = ThemedTk(theme="arc")
        self.root.title("Connexion - Expert")

        self.label_username = ttk.Label(self.root, text="Nom d'utilisateur :")
        self.label_username.pack()

        self.entry_username = ttk.Entry(self.root)
        self.entry_username.pack()

        self.label_password = ttk.Label(self.root, text="Mot de passe :")
        self.label_password.pack()

        self.entry_password = ttk.Entry(self.root, show="*")
        self.entry_password.pack()

        self.button_login = ttk.Button(self.root, text="Connexion", command=self.login)
        self.button_login.pack()

    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        # Vérifiez les informations de connexion pour l'expert à partir du fichier experts.txt
        if self.check_credentials("experts.txt", username, password):
            self.root.destroy()
            ExpertApplication()
        else:
            messagebox.showerror("Erreur de connexion", "Nom d'utilisateur ou mot de passe incorrect.")

    def check_credentials(self, filename, username, password):
        with open(filename, 'r') as file:
            for line in file:
                user, pwd = line.strip().split(' ')
                if user == username and pwd == password:
                    return True
        return False

class UtilisateurApplication:
    def __init__(self):
        self.root = ThemedTk(theme="arc")
        self.root.title("Système Expert")

        self.button_expert_mode = ttk.Button(self.root, text="Mode Expert", command=self.run_expert_mode)
        self.button_expert_mode.pack()

        self.button_user_mode = ttk.Button(self.root, text="Mode Utilisateur", command=self.run_user_mode)
        self.button_user_mode.pack()

        self.button_add_expert = ttk.Button(self.root, text="Ajouter Expert", command=self.add_expert)
        self.button_add_expert.pack()

        self.root.mainloop()

    def run_expert_mode(self):
        self.root.destroy()
        ConnexionExpert()

    def run_user_mode(self):
        self.root.destroy()
        UserApplication()

    def add_expert(self):
        add_expert_window = tk.Toplevel(self.root)
        add_expert_window.title("Ajouter un nouvel expert")

        label_username = ttk.Label(add_expert_window, text="Nom d'utilisateur :")
        label_username.pack()

        entry_username = ttk.Entry(add_expert_window)
        entry_username.pack()

        label_password = ttk.Label(add_expert_window, text="Mot de passe :")
        label_password.pack()

        entry_password = ttk.Entry(add_expert_window, show="*")
        entry_password.pack()

        button_add = ttk.Button(add_expert_window, text="Ajouter", command=lambda: self.add_new_expert(entry_username.get(), entry_password.get(), add_expert_window))
        button_add.pack()

    def add_new_expert(self, username, password, add_expert_window):
        with open("experts.txt", "a") as file:
            file.write(f"{username} {password}\n")
        add_expert_window.destroy()
        messagebox.showinfo("Nouvel expert ajouté", "Nouvel expert ajouté avec succès.")

class UserApplication:
    def __init__(self):
        self.root = ThemedTk(theme="arc")
        self.root.title("Système Expert - Mode Utilisateur")

        self.systeme = SystemeExpert()

        self.label_instructions = ttk.Label(self.root, text="Veuillez saisir les symptômes observés (séparés par des virgules) :")
        self.label_instructions.pack()

        self.entree_symptomes = ttk.Entry(self.root)
        self.entree_symptomes.pack()

        self.bouton_soumettre = ttk.Button(self.root, text="Soumettre", command=self.soumettre_symptomes)
        self.bouton_soumettre.pack()

        self.resultat = ttk.Label(self.root, text="")
        self.resultat.pack()

        self.root.mainloop()

    def soumettre_symptomes(self):
        symptomes = self.entree_symptomes.get()
        symptomes = symptomes.split(",")
        symptomes = [symptome.strip() for symptome in symptomes]

        organes_defectueux = self.systeme.afficher_organes_defectueux(symptomes)
        if organes_defectueux:
            self.resultat.configure(text=f"L'organe potentiellement défectueux est : {', '.join(organes_defectueux)}")
        else:
            self.resultat.configure(text="Aucun organe potentiellement défectueux trouvé pour les symptômes donnés.")

class ExpertApplication:
    def __init__(self):
        self.root = ThemedTk(theme="arc")
        self.root.title("Système Expert - Mode Expert")

        self.systeme = SystemeExpert()

        self.label_instructions = ttk.Label(self.root, text="Bienvenue, expert. Veuillez utiliser les boutons pour ajouter, modifier ou supprimer une panne.")
        self.label_instructions.pack()

        self.button_ajouter_panne = ttk.Button(self.root, text="Ajouter Panne", command=self.ajouter_panne)
        self.button_ajouter_panne.pack()

        self.button_modifier_panne = ttk.Button(self.root, text="Modifier Panne", command=self.modifier_panne)
        self.button_modifier_panne.pack()

        self.button_supprimer_panne = ttk.Button(self.root, text="Supprimer Panne", command=self.supprimer_panne)
        self.button_supprimer_panne.pack()

        self.afficher_pannes()

        self.root.mainloop()

    def ajouter_panne(self):
        ajout_panne_window = tk.Toplevel(self.root)
        ajout_panne_window.title("Ajouter Panne")

        label_panne = ttk.Label(ajout_panne_window, text="Nom de la panne :")
        label_panne.pack()

        entry_panne = ttk.Entry(ajout_panne_window)
        entry_panne.pack()

        label_causes = ttk.Label(ajout_panne_window, text="Causes (séparées par des virgules) :")
        label_causes.pack()

        entry_causes = ttk.Entry(ajout_panne_window)
        entry_causes.pack()

        button_valider = ttk.Button(ajout_panne_window, text="Valider", command=lambda: self.valider_ajout_panne(entry_panne.get(), entry_causes.get(), ajout_panne_window))
        button_valider.pack()

    def valider_ajout_panne(self, panne, causes, ajout_panne_window):
        causes_liste = [cause.strip() for cause in causes.split(",")]
        self.systeme.ajouter_panne(panne, causes_liste)
        ajout_panne_window.destroy()
        self.afficher_pannes()
        messagebox.showinfo("Panne ajoutée", f"La panne '{panne}' a été ajoutée avec succès.")

    def modifier_panne(self):
        modification_panne_window = tk.Toplevel(self.root)
        modification_panne_window.title("Modifier Panne")

        label_ancienne_panne = ttk.Label(modification_panne_window, text="Ancien nom de la panne :")
        label_ancienne_panne.pack()

        entry_ancienne_panne = ttk.Entry(modification_panne_window)
        entry_ancienne_panne.pack()

        label_nouvelle_panne = ttk.Label(modification_panne_window, text="Nouveau nom de la panne :")
        label_nouvelle_panne.pack()

        entry_nouvelle_panne = ttk.Entry(modification_panne_window)
        entry_nouvelle_panne.pack()

        label_nouvelles_causes = ttk.Label(modification_panne_window, text="Nouvelles causes (séparées par des virgules) :")
        label_nouvelles_causes.pack()

        entry_nouvelles_causes = ttk.Entry(modification_panne_window)
        entry_nouvelles_causes.pack()

        button_valider = ttk.Button(modification_panne_window, text="Valider", command=lambda: self.valider_modification_panne(entry_ancienne_panne.get(), entry_nouvelle_panne.get(), entry_nouvelles_causes.get(), modification_panne_window))
        button_valider.pack()

    def valider_modification_panne(self, ancienne_panne, nouvelle_panne, nouvelles_causes, modification_panne_window):
        nouvelles_causes_liste = [cause.strip() for cause in nouvelles_causes.split(",")]
        self.systeme.modifier_panne(ancienne_panne, nouvelle_panne, nouvelles_causes_liste)
        modification_panne_window.destroy()
        self.afficher_pannes()
        messagebox.showinfo("Panne modifiée", f"La panne '{ancienne_panne}' a été modifiée en '{nouvelle_panne}' avec les nouvelles causes '{', '.join(nouvelles_causes_liste)}'.")

    def supprimer_panne(self):
        suppression_panne_window = tk.Toplevel(self.root)
        suppression_panne_window.title("Supprimer Panne")

        label_panne = ttk.Label(suppression_panne_window, text="Nom de la panne à supprimer :")
        label_panne.pack()

        entry_panne = ttk.Entry(suppression_panne_window)
        entry_panne.pack()

        button_valider = ttk.Button(suppression_panne_window, text="Valider", command=lambda: self.valider_suppression_panne(entry_panne.get(), suppression_panne_window))
        button_valider.pack()

    def valider_suppression_panne(self, panne, suppression_panne_window):
        self.systeme.supprimer_panne(panne)
        suppression_panne_window.destroy()
        self.afficher_pannes()
        messagebox.showinfo("Panne supprimée", f"La panne '{panne}' a été supprimée avec succès.")

    def afficher_pannes(self):
        for widget in self.root.winfo_children():
            if widget not in [self.button_ajouter_panne, self.button_modifier_panne, self.button_supprimer_panne]:
                widget.destroy()

        pannes = self.systeme.afficher_pannes()
        for panne, causes in pannes.items():
            label_panne = ttk.Label(self.root, text=f"Panne: {panne}, Causes: {', '.join(causes)}")
            label_panne.pack()

if __name__ == "__main__":
    UtilisateurApplication()
