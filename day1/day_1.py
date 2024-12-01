f = open("day_1.txt", "r")
left_ids = []
right_ids = []
for x in f:
  loc_ids = x.split('   ')
  left_ids.append(loc_ids[0])
  right_ids.append(loc_ids[1].strip())
f.close()

left_ids.sort()
right_ids.sort()

total_distance = 0
for i in range(len(left_ids)):
  total_distance += abs(int(left_ids[i]) - int(right_ids[i]))

print("Total distance: " + str(total_distance))

total_similarity_score = 0
for id in left_ids:
  similarity_score = right_ids.count(id) * int(id)
  total_similarity_score += similarity_score
print("Similarity score: " + str(total_similarity_score))
