import time

def Bresenham(grid, x0, y0, x1, y1):
  def plot(grid, x, y, tr_xy):
    if tr_xy == -1:
      x, y = y, x
    grid[y][x] = 1

  tr_xy = 1
  sign_x, sign_y = 1, 1
  deltax, deltay = x1 - x0, y1 - y0
  
  if abs(deltax) < abs(deltay):
    tr_xy = -1
    x0, y0 = y0, x0
    x1, y1 = y1, x1
    deltax, deltay = deltay, deltax

  if deltay < 0:
    sign_y = -1
    deltay *= -1
  if deltax < 0:
    sign_x = -1
    deltax *= -1

  error = 0
  x, y = x0, y0
  for t in range(deltax + 1):
    plot(grid, x, y, tr_xy)
    x += sign_x
    error += 2 * deltay
    if error > deltax:
      y += sign_y
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
  return Bresenham(grid, x0, y0, x1, y1)

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



