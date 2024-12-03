
def read_file(file_name):
  f = open(file_name, "r")
  reports = []
  for x in f:
    reports.append(x.split(' '))
  f.close()
  return reports

def is_safe(report):
  increasing = False
  for i in range(len(report)):
    if i == 0:
      if report[i+1] > report[i]:
        increasing = True
    else:
      if increasing and report[i-1] > report[i]:
        return False
      elif not increasing and report[i-1] < report[i]:
        return False
      dif_previous = abs(report[i-1] - report[i])
      if dif_previous > 3 or dif_previous ==0:
        return False

  return True

reports = read_file("input.txt")
safe_count = 0
for report in reports:
  int_reports = [int(x) for x in report]
  if is_safe(int_reports):
    safe_count += 1
  else:
    for i in range(len(int_reports)):
      with_out_level_i = int_reports[:i] + int_reports[i+1 :]
      if is_safe(with_out_level_i):
        safe_count += 1
        break

print("Safe reports: " + str(safe_count))

# Part 1: 639
# Part 2: 674