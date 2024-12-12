def read_file(file_name):
  f = open(file_name, "r")
  map = []
  for x in f:
    map.append(x.strip())
  f.close()
  return map

def find_guard_in_row(row, row_ind):
  return [(row_ind, i) for i, x in enumerate(row) if x == "^"]

def move_up(current):
  return (current[0] - 1, current[1])

def move_down(current):
    return (current[0] + 1, current[1])

def move_right(current):
    return (current[0], current[1] + 1)

def move_left(current):
    return (current[0], current[1] - 1)

def next(direction, current):
   move_in_direction = {"^": move_up, "v": move_down, ">": move_right, "<": move_left}
   return move_in_direction[direction](current)

def is_obstacle(position):
   return map[position[0]][position[1]] == "#"

def rotate(direction):
   rotated_direction = {"^": ">", "v": "<", ">": "v", "<": "^"}
   return rotated_direction[direction]

def is_edge(position):
   return position[0]<0 or position[0] > len(map)-1 or position[1]<0 or position[1] > len(map[0])-1 

def mark_as_visited(position, map):
   map[position[0]] = map[position[0]][:position[1]] + 'X' + map[position[0]][position[1] + 1:]
   return map

map = read_file("/home/anna/code/advent-of-code-2024/day6/input.txt")# map[row][col]
anotated_map = map

start_location = list(filter(None, [find_guard_in_row(row, row_ind) for row_ind, row in enumerate(map)]))[0][0]

current = start_location
direction = '^'
anotated_map = mark_as_visited(current, anotated_map)

while not is_edge(next(direction, current)):
   if is_obstacle(next(direction, current)):
      direction = rotate(direction)
   else:
      current = next(direction, current)
      anotated_map = mark_as_visited(current, anotated_map)

visited_count = sum([row.count('X') for row in anotated_map])

print("Visited locations: " + str(visited_count))
