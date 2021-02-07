import time

def Bresenham(grid, x0, y0, x1, y1, tr_x, tr_xy):
    def plot(grid, x, y, tr_x, tr_xy):
        if tr_x == -1:
          x = 4 - x
        if tr_xy == -1:
          x, y = y, x
        grid[y][x] = 1

    deltax, deltay = x1 - x0, y1 - y0
    error = 0
    y = y0
    for x in range(x0, x1 + 1):
        plot(grid, x, y, tr_x, tr_xy)
        error += 2 * deltay
        if error > deltax:
            y += 1
            error -= 2 * deltax
    return grid

def clear_grid(grid):
    for line in grid:
      for x in range(len(line)):
        line[x]  = 0

def print_grid(grid):
  for y in range(4, -1, -1):
    for x in range(5):
      dot = "."
      if grid[y][x] == 1:
        dot = "*"
      print(dot, end="")
    print()
  print()

def draw_line(grid, x0, y0, x1, y1):
  deltax, deltay = x1 - x0, y1 - y0
  tr_xy = 1
  tr_x = 1

  if deltax < 0:
    x0, x1 = x1, x0
    y0, y1 = y1, y0
    deltax, deltay = -deltax, -deltay

  if deltay < 0:
    tr_x = -1
    x0, x1 = x1, x0
    deltax *= -1
    if (deltax < 0) or (deltax == 0 and deltay < 0):
      x0, x1 = x1, x0
      y0, y1 = y1, y0
      deltax, deltay = -deltax, -deltay

  if deltax < deltay:
    tr_xy = -1
    x0, y0 = y0, x0
    x1, y1 = y1, x1
    deltax, deltay = deltay, deltax

  return Bresenham(grid, x0, y0, x1, y1, tr_x, tr_xy)

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
  time.sleep(1)
for h in range(4, -1, -1):
  clear_grid(grid)
  draw_line(grid, 0, 0, h, 4)
  print_grid(grid)
  time.sleep(1)

# area 2
for h in range(4, -1, -1):
  clear_grid(grid)
  draw_line(grid, 0, 4, 4, h)
  print_grid(grid)
  time.sleep(1)
for h in range(4, -1, -1):
  clear_grid(grid)
  draw_line(grid, 0, 4, h, 0)
  print_grid(grid)
  time.sleep(1)

# area 3
for h in range(4, -1, -1):
  clear_grid(grid)
  draw_line(grid, 4, 4, 0, h)
  print_grid(grid)
  time.sleep(1)
for h in range(0, 5):
  clear_grid(grid)
  draw_line(grid, 4, 4, h, 0)
  print_grid(grid)
  time.sleep(1)

# area 4
for h in range(0, 5):
  clear_grid(grid)
  draw_line(grid, 4, 0, 0, h)
  print_grid(grid)
  time.sleep(1)
for h in range(0, 5):
  clear_grid(grid)
  draw_line(grid, 4, 0, h, 4)
  print_grid(grid)
  time.sleep(1)
