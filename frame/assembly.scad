use <parts/box_section.scad>;
use <parts/motor.scad>
use <parts/wheel.scad>;
use <subassemblies/rear_axle.scad>;
use <subassemblies/seat_mount.scad>;

translate([0, 0, 25])
{
  RearAxle(16, 600, -180, 180);
}

translate([-130, 120, 75])
{
  Motor();
}

/* Front wheel */
translate([0, 900, 0])
{
  Wheel();
}

outer = 210;
inner = 120;

translate([0, -180, 0])
{
  outer_length = 500;
  inner_length = 800;

  for (x = [-outer, outer])
  {
    translate([x, 0, 0])
    {
      BoxSection(500, false);
    }
  }

  for (x = [-inner, inner])
  {
    translate([x, 0, 0])
    {
      BoxSection(inner_length, false);
    }
  }

  translate([0, inner_length + 12.5, 0])
  {
    rotate([0, 0, 90])
    {
      BoxSection(inner * 2 + 25, true, col="darkgreen");
    }
  }

  translate([0, outer_length + 12.5, 0])
  {
    rotate([0, 0, 90])
    {
      BoxSection(inner * 2 - 25, true, col="darkgreen");

      for (a = [0, 180])
      {
        rotate([0, 0, a])
        {
          translate([0, -outer - 12.5, 0])
          {
            BoxSection(outer - inner, false, col="lime");
          }
        }
      }
    }
  }

  translate([0, -12.5, 0])
  {
    rotate([0, 0, 90])
    {
      BoxSection(outer * 2 + 25, true, col="darkgreen");
    }
  }
}

/* Floor panel */
translate([0, 220, -(25 + 3) / 2])
{
  color("grey")
  {
    cube([inner * 2 + 25, 820 + 25, 3], center=true);
  }
}

translate([0, 0, 150])
{
  SeatMount(outer*2, 280);

  /* Seat mount panel */
  translate([0, 0, (25 + 3) / 2])
  {
    color("grey")
    {
      cube([outer * 2 + 25, 280 + 25, 3], center=true);
    }
  }
}
