def complete_labels(player, artists):
    """
    Renvoie le nombre de labels complets pour le joueur 'player'.
    """
    player_artists = player['inventory']['artists']
    player_labels = [artists[artist]['label'] for artist in player_artists]
    label_counts = [player_labels.count(label) for label in set(player_labels)]
    return label_counts.count(4)
