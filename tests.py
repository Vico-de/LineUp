import random
import unittest

import data
import events
import scoring
import values


class Tests(unittest.TestCase):

    def test_scoring(self):
        scenes = data.scenes()
        artists = data.artists()

        label_artists = [a for a in artists if artists[a]['label'] == "Club Azur"]
        scene = "Tunnel of Love"

        player = {
            'name': "Testeur",
            'budget': 1000000,
            'choice': "ok",
            'score': 0,
            'inventory': {
                'artists': label_artists,
                'scenes': [scene]
            }
        }

        scenes[scene]["artists"] = label_artists

        self.assertEqual(
            scoring.full_label(player, scenes, artists),
            values.point_fulllabel,
            "Points non attribués pour un label complet."
        )

    def test_malus(self):
        scenes = data.scenes()
        artists = data.artists()

        player = {
            'name': "Testeur",
            'budget': 1000000,
            'choice': "ok",
            'score': 0,
            'inventory': {
                'artists': artists,
                'scenes': [scenes]
            }
        }

        events.choose()
        random_number = random.randrange(len(target['inventory']['artist']))
        artist_pop = target['inventory']['artists'][random_number]
        print(f"\n{target['name']} a perdu {artist_pop}")
        target['inventory']['artists'].pop(random_number)
