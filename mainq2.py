dog = {}
dog['name'] = 'Buddy'
dog['color'] = 'Brown'
dog['breed'] = 'Labrador'
dog['legs'] = 4
dog['age'] = 3
print("Dog Dictionary:", dog)
student = {
    'first_name': 'John',
    'last_name': 'Doe',
    'gender': 'Male',
    'age': 25,
    'marital_status': 'Single',
    'skills': ['Python', 'JavaScript'],
    'country': 'USA',
    'city': 'New York',
    'address': '123 Main St'
}
print("\nStudent Dictionary:", student)
print("\nLength of Student Dictionary:", len(student))
skills = student['skills']
print("\nStudent Skills:", skills)
print("Data Type of Skills:", type(skills))
student['skills'].append('React')
student['skills'].append('Node.js')
print("\nUpdated Student Skills:", student['skills'])
keys = list(student.keys())
print("\nDictionary Keys:", keys)
values = list(student.values())
print("\nDictionary Values:", values)
