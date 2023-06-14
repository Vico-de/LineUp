class IA:
    def __init__(self, budget, adversaire):
        self.budget = budget
        self.adversaire = adversaire
        self.risk = random.uniform(0, 1)  # Valeur aléatoire entre 0 et 1
        self.interest = self.calc_interest

    def calc_interest(self):

    def prendre_decision_enchere(self, carte_en_jeu):
        # Implémentez ici l'algorithme de décision de l'IA pour monter l'enchère ou passer
        # en fonction de son budget, de l'avantage de l'adversaire, du risque et de l'intérêt

        if self.risk * self.budget > ...:
            # L'IA choisit de monter l'enchère
            return True
        else:
            # L'IA choisit de passer
            return False
