f = open("day_1.txt", "r")
left_ids = []
right_ids = []
for x in f:
  loc_ids = x.split('   ')
  left_ids.append(loc_ids[0])
  right_ids.append(loc_ids[1])
f.close()

left_ids.sort()
right_ids.sort()

total_distance = 0
for i in range(len(left_ids)):
  total_distance += abs(int(left_ids[i]) - int(right_ids[i]))

print(total_distance)