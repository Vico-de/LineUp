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
                print(f"{player['name']} a obtenu 40 points pour la scène {scene_name} avec le label {label}.")

    return score
