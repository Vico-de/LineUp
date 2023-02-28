import data


# TODO regarder comment gérer/import events_cards
def pick_event(player, events_cards, players):
    events_cards_stack = data.random_list(events_cards)
    effect(player, events_cards, players)
    player['inventory']['events'].append(events_cards_stack[0])
    events_cards_stack.pop(0)
    return player


def effect(player, events_cards, players):
    scenes = player['inventory']['scenes']
    artists = player['inventory']['artists']
    target = player

    # Bonus - Le joueur qui tire la carte gagne 10 000 écocups
    if events_cards['effect'] == "+ 10000":
        print(events_cards['events'])
        player['budget'] += 10000
        print(f"{player['name']} gagne 10000 écocups")

    # Bonus - Retire 3 étoiles de rentabilité à toutes les scènes "open air" du joueur qui tire cette carte
    elif events_cards['effect'] == "club -5 stars":
        print(events_cards['events'])
        print(f"\tToutes les boîtes de {target['name']} ont 5 étoiles de moins de rentabilité")
        for club in scenes:
            if scenes[club] == 3:
                scenes[club]['stars'] += -5
            else:
                continue

    # Bonus - Tous les artistes du joueur qui a tiré la carte, gagnent 1 étoiles
    elif events_cards['effect'] == "+ 1 star artists":
        print(events_cards['events'])
        for i in artists: artists[i]['stars'] += -1

    # Bonus - Retire 3 étoiles de rentabilité à toutes les scènes "open air" du joueur qui tire cette carte
    elif events_cards['effect'] == "open air - 3 stars":
        print(events_cards['events'])
        print(f"\tTous les open air de {player['name']} ont 3 étoiles de moins de rentabilité")
        for openair in scenes:
            if scenes[openair] == 2:
                scenes[openair]['stars'] += -3
            else:
                continue

    # Bonus - Retire 3 étoiles de rentabilité à toutes les scènes "soirées" au joueur qui tire la carte
    elif events_cards['effect'] == "event - 3 stars":
        print(events_cards['events'])
        print(f"\nToutes les soirées de {player['name']} ont 3 étoiles de moins de rentabilité")
        for event in scenes:
            if scenes[event] == 0:
                scenes[event]['stars'] += -3
            else:
                continue

    # Malus - Retires 20 000 écocups au joueur ciblé
    elif events_cards['effect'] == "-20000":
        print(events_cards['events'])
        for i in players: print(f"{players[i]['name']} : {players[i]['budget']}")
        choose(target)
        target['budget'] += -20000
        print(f"{player['name']} perd 20000 écocups")

    # Malus - Ajoute 5 étoiles de rentabilité à toutes les scènes "open air" du joueur qui tire cette carte
    elif events_cards['effect'] == "open air + 5 stars":
        print(events_cards['events'])
        print(f"\tTous les open air de {player['name']} ont 5 étoiles de plus de rentabilité")
        for openair in scenes:
            if scenes[openair] == 2:
                scenes[openair]['stars'] += 5
            else:
                continue

    # Malus - Retire un artiste random au joueur ciblé
    elif events_cards['effect'] == "-1 artist":
        print(events_cards['events'])
        choose(target)
        artists_target = target['inventory']['artists']
        data.random_list(artists_target)
        print(f"\n{target['name']} a perdu {artists_target[0]}")
        artists_target.pop(0)

    # Malus - Ajoute 3 étoiles de rentabilité à toutes les scènes "boites"
    elif events_cards['effect'] == "club + 3 stars":
        print(events_cards['events'])
        print(f"\nToutes les boîtes de {player['name']} ont 3 étoiles de plus de rentabilité")
        for club in scenes:
            if scenes[club] == 3:
                scenes[club]['stars'] += -5
            else:
                continue

    # Malus - Retire une étoile à tous les artistes du joueur ciblé
    elif events_cards['effect'] == "-1 star artists":
        print(events_cards['events'])
        choose(target)
        artists_target = target['inventory']['artists']
        for i in artists_target: artists_target[i]['stars'] += -1

    # Malus - Ajoute 3 étoiles de rentabilité à toutes les scènes "soirées" au joueur qui tire la carte
    elif events_cards['effect'] == "event + 3 stars":
        print(events_cards['events'])
        choose(players)
        print(f"\nToutes les soirées de {choose['name']} ont 3 étoiles de plus de rentabilité")
        for event in scenes:
            if scenes[event] == 0:
                scenes[event]['stars'] += 3
            else:
                continue

    player['fame'] += events_cards['fame']

    return player


def choose(players):
    target = 0
    print(players)
    while target not in players['name']:
        target = input("\nChoisissez le joueur auquel vous voulez attribuer le malus : ")
    return target
