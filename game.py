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
    players = []

    for i in range(num_players):
        # TODO: Ajouter un champ pour dire si le joueur est un ordi
        player_dict = {
            'name': f"Joueur {i + 1}",
            'budget': 1000000,
            'choice': "ok",
            'score': 0,
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
        # Liste des noms des scènes disponibles
        scene_card_stack = list(scenes.keys())

        # Mélanger les cartes scènes
        random.shuffle(scene_card_stack)

        # Répartir les scènes entre les joueurs
        for i in range(len(scenes)):
            player = players[i % len(players)]
            player['inventory']['scenes'].append(scene_card_stack[i])
    else:
        # TODO: Sélection manuelle des scènes
        pass


def artist_auction(players, artists):
    """
    Répartit les artistes entre les joueurs.
    """
    if values.auto:
        # Liste des noms des artistes
        artist_card_stack = list(artists.keys())

        # Mélanger les cartes artistes
        random.shuffle(artist_card_stack)

        # Répartir entre les joueurs
        for i in range(len(artist_card_stack)):
            player = players[i % len(players)]
            player['inventory']['artists'].append(artist_card_stack[i])
        pass
    else:
        # TODO: Sélection manuelle des artistes
        pass

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

