import json

with open("grid.json", "r") as file:
    grid = json.load(file)
    
def print_grid(grid):
    for row in grid:
        print(row)

print_grid(grid)