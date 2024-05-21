it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
print("Length of it_companies set:", len(it_companies))
it_companies.add('Twitter')
print("it_companies set after adding 'Twitter':", it_companies)
it_companies.update(['Samsung', 'Huawei', 'Xiaomi'])
print("it_companies set after adding multiple companies:", it_companies)
it_companies.remove('Xiaomi')
print("it_companies set after removing 'Xiaomi':", it_companies)
print("A union B:", A.union(B))
print("A intersection B:", A.intersection(B))
print("Is A subset of B?", A.issubset(B))
print("Are A and B disjoint sets?", A.isdisjoint(B))
print("A union B:", A.union(B))
print("B union A:", B.union(A))
print("Symmetric difference between A and B:", A.symmetric_difference(B))
del A, B
age_set = set(age)
print("Age list:", age)
print("Age set:", age_set)
print("Length of age list:", len(age))
print("Length of age set:", len(age_set))
