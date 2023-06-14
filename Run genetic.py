def run_gen(player_list):
    # Initialisation des IA
    ia_population = []
    for i in range(100):
        for i in range(5):
            player_list = {
                'name': f"IA {i + 1}",
                'budget': 1000000,
                'score': 0,
                'fame': 0,
                'inventory': {
                    'artists': [],
                    'scenes': [],
                    'events': []
                }
            }

    # Boucle de jeu
    for _ in range(10):
        carte_en_jeu = ...

        for ia in ia_population:
            decision = ia.prendre_decision_enchere(carte_en_jeu)
            if decision:
                # L'IA choisit de monter l'enchère
                ...

        ...

    ...


jouer_jeu()
