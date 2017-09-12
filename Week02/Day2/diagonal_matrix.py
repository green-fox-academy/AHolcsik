# - Create (dynamically) a two dimensional list
#   with the following matrix. Use a loop!
#
#   1 0 0 0
#   0 1 0 0
#   0 0 1 0
#   0 0 0 1
#
# - Print this two dimensional list to the output

l = [1, 0, 0, 0]

def create_grid(grid_height, grid_width):
    grid = []
    for i in range(grid_height):
        row_list = []
        for j in range(grid_width):
            if j == i:
                row_list.append("1")
            else:    
                row_list.append ("0")
        grid.append (row_list)
    return grid

def print_grid(grid):
    for row in grid:
        print(row)

print_grid(create_grid(4,4))






