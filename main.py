import csv
import statistics
from tabulate import tabulate

with open('math.csv', 'r', encoding='utf-8') as f:
    data = {}
    reader = csv.DictReader(f)
    for row in reader:
        data.setdefault(row['student'], []).append(int(row['coffee_spent']))

    for student, values in data.items():
        median = statistics.median(values)
        sorted_data = sorted(data.items(), key=lambda x: statistics.median(x[1]), reverse=True)
    result = [[student, statistics.median(values)] for student, value in sorted_data]
    print(tabulate(result, headers=['student', 'coffee_spent'], tablefmt='grid'))
