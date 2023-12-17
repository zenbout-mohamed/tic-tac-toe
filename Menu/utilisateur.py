import json

class Utilisateur:
    def __init__(self, nom):
        self.nom = nom
        self.score = 0
        self.historique_scores = []

    def sauvegarder(self):
        # Sauvegarder les informations de l'utilisateur dans un fichier JSON
        with open(f"{self.nom}.json", "w") as fichier:
            json.dump({"nom": self.nom, "score": self.score, "historique_scores": self.historique_scores}, fichier)

    def charger(self):
        # Charger les informations de l'utilisateur depuis un fichier JSON
        try:
            with open(f"{self.nom}.json", "r") as fichier:
                data = json.load(fichier)
                self.score = data["score"]
                self.historique_scores = data["historique_scores"]
        except FileNotFoundError:
            pass
