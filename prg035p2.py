from prg035p1 import Grid

grid = Grid("grid.json")
grid.print()

for i in range(4):
    grid.rotate()
    print("---")
    grid.print()