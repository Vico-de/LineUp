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


TYPE_NAMES = {
    0: "Spécial",
    1: "Salles de concert",
    2: "Open air",
    3: "Discothèque",
    4: "Festival",
}


def format_type(t):
    if t in TYPE_NAMES:
        return TYPE_NAMES[t]
    else:
        return "Inconnu"


def format_scene(scene_name, scenes):
    scene = scenes[scene_name]
    type = format_type(scene['type'])
    return f"{scene['stars']}★\t {scene_name}{' ' * (21 - len(scene_name))} {type}{' ' * (20 - len(type))}{scene['cost']}"
