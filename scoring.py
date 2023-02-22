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

        #Vérification qu'il y a au moins 3 hommes
        artists_man += sum([artist['genre'] for artist in scene_artists])
        artists_woman += sum([1 - artist['genre'] for artist in scene_artists])


    if artists_man >= 3 and artists_woman >= 3:
        # Ajout de 40 points au joueur
        score += values.point_genderegality
        # Affichage d'un message de réussite
        print(f"{player['name']} a obtenu {values.point_genderegality} points pour avoir favorisé la diversité des genres.")



    return score

def correctartist(player, artists, scenes):
    """
    Renvoie 20 points pour chaque artiste placé dans la bonne scène
    """
    score = 0
    # Parcours des scènes de l'inventaire du joueur
    for scene_name in player['inventory']['scenes']:
        scene = scenes[scene_name]
        scene_artist = scene["scene"]
        if "artists" not in scene:
            continue
        list_artists = scene["artists"]
        for artist in list_artists:
            artist_in_scene = artists[artist]['scene']

        # Vérification si l'artiste correspond à la scène
            if artist_in_scene == scene_artist:
                score += values.point_correctartist
                # Affichage d'un message de réussite
                print(f"{player['name']} a obtenu {values.point_correctartist} points pour avoir correctement placé {artist}.")

    return score

def genderegalityeverywhere(player, artists, scenes):
    """
    Renvoie 20 points pour chaque artiste placé dans la bonne scène
    """
    score = 0
    # Parcours des scènes de l'inventaire du joueur
    for scene_name in player['inventory']['scenes']:
        scene = scenes[scene_name]
        if "artists" not in scene:
            continue
            list_artists = scene["artists"]
            gender_artist = []
            ok = []
            for artist in list_artists:
                gender_artist.append(artists[artist]['genre'])
                ok.append(any(i in gender_artist for i in {0,1}))

            # Vérification si l'artiste correspond à la scène
            if all(ok) is True:
                score += values.point_genderegalityeverywhere
                # Affichage d'un message de réussite
                print(f"{player['name']} a obtenu {values.point_genderegalityeverywhere} points pour avoir diversifié toutes ces scènes.")

    return score

def stars_profit(player, artists, scenes):
    """
    Renvoie 5 points pour chaque scène dont le quota d'artiste est respecté (*scene<*artistes)
    """
    score = 0
    # Parcours des scènes de l'inventaire du joueur
    for scene_name in player['inventory']['scenes']:
        scene = scenes[scene_name]
        artists_stars = 0
        if "artists" not in scene:
            continue
        scene_profit = scene["stars"]

        list_artists = scene["artists"]
        for artist in list_artists:
            artists_stars += artists[artist]['stars']

        # Vérification si l'artiste correspond à la scène
        if scene_profit < artists_stars:
            score += values.point_starsprofitability
            # Affichage d'un message de réussite
            print(f"{player['name']} a obtenu {values.point_starsprofitability} points pour avoir rentabilisé {scene_name}.")

        return score







# def nom_fonction(player, artists, scenes):
#     """
#     Renvoie 20 points pour chaque artiste placé dans la bonne scène
#     """
#     score = 0
#     # Parcours des scènes de l'inventaire du joueur
#     for scene_name in player['inventory']['scenes']:
#         scene = scenes[scene_name]
#         scene_artist = scene["scene"]
#         if "artists" not in scene:
#             continue
# #CODE POUR CHECK UN TRUC
#
#
#
#
#             # Vérification si l'artiste correspond à la scène
#             if condition:
#                 score += values.point_genderegalityeverywhere
#                 # Affichage d'un message de réussite
#                 print(f"{player['name']} a obtenu {values.point_genderegalityeverywhere} points pour avoir diversifié toutes ces scènes.")
#
#         return score