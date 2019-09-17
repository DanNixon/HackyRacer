use <../../parts/box_section.scad>;

include <dimensions.scad>;
include <../../dimensions.scad>;

module SeatMountAssembly()
{
  difference()
  {
    width = outer * 2;

    union()
    {
      for (y = [-seat_depth/2, seat_depth/2])
      {
        translate([0, y, 0])
        {
          rotate([0, 0, 90])
          {
            BoxSection(width + box_section_outer, true, col="darkgreen");
          }
        }
      }

      for (x = [-width/2, width/2, -seat_mount_centres[0]/2, seat_mount_centres[0]/2])
      {
        translate([x, 0, 0])
        {
          BoxSection(seat_depth-25.0, true);
        }
      }

      translate([0, 0, (box_section_outer + plate_thickness) / 2])
      {
        color("grey")
        {
          cube([outer * 2 + box_section_outer, 280 + box_section_outer, plate_thickness], center=true);
        }
      }
    }

    for (x = [-seat_mount_centres[0]/2, seat_mount_centres[0]/2])
    {
      for (y = [-seat_mount_centres[1]/2, seat_mount_centres[1]/2])
      {
        translate([x, y])
        {
          cylinder(h=100, d=seat_mount_hole_diameter, center=true);
        }
      }
    }
  }
}

SeatMountAssembly();