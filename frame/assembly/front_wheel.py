import solid as sp
import solid.utils as spu

from frame.assembly import axle_diameter
from frame.parts.wheel import wheel

magic_1 = 30
magic_2 = 25
magic_3 = 20
magic_4 = 40


def assembly():
    return sp.union()(
        sp.color(spu.Red)(spu.right(100)(wheel())),
        sp.color(spu.Green)(
            sp.hull()(
                sp.cylinder(h=magic_1, r=magic_2, center=True),
                spu.right(magic_4)(
                    sp.cylinder(h=magic_1, r=magic_3, center=True)
                )
            )
        ),
        sp.color(spu.Blue)(
            sp.rotate([0, 90, 0])(sp.cylinder(d=axle_diameter, h=160))
        ),
    )


if __name__ == '__main__':
    print(sp.scad_render(assembly()))