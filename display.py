def display_inventory(players, scenes):
    for player in players:
        print(f"\nInventaire de {player['name']} :")
        for scene in player['inventory']['scenes']:
            if 'artists' in scenes[scene]:
                print(f"\t{scene} -> {scenes[scene]['artists']}")
            else:
                print(f"\t{scene} -> Aucun artiste")


def display_artists(players):
    for player in players:
        print(f"\nArtistes de {player['name']} :")
        print(f"\t{player['inventory']['artists']}")
