module BoxSection(outer, length, center, col="yellow")
{
  translate(center ? [0, 0, 0] : -[outer[0]/2, 0, outer[1]/2])
  {
    color(col)
    {
      cube([outer[0], length, outer[1]], center=center);
    }
  }
}
