import data
import display
import events
import util
import values


def start_auction(players, artists, scenes):
    artist_card_stack = data.random_list(artists)
    events_cards = data.events()
    cards_event_source = events_cards.copy()
    player_stack = [i for i in range(len(players))]

    while len(artist_card_stack) > 0 \
            and all([len(p['inventory']['artists']) < 12 for p in players]) \
            and all([util.complete_labels(p, artists) < 2 for p in players]):
        artist_name = artist_card_stack.pop()
        print(f"\nLa carte retournée est {display.format_artist(artist_name, artists)}")
        artist_label, _, artist_stars, artist_style, artist_scene, artist_gender = artists[artist_name]
        print(f"\tLe coût de cette carte est {artists[artist_name]['cost']} écocups.")

        # Boucle pour permettre aux joueurs de surenchérir ou de passer leur tour
        highest_bidder = None
        artist_cost = artists[artist_name]["cost"]
        last_bid = artist_cost

        skip = []
        bought = False
        auction_in_progress = True

        # Le premier joueur peut acheter la carte directement
        print("")
        while True:
            player = players[player_stack[0]]
            bid = input(f"{player['name']}, tapez \"acheter\" pour obtenir"
                        f" {artist_name} pour {artist_cost} écocups, ou tapez \"passer\" pour passer votre tour : ")
            if bid in values.PASSE:
                print(f"\t{player['name']} passe son tour.")
                skip.append(player['name'])
                break
            elif bid in values.ACHAT:
                highest_bidder = player
                index = players.index(player)
                bought = True
                auction_in_progress = False
                print(f"\t{player['name']} obtient {artist_name}.")
                _, pick_event_card = events.pick_event(highest_bidder, events_cards)
                if pick_event_card is None:
                    break
                print(f"\t{player['name']} reçoit {pick_event_card}.")
                events.effect(index, pick_event_card, players, scenes, cards_event_source, artists)
                break
            else:
                print("\tSaisie invalide, veuillez réessayer.")

        auction_player_index = 0

        while auction_in_progress:
            auction_player_index += 1
            player_i = player_stack[auction_player_index % len(player_stack)]
            player = players[player_i]

            if player['name'] in skip:
                continue

            player_budget = player['budget']
            if player_budget < last_bid:
                print(f"\n{player['name']} ne peut pas acheter {artist_name} car il n'a plus assez d'écocups.")
                skip.append(player['name'])
                continue

            # Enchères
            if not bought:
                print("")
                while True:
                    bid = input(f"{player['name']}, proposez un montant supérieur à {last_bid}"
                                f" (ou tapez \"passer\" pour passer votre tour) : ")

                    if bid in values.PASSE:
                        print(f"\t{player['name']} passe son tour.")
                        skip.append(player['name'])
                    else:
                        try:
                            bid = int(bid)
                            if bid <= last_bid:
                                print("Votre enchère doit être supérieure au montant précédent.")
                            elif bid > player_budget:
                                print("Vous n'avez pas assez d'écocups pour proposer ce montant.")
                            elif bid % 1000 != 0:
                                print("Votre enchère doit être un multiple de 1000.")
                            else:
                                last_bid = bid
                                highest_bidder = player
                                print(f"\t{player['name']} propose un montant de {bid} écocups.")
                        except ValueError:
                            print("Vous devez entrer un nombre entier ou \"passer\".")

                    all_skipped = len(skip) == len(players)
                    auction_winner = len(skip) == len(players) - 1 and highest_bidder is not None
                    if all_skipped or auction_winner:
                        auction_in_progress = False
                        break

        # Vendre la carte au joueur ayant fait la plus haute enchère
        if highest_bidder is not None:
            highest_bidder['budget'] -= last_bid
            print("\n——————————————————————————————————————————————————————————————————————")
            print(f"{highest_bidder['name']} remporte {artist_name} pour un montant de {last_bid} écocups.")
            # ajout de la carte au dictionnaire de l'inventaire du joueur
            highest_bidder['inventory']['artists'].append(artist_name)
            # pioche d'une carte événement
            events.pick_event(highest_bidder, events_cards)
        else:
            del artists[artist_name]
            print("\n——————————————————————————————————————————————————————————————————————")
            print("La carte est retirée de la partie.")

        # Affichage des budgets restants
        for player in players:
            print(f"\t{player['name']} a maintenant {player['budget']} écocups.")

        print("——————————————————————————————————————————————————————————————————————")
        player_stack.append(player_stack.pop(0))

    print("La phase d'enchères est finie.")
