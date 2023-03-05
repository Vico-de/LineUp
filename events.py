import data


# TODO regarder comment gérer/import events_cards
def pick_event(player, events_cards):
    events_cards_stack = data.random_list(events_cards)
    pick_event_card = events_cards_stack[0]
    player['inventory']['events'].append(pick_event_card)
    del events_cards[pick_event_card]
    return player, pick_event_card


def effect(player, pick_event_card, players, events_card, scenes):
    player_scenes = player['inventory']['scenes']
    artists = player['inventory']['artists']
    target = player
    card = events_card[pick_event_card]

    # Bonus - Le joueur qui tire la carte gagne 10 000 écocups
    if card['effect'] == "+ 10000":
        print(card['event'])
        player['budget'] += 10000
        print(f"{player['name']} gagne 10000 écocups")

    # Bonus - Retire 3 étoiles de rentabilité à toutes les scènes "open air" du joueur qui tire cette carte
    elif card['effect'] == "club -5 stars":
        print(card['event'])
        print(f"\tToutes les boîtes de {target['name']} ont 5 étoiles de moins de rentabilité")
        for club in player_scenes:
            if scenes[club]['stars'] == 3:
                scenes[club]['stars'] += -5
            else:
                continue

    # Bonus - Tous les artistes du joueur qui a tiré la carte, gagnent 1 étoiles
    elif card['effect'] == "+ 1 star artists":
        print(card['event'])
        for i in artists: artists[i]['stars'] += -1

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
        choose(target)
        target['budget'] += -20000
        print(f"{player['name']} perd 20000 écocups")

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
        choose(target)
        artists_target = target['inventory']['artists']
        data.random_list(artists_target)
        print(f"\n{target['name']} a perdu {artists_target[0]}")
        artists_target.pop(0)

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
        choose(target)
        artists_target = target['inventory']['artists']
        for i in artists_target: artists_target[i]['stars'] += -1

    # Malus - Ajoute 3 étoiles de rentabilité à toutes les scènes "soirées" au joueur qui tire la carte
    elif card['effect'] == "event + 3 stars":
        print(card['event'])
        choose(players)
        print(f"\nToutes les soirées de {choose['name']} ont 3 étoiles de plus de rentabilité")
        for event in scenes:
            if scenes[event] == 0:
                scenes[event]['stars'] += 3
            else:
                continue

    player['fame'] += card['fame']

    return player


def choose(players):
    target = ""
    print(players)
    while target not in players['name']:
        target = input("\nChoisissez le joueur auquel vous voulez attribuer le malus : ")
    return target
