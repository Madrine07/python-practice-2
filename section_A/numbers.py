#  no. 1

def calculate_grade(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 80:
        return "B"
    elif percentage >= 70:
        return "C"
    elif percentage >= 60:
        return "D"
    elif percentage >= 50:
        return "E"
    else:
        return "Fail"

score = float(input("Enter student's percentage score: "))
print(f"Grade: {calculate_grade(score)}")


# no. 1) a)ii)

def celsius_to_fahrenheit(c):
    return (9/5) * c + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
choice = int(input("Enter choice (1 or 2): "))

if choice == 1:
    celsius = float(input("Enter temperature in Celsius: "))
    print(f"{celsius}°C is {celsius_to_fahrenheit(celsius)}°F")
else:
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    print(f"{fahrenheit}°F is {fahrenheit_to_celsius(fahrenheit)}°C")


# no.)1)b)i

def calculate_triangle_area(base, height):
    return 0.5 * base * height


base = float(input("Enter base of triangle: "))
height = float(input("Enter height of triangle: "))
print(f"Area of triangle: {calculate_triangle_area(base, height)}")

# no.1)b)ii)

def sum_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total


sample_list = [9, 2, 3, 5, 8]
print(f"Sum of numbers: {sum_list(sample_list)}")

