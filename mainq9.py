N = int(input("Enter the number of students: "))
weights_lbs = []
print("Enter the weights of students in pounds (lbs):")
for i in range(N):
    weight_lb = float(input(f"Weight of student {i+1}: "))
    weights_lbs.append(weight_lb)

weights_kg = []
for weight_lb in weights_lbs:
    weight_kg = weight_lb * 0.453592
    weights_kg.append(weight_kg)

print("\nWeights in pounds (lbs):", weights_lbs)
print("Weights in kilograms (kg):", ["{:.2f}".format(weight) for weight in weights_kg])
