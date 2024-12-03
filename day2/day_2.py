
def read_file(file_name):
  f = open(file_name, "r")
  reports = []
  for x in f:
    reports.append(x.split(' '))
  f.close()
  return reports

def is_safe(report):
  for i in range(len(report)):
    report[i] = int(report[i])

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
  if is_safe(report):
    safe_count += 1

print("Safe reports: " + str(safe_count))
