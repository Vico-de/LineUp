import values


def full_label(player, scenes, artists):
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
                print(f"\t{values.point_fulllabel} pts pour la scène {scene_name} avec le label {label}.")

    return score

def gender_equality(player, scenes, artists):
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
        print(f"\t{values.point_genderegality} pts pour avoir favorisé la diversité des genres.")
    else:
        score += values.point_penalities
        print(f"\t{values.point_penalities} pts - égalité f/h")


    return score

def correctartist(player, scenes, artists):
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
                print(f"\t{values.point_correctartist} pts pour avoir correctement placé {artist}.")

    return score

def genderegalityeverywhere(player, scenes, artists):
    """
    Renvoie 20 points si chaque scène comporte au moins un homme et une femme
    """
    score = 0
    ok = []
    # Parcours des scènes de l'inventaire du joueur
    for scene_name in player['inventory']['scenes']:
        scene = scenes[scene_name]
        if "artists" not in scene:
            continue
        list_artists = scene["artists"]
        gender_artist = []

        for artist in list_artists:
            gender_artist.append(artists[artist]['genre'])
        for x in gender_artist:
            if x in [0, 1]:
                ok.append(True)
        ok.append(False)

    # Vérification si l'artiste correspond à la scène
    if all(ok) is True:
        score += values.point_genderegalityeverywhere
        # Affichage d'un message de réussite
        print(f"\t{values.point_genderegalityeverywhere} pts pour avoir diversifié toutes ces scènes.")

    return score

def stars_profit(player, scenes, artists):
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
            print(f"\t{values.point_starsprofitability} pts pour avoir rentabilisé {scene_name}.")
        else:
            score += values.point_penalities
            print(f"\t{values.point_penalities} pts - rentabilité")
    return score

#TODO check si ça marche ci-dessous
def various_scenes(player, scenes):
    """
    Renvoie 40 points si tous les types de scène sont présents dans le deck d'un joueur
    """
    score = 0
    # Parcours des scènes de l'inventaire du joueur
    list_type = []
    type = []
    for i in scenes:
        type.append(scenes[i]['type'])
    list_styles = list(set(type))

    for scene_name in player['inventory']['scenes']:
        scene = scenes[scene_name]
        scene_type = scene["type"]
        list_type.append(scene_type)


    # Vérification si l'artiste correspond à la scène
    if all(i in list_type for i in list_styles) is True:
        score += values.point_variousscenes
        # Affichage d'un message de réussite
        print(f"\t{values.point_variousscenes} pts pour avoir chaque style de scènes possible.")

    return score

def wrongstyle(player, scenes, artists):
    """
    Retire 10 points pour chaque artiste dont le style est le mauvais de la scène
    """
    score = 0
    # Parcours des scènes de l'inventaire du joueur
    for scene_name in player['inventory']['scenes']:
        scene = scenes[scene_name]
        scene_wrongstyle = scene["wrong style"]
        if "artists" not in scene:
            continue
        list_artists = scene["artists"]
        for artist in list_artists:
            artist_style = artists[artist]['style']

        # Vérification si l'artiste correspond à la scène
            if artist_style == scene_wrongstyle:
                score += values.point_penalities
                # Affichage d'un message de réussite
                print(f"\t{values.point_penalities} pts - {artist}, mauvais style.")

    return score

def allscenescorrectartist(player, scenes, artists):
    """
    Renvoie 40 points si toutes les scènes ont un artiste placé dans la bonne scène
    """
    score = 0
    allscenes = 0
    # Parcours des scènes de l'inventaire du joueur
    for scene_name in player['inventory']['scenes']:
        scene = scenes[scene_name]
        scene_artist = scene["scene"]

        if "artists" not in scene:
            return 0
        list_artists = scene["artists"]
        for artist in list_artists:
            artist_in_scene = artists[artist]['scene']
        # Vérification si l'artiste correspond à la scène
            if artist_in_scene == scene_artist:
                allscenes += 1

        if allscenes == len(player['inventory']['scenes']):
            score += values.point_allscenecorrectartist
            # Affichage d'un message de réussite
            print(f"\t{values.point_allscenecorrectartist} pts pour avoir placé au moins un bon artiste par scène.")

    return score

# TODO coder ci-dessous
def stylesdiversity(player, scenes, artists):
    """
    Renvoie 40 points si 3 styles différents sont présents dans chaque scène
    """
    score = 0

    n_styles = [len({artists[a]["style"] for a in scenes[s].get("artists", [])}) for s in player["inventory"]["scenes"]]
    if all([n >= 3 for n in n_styles]):
        score += values.point_stylesdiversity
        # Affichage d'un message de réussite
        print(f"\t{values.point_variousscenes} pts pour avoir 3 styles différents dans chaque scène.")
    return score


# TODO fix bug fame scoring
def fame_score(players):
    """
    Renvoie 40 points au joueur qui a le plus de fame (total des points des cartes évènements)
    """
    fame = {}
    score = 0
    for player in players:
        fame[player['name']] = player['fame']
    player_fame = max(fame, key=fame.get)
    if len(player_fame) > 1:
        None
    winner = next((win for win in players if win['name'] == player_fame), None)
    score += values.point_fame
    print(f"Le bonus de réputation est attribué à {winner['name']}")

    return score, winner

# def nom_fonction(player, scenes, artists):
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