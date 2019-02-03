import csv

with open('data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['id', 'name', 'age'])
    writer.writerow(['10001', 'Mike', '20'])
    writer.writerow(['10002', 'Bob', '22'])
    writer.writerow(['10003', 'Jordan', '21'])


with open('data1.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=' ')
    writer.writerow(['id', 'name', 'age'])
    writer.writerow(['10001', 'Mike', '20'])
    writer.writerow(['10002', 'Bob', '22'])
    writer.writerow(['10003', 'Jordan', '21'])

with open('data2.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['id', 'name', 'age'])
    writer.writerows([['10001', 'Mike', '20'], ['10002', 'Bob', '22'],['10003', 'Jordan', '21']])

with open('data3.csv', 'w', newline='') as csvfile:
    fieldnames = ['id', 'name', 'age']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'id': '10001', 'name': 'Mike', 'age': 20})
    writer.writerow({'id': '10002', 'name': 'Bob', 'age': 22})
    writer.writerow({'id': '10003', 'name': 'Jordan', 'age': 21})


# 写入中文需要编码
with open('data3.csv', 'a', encoding='utf-8', newline='') as csvfile:
    fieldnames = ['id', 'name', 'age']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writerow({'id':'10005', 'name':'王伟', 'age':22})


with open('data3.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)
