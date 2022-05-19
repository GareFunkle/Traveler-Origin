
from characters.NPC.Grec.Action.canwalk import CanWalk
from characters.Player.Animatesprite.animatesprite import Animate_Sprite
from lib.units.NPC.Grec.units import Units


class Grec(Units, CanWalk):
    def __init__(self, nb_points):
        Units.__init__(self, Animate_Sprite(0, 0, 'grec'),
                       current_health=100, max_health=100)
        CanWalk.__init__(self, nb_points, speed_walk=3, speed_run=5)
