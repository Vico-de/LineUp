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

                choice = input("Entrez le nom de la carte pour l'acheter ou 'passe' pour passer votre tour : ")

                while choice != "passe" and choice not in scene_card_stack:
                    choice = input("Entrez le nom de la carte pour l'acheter ou 'passe' pour passer votre tour : ")

                if choice == "passe":
                    skip.append(player['name'])
                    continue
                else:
                    card_cost = scenes[choice]['cost']

                    # Vérification si le joueur a suffisamment d'argent pour acheter la carte
                    if player['budget'] >= card_cost:
                        player['budget'] -= card_cost  # Déduction du coût de la carte du budget du joueur
                        player['inventory']['scenes'].append(
                            choice)  # Ajout de la carte achetée dans le dictionnaire du joueur
                        scene_card_stack.remove(
                            choice)  # Retrait de la carte achetée de la liste des cartes disponibles
                        print(f"{player['name']} a acheté la carte {choice} pour {card_cost} écocups.")
                        print(f"Il te reste {player['budget']} écocup !")
                    else:
                        print(f"{player['name']}, vous n'avez pas assez d'argent pour acheter cette carte.")

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
        while len(artist_card_stack) > 0:
            artist_name = artist_card_stack.pop()
            print("\nLa carte retournée est :", artist_name)
            artist_label, _, artist_stars, artist_style, artist_gender = artists[artist_name]
            print("Le coût de cette carte est :", artists[artist_name]["cost"])

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
                if 'artists' not in scene:
                    scene['artists'] = []
                if artist_name not in scene['artists']:
                    scene['artists'].append(artist_name)
    else:
        pass

    # On affiche l'inventaire mis à jour de chaque joueur
    display.display_inventory(players, scenes)


def announce_winner(players, scenes, artists):
    """
    Calcule les scores des joueurs et les affiche.
    """
    print("\nScores:")
    for player in players:
        player["score"] += scoring.full_label(player, scenes, artists)
        # player["score"] += scoring.condition1(player, scene_cards, artist_cards)
        # player["score"] += scoring.condition2(player, scene_cards, artist_cards)
        # player["score"] += scoring.condition3(player, scene_cards, artist_cards)

        print(f"\t{player['name']}: {player['score']}")

