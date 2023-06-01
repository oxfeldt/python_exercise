name = input("Enter your name: ")
age = int(input("Enter your age: "))
vægt = int(input("Enter your weight: "))
højde = int(input("Enter your height: "))
højde_done = 2 * højde / 100
bmi = vægt / højde_done
print(f"Hello, {name} you are {age} old, you have a height of {højde}cm and weight {vægt}kg, therefor your BMI is: {bmi}")