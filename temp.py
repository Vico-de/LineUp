def choix_manuel():


#--------------------------------------------------------------------
artist_discard = []


    # Boucle pour permettre aux joueurs de surenchérir ou de passer leur tour
    highest_bidder = None
    artist_cost = artist_card[artist_name]["cost"]
    last_bid = artist_cost
    for i, player in enumerate(players):
        player_budget = player['budget']
        last_bid = 0  # initialisation à 0
        if player_budget < last_bid:
            print(f"{player} ne peut pas surenchérir car il n'a plus assez d'argent.")
            continue
        while True:
            if i == 0:
                bid = input(
                    f"{player}, proposez un montant égal ou supérieur à {last_bid} (ou tapez 'passer' pour passer votre tour) : ")
                if bid == 'passer':
                    print(f"{player} passe son tour.")
                    break

                try:
                    bid = int(bid)
                    if bid < artist_cost:
                        print("Votre enchère doit être supérieure ou égale au prix initial.")
                    elif bid > player_budget:
                        print("Vous n'avez pas assez d'argent pour proposer ce montant.")
                    elif bid % 1000 != 0:
                        print("Votre enchère doit être un multiple de 1000.")
                    else:
                        last_bid = bid
                        highest_bidder = player
                        artist_cost = bid
                        print(f"{player} propose un montant de {bid}.")
                        break
                except ValueError:
                    print("Vous devez entrer un nombre entier ou 'passer'.")
            else:
                bid = input(
                    f"{player}, proposez un montant supérieur à {last_bid} (ou tapez 'passer' pour passer votre tour) : ")
                if bid == 'passer':
                    print(f"{player} passe son tour.")
                    break

                try:
                    bid = int(bid)
                    if bid <= last_bid:
                        print("Votre enchère doit être supérieure au montant précédent.")
                    elif bid > player_budget:
                        print("Vous n'avez pas assez d'argent pour proposer ce montant.")
                    elif bid % 1000 != 0:
                        print("Votre enchère doit être un multiple de 1000.")
                    else:
                        last_bid = bid
                        highest_bidder = player
                        print(f"{player} propose un montant de {bid}.")
                        break
                except ValueError:
                    print("Vous devez entrer un nombre entier ou 'passer'.")

    # Vendre la carte au joueur ayant fait la plus haute enchère
    if highest_bidder is not None:
        highest_bidder['budget'] -= last_bid
        print(f"{highest_bidder['name']} remporte la carte pour un montant de {last_bid}.")
        # ajout de la carte au dictionnaire de l'inventaire du joueur
        highest_bidder['inventory']['artists'].append(artist_name)

        removed_card.append(artist_name)
    else:
        print("La carte est retirée de la partie.")

    # Affichage des budgets restants
    for player in players:
        print(f"{player['name']} a maintenant {player['budget']} euros.")



#CODE TEMPORAIRE POUR DISPATCH LES ARTISTES DANS LES sceneS DE FACON ALEATOIRE


# Dispatch des artistes dans les scènes
for player in players:
    inventory = player['inventory']
    scenes = inventory['scenes']
    artists = inventory['artists']
    print(f"{player['name']}, voici les scènes disponibles dans votre deck :")
    for scene_name, scene in scene_card.items():
        if scene_name in scenes:
            print(f"Scène : {scene_name}")
    while artists:
        artist = artists[0]
        print(f"{player['name']}, voici les artistes disponibles dans votre deck : {artists}")
        scene_choice = input(f"Dans quelle scène voulez-vous placer {artist} ? ")
        if scene_choice in scenes:
            scene = scene_card[scene_choice]
            # Ajouter l'artiste à la scène
            scene.setdefault('Artists', []).append(artist)
            # Retirer l'artiste du deck du joueur
            inventory['artists'].remove(artist)
            artists = inventory['artists']
        else:
            print("Scène invalide, veuillez choisir une scène présente dans votre deck.")
    print("Tous les artistes ont été répartis dans les scènes.")