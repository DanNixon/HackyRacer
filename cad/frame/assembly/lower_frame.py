import solid as sp
import solid.utils as spu

from frame.materials import box_section, plate
from frame.utils import entrypoint

from .dimensions import outer, outer_length, inner, inner_length, rear_axle_position
from . import rear_axle_bearing, front_axle


def assembly():
    outer_bars = sp.rotate([-90, 0, 0])(
        [
            spu.left(d)(
                box_section.volume(
                    length=outer_length, center=False, color='red'
                )
            ) for d in [-outer, outer]
        ]
    )

    inner_bars = sp.rotate([-90, 0, 0])(
        [
            spu.left(d)(
                box_section.volume(
                    length=inner_length, center=False, color='green'
                )
            ) for d in [-inner, inner]
        ]
    )

    front_bumper = spu.forward(
        inner_length + (box_section.default_size[0] / 2.)
    )(
        sp.rotate([0, 90, 0])(
            box_section.volume(
                length=inner * 2. + box_section.default_size[0],
                center=True,
                color='blue'
            )
        )
    )

    mid_bars = spu.forward(outer_length + box_section.default_size[0] / 2.)(
        sp.rotate([0, 90, 0])(
            box_section.volume(
                length=inner * 2. - box_section.default_size[0],
                center=True,
                color='cyan'
            ),
            [
                sp.rotate([0, a, 0])(
                    spu.up(inner + box_section.default_size[0] / 2.)(
                        box_section.volume(
                            length=outer - inner, center=False, color='cyan'
                        )
                    )
                ) for a in [0, 180]
            ],
        ),
    )

    rear_bar = spu.back(box_section.default_size[0] / 2.)(
        sp.rotate([0, 90, 0])(
            box_section.volume(
                length=outer * 2. + box_section.default_size[0],
                center=True,
                color='magenta'
            )
        )
    )

    bearings = spu.forward(rear_axle_position)(
        sp.rotate([180, 0, 0])(
            [
                sp.translate([x, 0, box_section.default_size[0] / 2.])(
                    sp.color('orange')(rear_axle_bearing.volume())
                ) for x in [-outer, outer]
            ]
        )
    )

    front_axle_and_wheels = sp.color('gray')(
        sp.translate((0, 1150, -box_section.default_size[0]))(
            front_axle.assembly()
        )
    )

    return sp.union()(
        outer_bars,
        inner_bars,
        front_bumper,
        mid_bars,
        rear_bar,
        bearings,
        front_axle_and_wheels,
    )


if __name__ == '__main__':
    entrypoint.main(assembly())
