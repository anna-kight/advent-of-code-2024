def read_file(file_name):
  f = open(file_name, "r")
  puzzle = []
  for x in f:
    puzzle.append(x)
  f.close()
  return puzzle

 
def going_up(puzzle, start_loc, word):
  if start_loc[0] < 3:
    return False
  else:
    for i, c in enumerate(word):
      if c != puzzle[start_loc[0]-i][start_loc[1]]:
        return False 
  return True

def going_down(puzzle, start_loc, word):
  if start_loc[0] > len(puzzle) - 4:
    return False
  else:
    for i, c in enumerate(word):
      if c != puzzle[start_loc[0] + i][start_loc[1]]:
        return False
  return True

def going_left(puzzle, start_loc, word):
  if start_loc[1] < 3:
    return False
  else:
    for i, c in enumerate(word):
      if c != puzzle[start_loc[0]][start_loc[1] - i]:
        return False
  return True


def going_right(puzzle, start_loc, word):
  if start_loc[1] > len(puzzle[0]) - 4:
    return False
  else:
    for i, c in enumerate(word):
      if c != puzzle[start_loc[0]][start_loc[1]+i]:
        return False
  return True

#---------diagonals------------
def going_up_right(puzzle, start_loc, word):
  if start_loc[0] < 3 or start_loc[1] > len(puzzle[0]) - 4:
    return False
  else:
    for i, c in enumerate(word):
      if c != puzzle[start_loc[0] - i][start_loc[1] + i]:
        return False
  return True

def going_down_right(puzzle, start_loc, word):
  if start_loc[0] > len(puzzle) - 4 or start_loc[1] > len(puzzle[0]) - 4:
    return False
  else:
    for i, c in enumerate(word):
      if c != puzzle[start_loc[0] + i][start_loc[1] + i]:
        return False
  return True
  
def going_up_left(puzzle, start_loc, word):
  if start_loc[0] < 3 or start_loc[1] < 3:
    return False
  else:
    for i, c in enumerate(word):
      if c != puzzle[start_loc[0] - i][start_loc[1] - i]:
        return False
  return True

def going_down_left(puzzle, start_loc, word):
  if start_loc[0] > len(puzzle) - 4 or start_loc[1] < 3:
    return False
  else:
    for i, c in enumerate(word):
      if c != puzzle[start_loc[0] + i][start_loc[1] - i]:
        return False
  return True
  
def find_x_in_row(row, row_ind):
  return [(row_ind, i) for i, x in enumerate(row) if x == "X"]

puzzle = read_file("/home/anna/code/advent-of-code-2024/day4/input.txt")
puzzle = [row.strip() for row in puzzle] # puzzle[row][col]
x_locations_by_row = [find_x_in_row(row, row_ind) for row_ind, row in enumerate(puzzle)]

x_locations = [loc for i in x_locations_by_row for loc in i]

xmas = "XMAS"
is_going_up = len(list(filter(None,[going_up(puzzle, loc, xmas) for loc in x_locations])))
is_going_down = len(list(filter(None,[going_down(puzzle, loc, xmas) for loc in x_locations])))
is_going_left = len(list(filter(None,[going_left(puzzle, loc, xmas) for loc in x_locations])))
is_going_right = len(list(filter(None,[going_right(puzzle, loc, xmas) for loc in x_locations])))


is_going_up_right = len(list(filter(None,[going_up_right(puzzle, loc, xmas) for loc in x_locations])))
is_going_up_left = len(list(filter(None,[going_up_left(puzzle, loc, xmas) for loc in x_locations])))
is_going_down_right = len(list(filter(None,[going_down_right(puzzle, loc, xmas) for loc in x_locations])))
is_going_down_left = len(list(filter(None,[going_down_left(puzzle, loc, xmas) for loc in x_locations])))

xmas_count = is_going_up + is_going_down + is_going_left  + is_going_right + is_going_up_right + is_going_up_left + is_going_down_right + is_going_down_left 

print("XMAS count: " + str(xmas_count))
