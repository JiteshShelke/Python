import csv

# READ

# with open('file.csv') as f:
#   point=csv.reader(f)
#   for i in point:
#     print(i)
    
# WRITE

with open('hello.csv','w',newline='') as f:
  point=csv.writer(f)
  point.writerow(['suraj',23,90000])
  point.writerow(['suraj',23,90000])
  point.writerow(['sura',23,90000])
  point.writerow(['suraj',23,90000])