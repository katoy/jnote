import time

def delta_line(grid, x0, y0, x1, y1):
  def plot(grid, x, y):
    grid[int(y)][int(x)] = 1

  deltax, deltay = x1 - x0, y1 - y0
  longer = max(abs(deltax), abs(deltay))
  if longer == 0:
    longer = 1

  x, y = x0 + 1 / 2, y0 + 1 / 2
  dx, dy = deltax / longer, deltay / longer
  for t in range(longer + 1):
    plot(grid, x, y)
    x, y  = x + dx, y + dy
  return grid

def clear_grid(grid):
    for line in grid:
      for x in range(len(line)):
        line[x]  = 0

def print_grid(grid):
  for y in range(4, -1, -1):
    for x in range(5):
      dot = "・"
      if grid[y][x] == 1:
        dot = "口"
      print(dot, end="")
    print()
  print()

def draw_line(grid, x0, y0, x1, y1):
  return delta_line(grid, x0, y0, x1, y1)

grid = [
  [0, 0, 0 ,0 ,0],
  [0, 0, 0 ,0 ,0],
  [0, 0, 0 ,0 ,0],
  [0, 0, 0 ,0 ,0],
  [0, 0, 0 ,0 ,0],
]

# area 1
for h in range(0, 5):
  clear_grid(grid)
  draw_line(grid, 0, 0, 4, h)
  print_grid(grid)
for h in range(4, -1, -1):
  clear_grid(grid)
  draw_line(grid, 0, 0, h, 4)
  print_grid(grid)

# area 2
for h in range(4, -1, -1):
  clear_grid(grid)
  draw_line(grid, 4, 0, h, 4)
  print_grid(grid)
for h in range(4, -1, -1):
  clear_grid(grid)
  draw_line(grid, 4, 0, 0, h)
  print_grid(grid)

# area 3
for h in range(4, -1, -1):
  clear_grid(grid)
  draw_line(grid, 4, 4, 0, h)
  print_grid(grid)
for h in range(0, 5):
  clear_grid(grid)
  draw_line(grid, 4, 4, h, 0)
  print_grid(grid)

# area 4
for h in range(5):
  clear_grid(grid)
  draw_line(grid, 0, 4, h, 0)
  print_grid(grid)
for h in range(5):
  clear_grid(grid)
  draw_line(grid, 0, 4, 4, h)
  print_grid(grid)



