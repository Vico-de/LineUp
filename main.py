import game

import data

artist_cards = data.artists()
scene_cards = data.scenes()

players = game.init()

game.scene_choice(players, scene_cards)

game.artist_auction(players, artist_cards)

game.dispatch_artists(players, scene_cards)

game.announce_winner(players, artist_cards, scene_cards)
