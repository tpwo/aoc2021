from dataclasses import dataclass, field
from typing import NamedTuple

INPUT = """\
0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
"""

lines = INPUT.splitlines()

@dataclass
class Coordinates:
    x1: list[int] = field(default_factory=list)
    x2: list[int] = field(default_factory=list)
    y1: list[int] = field(default_factory=list)
    y2: list[int] = field(default_factory=list)


coords = Coordinates()


for line in lines:
    x1y1, _, x2y2 = line.partition(" -> ")
    x1, y1, x2, y2 = ",".join([x1y1, x2y2]).split(",")

    coords.x1.append(int(x1))
    coords.x2.append(int(x2))
    coords.y1.append(int(y1))
    coords.y2.append(int(y2))


print(coords)
