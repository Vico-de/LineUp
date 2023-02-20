import values


def full_label(player, artists, scenes):
    """
    Renvoie les points pour un label complet sur une scène.
    """
    score = 0

    # Parcours des scènes de l'inventaire du joueur
    for scene_name in player['inventory']['scenes']:
        scene = scenes[scene_name]
        if "artists" not in scene:
            continue
        scene_artists = [artists[artist] for artist in scene["artists"]]
        scene_labels = [artist['label'] for artist in scene_artists]

        # Vérification s'il y a au moins 4 artistes avec le même label
        label_counts = {}
        for label in scene_labels:
            if label in label_counts:
                label_counts[label] += 1
            else:
                label_counts[label] = 1

        for label, count in label_counts.items():
            if count >= 4:
                # Ajout de 40 points au joueur
                score += values.point_fulllabel

                # Affichage d'un message de réussite
                print(f"{player['name']} a obtenu {values.point_fulllabel} points pour la scène {scene_name} avec le label {label}.")

    return score

def gender_equality(player, artists, scenes):
    """
    Renvoie 20 points si il y a au moins 3 femmes et 3 hommes dans les artistes d'un joueur
    """
    score = 0
    artists_man = 0
    artists_woman = 0
    # Parcours des scènes de l'inventaire du joueur
    for scene_name in player['inventory']['scenes']:
        scene = scenes[scene_name]
        if "artists" not in scene:
            continue
        scene_artists = [artists[artist] for artist in scene["artists"]]
        scene_gender = [artist['genre'] for artist in scene_artists]

        #Vérification qu'il y a au moins 3 hommes

        for man in scene_gender:
            if man == 1:
                artists_man += 1

        for woman in scene_gender:
            if woman == 0:
                artists_woman += 1


    if artists_man >= 3 and artists_woman >= 3:
        # Ajout de 40 points au joueur
        score += values.point_genderegality
        # Affichage d'un message de réussite
        print(f"{player['name']} a obtenu {values.point_genderegality} points pour avoir favorisé la diversité des genres.")


    return score

def correctartist(player, artists, scenes):
    """
    Renvoie 20 points si il y a au moins 3 femmes et 3 hommes dans les artistes d'un joueur
    """
    score = 0
    # Parcours des scènes de l'inventaire du joueur
    for scene_name in player['inventory']['scenes']:
        scene = scenes[scene_name]
        scene_artists = scene["scene"]
        if "artists" not in scene:
            continue
        artists_in_scenes = [artists[artist] for artist in scene["artists"]]
        artists_correct_scenes = [artist['scene'] for artist in artists_in_scenes]

        # Vérification si l'artiste correspond à la scène
        for correct in artists_correct_scenes:
            if correct == scene_artists:
                score += values.point_correctartist
                # Affichage d'un message de réussite
                print(f"{player['name']} a obtenu {values.point_correctartist} points pour avoir correctement placé {scenes['artist']}.")

    return score