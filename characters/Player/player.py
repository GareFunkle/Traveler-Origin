from characters.Player.Action.projectil import Projectile
from characters.Player.Animatesprite.animatesprite import Animate_Sprite
from characters.Player.Action.canwalk import CanWalk
from lib.units.unit import Unit
from characters.Player.Action.canjump import CanJump
from characters.Player.Action.canattack import CanAttack


class Player(Unit, CanWalk, CanJump, CanAttack, Projectile):
    def __init__(self):
        Unit.__init__(self, Animate_Sprite(0, 0, 'PLAYER'),
                      current_health=100, max_health=100)

        CanWalk.__init__(self, speed_walk=3, speed_run=5)
        CanJump.__init__(
            self,
            self.rect,
            jump=0,
            jump_high=0,
            jump_down=5,
            number_jump=0,
            to_jump=False,
        )
        CanAttack.__init__(self, attack_damage=3)
        Projectile.__init__(self, velocity=3)
