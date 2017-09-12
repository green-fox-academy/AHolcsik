l = [1, 0, 0, 0]

def create_grid(grid_height, grid_width):
    grid = []
    for i in range(grid_height):
        row_list = []
        for j in range(grid_width):
            row_list.append ("0")
        grid.append (row_list)
    return grid

def print_grid(grid):
    for row in grid:
        print(row)

print_grid(create_grid(4,4))