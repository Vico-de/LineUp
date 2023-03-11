import random

import data


def pick_event(player, events_cards):
    if len(events_cards) == 0:
        return None, None

    events_cards_stack = data.random_list(events_cards)
    pick_event_card = events_cards_stack[0]
    player['inventory']['events'].append(pick_event_card)
    del events_cards[pick_event_card]
    return player, pick_event_card


def effect(index, pick_event_card, players, scenes, cards_event_source, artists):
    player = players[index]
    player_scenes = player['inventory']['scenes']
    player_artists = player['inventory']['artists']
    card = cards_event_source[pick_event_card]

    # Bonus - Le joueur qui tire la carte gagne 10 000 écocups
    if card['effect'] == "+ 10000":
        print(card['event'])
        player['budget'] += 10000
        print(f"{player['name']} gagne 10000 écocups")

    # Bonus - Retire 3 étoiles de rentabilité à toutes les scènes "open air" du joueur qui tire cette carte
    elif card['effect'] == "club -5 stars":
        print(card['event'])
        print(f"\tToutes les boîtes de {player['name']} ont 5 étoiles de moins de rentabilité")
        for club in player_scenes:
            if scenes[club]['stars'] == 3:
                scenes[club]['stars'] += -5
            else:
                continue

    # Bonus - Tous les artistes du joueur qui a tiré la carte, gagnent 1 étoile
    elif card['effect'] == "+ 1 star artists":
        print(card['event'])
        for i in player_artists: artists[i]['stars'] += 1

    # Bonus - Retire 3 étoiles de rentabilité à toutes les scènes "open air" du joueur qui tire cette carte
    elif card['effect'] == "open air - 3 stars":
        print(card['event'])
        print(f"\tTous les open air de {player['name']} ont 3 étoiles de moins de rentabilité")
        for openair in player_scenes:
            if scenes[openair]['stars'] == 2:
                scenes[openair]['stars'] += -3
            else:
                continue

    # Bonus - Retire 3 étoiles de rentabilité à toutes les scènes "soirées" au joueur qui tire la carte
    elif card['effect'] == "event - 3 stars":
        print(card['event'])
        print(f"\nToutes les soirées de {player['name']} ont 3 étoiles de moins de rentabilité")
        for event in player_scenes:
            if scenes[event]['stars'] == 0:
                scenes[event]['stars'] += -3
            else:
                continue

    # Malus - Retires 20 000 écocups au joueur ciblé
    elif card['effect'] == "-20000":
        print(card['event'])
        for p in players: print(f"{p['name']} : {p['budget']}")
        target = players[choose(players)]
        target['budget'] += -20000
        print(f"{target['name']} perd 20000 écocups")

    # Malus - Ajoute 5 étoiles de rentabilité à toutes les scènes "open air" du joueur qui tire cette carte
    elif card['effect'] == "open air + 5 stars":
        print(card['event'])
        print(f"\tTous les open air de {player['name']} ont 5 étoiles de plus de rentabilité")
        for openair in player_scenes:
            if scenes[openair]['stars'] == 2:
                scenes[openair]['stars'] += 5
            else:
                continue

    # Malus - Retire un artiste random au joueur ciblé
    elif card['effect'] == "-1 artist":
        print(card['event'])
        target = players[choose(players)]
        n_artistes = len(target['inventory']['artists'])
        if n_artistes == 0:
            print(f"\n{target['name']} n'a pas d'artistes.")
        else:
            random_number = random.randrange(n_artistes)
            artist_pop = target['inventory']['artists'][random_number]
            print(f"\n{target['name']} a perdu {artist_pop}")
            target['inventory']['artists'].pop(random_number)


    # Malus - Ajoute 3 étoiles de rentabilité à toutes les scènes "boites"
    elif card['effect'] == "club + 3 stars":
        print(card['event'])
        print(f"\nToutes les boîtes de {player['name']} ont 3 étoiles de plus de rentabilité")
        for club in player_scenes:
            if scenes[club]['stars'] == 3:
                scenes[club]['stars'] += -5
            else:
                continue

    # Malus - Retire une étoile à tous les artistes du joueur ciblé
    elif card['effect'] == "-1 star artists":
        print(card['event'])
        target = players[choose(players)]
        target_artists = target['inventory']['artists']
        for i in target_artists:
            artists[i]['stars'] += 1

    # Malus - Ajoute 3 étoiles de rentabilité à toutes les scènes "soirées" au joueur qui tire la carte
    elif card['effect'] == "event + 3 stars":
        print(card['event'])
        target = players[choose(players)]
        print(f"\nToutes les soirées de {target['name']} ont 3 étoiles de plus de rentabilité")
        for event in scenes:
            if scenes[event] == 0:
                scenes[event]['stars'] += 3
            else:
                continue

    player['fame'] += card['fame']

    return


def choose(players: list) -> int:
    target: int = 0

    for i, player in enumerate(players):
        print(f"{str(i + 1)} - {player['name']}")

    while target < 1 or target > len(players):
        try:
            target = int(input("\nChoisissez le joueur auquel vous voulez attribuer le malus : "))
        except ValueError:
            print("Vous devez entrer un nombre entier.")

    return target - 1
