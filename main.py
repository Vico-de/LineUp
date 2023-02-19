import random

import scoring

import data

artist_cards = data.artists()
scene_cards = data.scenes()

# Définition du nombre de joueurs, de leur budget et de leur dictionnaire
num_players = int(input("Entrez le nombre de joueurs : "))
players = []
for i in range(num_players):
    player_dict = {'name': f"Joueur {i + 1}", 'budget': 1000000, 'choice': "ok", 'score': 0,
                   'inventory': {'artists': [], 'scenes': []}}
    players.append(player_dict)

# CODE TEMPORAIRE POUR TEST PLUS RAPIDEMENT
artist_card_stack = list(artist_cards.keys())
scene_card_stack = list(scene_cards.keys())

# Mélanger les cartes artistes et les répartir entre les joueurs
random.shuffle(artist_card_stack)
for i in range(len(artist_card_stack)):
    player = players[i % num_players]
    player['inventory']['artists'].append(artist_card_stack[i])

# Mélanger les cartes scènes et les répartir entre les joueurs
random.shuffle(scene_card_stack)
for i in range(len(scene_card_stack)):
    player = players[i % num_players]
    player['inventory']['scenes'].append(scene_card_stack[i])


def display_inventory(players, scenes):
    for player in players:
        print(f"\nInventaire de {player['name']} :")
        for scene in player['inventory']['scenes']:
            if 'artists' in scenes[scene]:
                print(f"\t{scene} -> {scenes[scene]['artists']}")
            else:
                print(f"\t{scene} -> Aucun artiste")


# CODE TEMPORAIRE POUR DISPATCH LES ARTISTES
def assign_artists_to_scenes(players, scenes):
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

    # On affiche l'inventaire mis à jour de chaque joueur
    display_inventory(players, scenes)


assign_artists_to_scenes(players, scene_cards)

# ICI VIENS TEMP

for player in players:
    player["score"] += scoring.full_label(player, scene_cards, artist_cards)
    # player["score"] += scoring.condition1(player, scene_cards, artist_cards)
    # player["score"] += scoring.condition2(player, scene_cards, artist_cards)
    # player["score"] += scoring.condition3(player, scene_cards, artist_cards)

    print(player["score"])
