# #(a)i
# #the grades the students will be receiving
# #the grades are
# #90%-100% grade is A
# #80%-89& grade is B
# # #70%-79% grade is C
# # #60%-69% GRADE is D
# # #50% -59% grade is E
# # #<50% = FAIL

# def calculate_grade(score):
#     if score >= 90:
#         return "A"
#     elif score >= 80:
#         return "B"
#     elif score >= 70:
#         return "C"
#     elif score >= 60:
#         return "D"
#     elif score >= 50:
#         return "E"
#     else:
#         return "FAIL"

# def main():
#     try:
#         score = float(input("Enter the student's score: "))
#         if score < 0 or score > 100:
#             print("Invalid score! Score should be between 0 and 100.")
#         else:
#             grade = calculate_grade(score)
#             print(f"The student's grade is: {grade}")
#     except ValueError:
#         print("Invalid input! Please enter a numeric value for the score.")

# if __name__ == "__main__":
#     main()


# #(ii)

# def celsiusToFahrenheit(celsius):
#     fahrenheit = (9/5) * celsius + 32
#     return fahrenheit

# def main():
#     try:
#         celsius = float(input("Enter the temperature in Celsius: "))
#         fahrenheit = celsiusToFahrenheit(celsius)
#         print("Temperature in Fahrenheit:", fahrenheit)
#     except ValueError:
#         print("Enter valid numeric value for temperature.")

# if __name__ == "__main__":
#     main()


# #b(i)
# def calculate_rectangle_area(base, height):
#     return 0.5 * base * height

# def main():
#     try:
#         base = float(input("Enter the base: "))
#         height = float(input("Enter the height: "))

#         area = calculate_rectangle_area(base, height)

#         print("Area of the rectangle is:", area)
#     except ValueError:
#         print("Please enter valid numeric values for base and height.")

# if __name__ == "__main__":
#     main()

#(ii)

#simple list (8,2,3,0,7)
def sum_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

# Example usage:
numbers = [9, 2, 3, 5, 8]
result = sum_list(numbers)
print("The sum is:", result)

