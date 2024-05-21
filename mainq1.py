ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print("Sorted list:", ages)
min_age = ages[0]
max_age = ages[-1]
print("Minimum age:", min_age)
print("Maximum age:", max_age)
ages.append(min_age)
ages.append(max_age)
print("List with min and max ages added:", ages)
n = len(ages)
ages.sort()
if n % 2 == 0:
    median = (ages[n//2 - 1] + ages[n//2]) / 2
else:
    median = ages[n//2]
print("Median age:", median)
average_age = sum(ages) / len(ages)
print("Average age:", average_age)
age_range = max_age - min_age
print("Range of ages:", age_range)
