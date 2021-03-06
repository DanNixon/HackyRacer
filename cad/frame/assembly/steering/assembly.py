import solid as sp
import solid.utils as spu

from frame.materials import tube
from frame.utils import entrypoint

from . import column_mount, instrument_panel, throttle, arm, arm_mount, wheel, wheel_mount
from .dimensions import column_diameter, column_length


def assembly():
    column = tube.volume(diameter=column_diameter, wall_thickness=2., length=column_length)

    return sp.union()(
        spu.up(column_length)(
            spu.up(wheel.plate_thickness / 2.)(
                sp.color('red')(wheel.volume()),
                spu.up(wheel.plate_thickness / 2.)(
                    sp.color('green')(instrument_panel.assembly())
                ),
                sp.translate((150, 80))(
                    sp.rotate((0., 60., 0.))(
                        sp.color('blue')(throttle.assembly())
                    )
                ),
            ),
            sp.rotate((0, 180, 0))(sp.color('cyan')(wheel_mount.volume())),
        ),
        sp.color('magenta')(column),
        spu.up(440.)(sp.color('purple')(column_mount.upper.assembly())),
        spu.up(60.)(sp.color('grey')(column_mount.lower.assembly())),
        sp.rotate((0, 0, 0))(
            sp.color('orange')(arm_mount.volume()),
            sp.color('pink')(spu.down(arm.thickness)(arm.volume())),
        ),
    )


if __name__ == '__main__':
    entrypoint.main(assembly())
