def read_file(file_name):
  f = open(file_name, "r")
  rules = []
  updates = []
  for x in f:
    if '|' in x:
      rules.append(x.strip().split('|'))
    elif ',' in x:
      updates.append(x.strip().split(','))
  f.close()
  return rules, updates


def passes_rule(rule, update):
  if rule[0] not in update or rule[1] not in update:
    return True
  loc_first = update.index(rule[0])
  loc_second = update.index(rule[1])
  if loc_first < loc_second:
    return True

def update_valid(rules, update):
  if len(list(filter(None,[passes_rule(rule, update) for rule in rules]))) == len(rules):
    return True
  else:
    return False
  
def get_middle(update):
  return int(update[len(update)//2])

rules, updates = read_file("/home/anna/code/advent-of-code-2024/day5/input.txt")

valid_updates = list(filter(lambda update: update_valid(rules, update), updates))

sum_of_middles = sum([get_middle(update) for update in valid_updates])

print("Sum of middle elements: " + str(sum_of_middles))
