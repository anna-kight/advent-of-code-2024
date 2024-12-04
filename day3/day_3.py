import re

def read_file(file_name):
  f = open(file_name, "r")
  lines = []
  for x in f:
    lines.append(x)
  f.close()
  return lines

def find_mul(line :str):
  pattern = re.compile("mul\(\d{1,3},\d{1,3}\)")
  matches = [m.group() for m in pattern.finditer(line)]
  return matches

def split_and_multiply(pair :str):
  pair_split = pair.split(',')
  return int(pair_split[0]) * int(pair_split[1])

bad_instructions = read_file("input.txt")
instructions = []
for line in bad_instructions:
  instructions += find_mul(line)

string_numbers = [instruction.strip('mul()') for instruction in instructions]
multiplied = [split_and_multiply(pair) for pair in string_numbers]

print("Sum of multiplications: " + str(sum(multiplied)))

