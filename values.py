auto = False

##### Scoring #####

# Cumulative points
point_fulllabel = 40  # Pour chaque scène qui possède les 4 artistes d'un même label
point_starsprofitability = 5  # Pour chaque scène ou le cumul des "stars" des artistes >= "stars" de la scène
point_3variousstyles = 20  # Pour chaque scène qui possède 3 artistes avec un style différent
point_correctartist = 10  # Pour chaque scène qui possède l'artiste dont "scene" = "numero scene" de la scène

# Point appliqué une seule fois pour chaque joueur dans son inventaire
point_variousscenes = 20  # Si tous les types de scène sont présentes dans le deck d'un joueur (0, 1, 2, 3 et 4 au moins une fois)
point_genderegality = 20  # Si dans tous les artistes d'un joueur, au moins 5 artistes avec "genre" = 0 et 5 artistes avec "genre" = 1
point_genderegalityeverywhere = 20  # Si toutes les scènes comportent au moins deux artistes dont le "genre" est différent
point_variousstyles = 10  # Si dans tous les artistes il y a au moins tous les "styles" présents une fois
point_allscenecorrectartist = 40  # Si toutes les scènes du joueur comportent chacune au moins un artiste avec "scene" = "numero de scène"

# Pénalités
point_penalities = -10  # Pénalité de points appliquée si tous les artistes d'un joueur est du même "genre",
                        # si une scène comporte un artiste dont le "style" = "style inadapté" de la scène
                        # si le cumul de "stars" des artistes présents sur une scène < "stars" de la scène