import auction
import data
import display
import scoring
import values
import random


def init():
    """
    Définition du nombre de joueurs, de leur budget et de leur dictionnaire.
    :return: La liste des joueurs
    """
    num_players = int(input("Entrez le nombre de joueurs : "))
    num_ordi = int(input("Entrez le nombre d'ordi : "))
    players = []

    for i in range(num_players + num_ordi):
        player_dict = {
            'name': f"Joueur {i + 1}",
            'budget': 1000000,
            'score': 0,
            'ordi': num_ordi > i,
            'inventory': {
                'artists': [],
                'scenes': []
            }
        }
        players.append(player_dict)

    return players


def scene_choice(players, scenes):
    """
    Répartit les scenes entre les joueurs.
    """
    if values.auto:
        # Liste des noms des scènes aléatoires
        scene_card_stack = data.random_list(scenes)

        # Répartir les scènes entre les joueurs
        for i in range(len(scenes)):
            player = players[i % len(players)]
            player['inventory']['scenes'].append(scene_card_stack[i])
    else:
        # Liste des cartes scènes disponibles
        scene_card_stack = list(scenes.keys())

        # Liste des joueurs qui ont passé
        skip = []

        # Boucle pour l'achat des cartes scènes
        while scene_card_stack:
            for player in players:
                if player['name'] in skip:
                    continue

                print(f"\n{player['name']} (budget : {player['budget']}) :")
                print("\tScènes disponibles :")
                for scene in scene_card_stack:
                    print(f"\t{display.format_scene(scene, scenes)}")

                while True:
                    choice = input("Entrez le nom de la carte pour l'acheter ou \"passer\" pour passer votre tour : ")

                    if choice not in values.PASSE and choice not in scene_card_stack:
                        print("\tSaisie invalide, veuillez réessayer.")
                    elif choice in values.PASSE:
                        if len(player['inventory']['scenes']) > 0:
                            skip.append(player['name'])
                            break
                        else:
                            print("\tVous devez acheter au moins une scène.")
                    elif player['budget'] < scenes[choice]['cost']:
                        print("\tPas assez d'écocups, veuillez réessayer.")
                    else:
                        break

                if player['name'] in skip:
                    continue

                # Déduction du coût de la carte du budget du joueur
                player['budget'] -= scenes[choice]['cost']
                # Ajout de la carte achetée dans le dictionnaire du joueur
                player['inventory']['scenes'].append(choice)

                # Retrait de la carte achetée de la liste des cartes disponibles
                scene_card_stack.remove(choice)
                print(f"\n\t{player['name']} a acheté la carte {choice} pour {scenes[choice]['cost']} écocups.")
                print(f"\tIl te reste {player['budget']} écocups !")

            # Fin de la boucle de choix
            if len(skip) == len(players):
                break


def artist_auction(players, artists):
    """
    Répartit les artistes entre les joueurs.
    """

    # Retirer 20% des cartes aléatoirement
    num_to_remove = round(0.2 * len(artists.keys()))
    removed_random = random.sample(artists.keys(), num_to_remove)
    for artist in removed_random:
        del artists[artist]

    artist_card_stack = data.random_list(artists)

    if values.auto:
        # Répartir entre les joueurs
        for i in range(len(artist_card_stack)):
            player = players[i % len(players)]
            player['inventory']['artists'].append(artist_card_stack[i])
    else:
        auction.start_auction(players, artists)

    display.display_artists(players)


def dispatch_artists(players, scenes):
    """
    Répartit les artistes entre les scènes.
    """
    if values.auto:
        for player in players:
            # Pour chaque joueur, on itère sur tous les artistes qu'il possède
            for artist_name in player['inventory']['artists']:
                # On choisit une scène aléatoire dans la liste des scènes du joueur
                scene_name = random.choice(player['inventory']['scenes'])
                # On récupère le dictionnaire de la scène
                scene = scenes[scene_name]
                # On ajoute l'artiste à la liste des artistes de la scène
                scene.setdefault('artists', []).append(artist_name)
    else:
        # Dispatch des artistes dans les scènes
        for player in players:
            inventory = player['inventory']
            print(f"\n{player['name']}, voici les scènes disponibles dans votre deck :")
            for scene in inventory['scenes']:
                print(f"\t{scene}")
            while inventory['artists']:
                print(f"Voici les artistes disponibles dans votre deck : {inventory['artists']}.")
                artist = inventory['artists'][0]
                while True:
                    scene_choice = input(f"Dans quelle scène voulez-vous placer {artist} ? ")
                    if scene_choice in inventory['scenes']:
                        scene = scenes[scene_choice]
                        # Ajouter l'artiste à la scène
                        scene.setdefault('artists', []).append(artist)
                        # Retirer l'artiste du deck du joueur
                        inventory['artists'].remove(artist)
                        break
                    else:
                        print("\tScène invalide, veuillez choisir une scène présente dans votre deck.")
            print("\nTous les artistes ont été répartis dans vos scènes.")

    # On affiche l'inventaire mis à jour de chaque joueur
    display.display_inventory(players, scenes)



def announce_winner(players, scenes, artists):
    """
    Calcule les scores des joueurs et les affiche.
    """
    print("\nScores:")
    for player in players:
        player["score"] += scoring.full_label(player, scenes, artists)
        player["score"] += scoring.gender_equality(player, scenes, artists)
        player["score"] += scoring.correctartist(player, scenes, artists)
        player["score"] += scoring.genderegalityeverywhere(player, scenes, artists)
        # player["score"] += scoring.condition3(player, scenes, artists)
        # player["score"] += scoring.condition3(player, scenes, artists)
        # player["score"] += scoring.condition3(player, scenes, artists)
        # player["score"] += scoring.condition3(player, scenes, artists)


        print(f"\t{player['name']}: {player['score']}")


