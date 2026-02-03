
def calculate_average(marks):
    return sum(marks) / len(marks)

student_marks = {
    "Alice": [85, 90, 78],
    "Bob": [92, 88, 95],
    "Charlie": [70, 75, 80]
}
print(f"Average Marks of Students:{len(student_marks)}")
# create    a another dic that contains the average marks of each student >75
average_marks = {}
for student, marks in student_marks.items():
    print(f"Calculating average for {student} with marks {marks}")
    avg = calculate_average(marks)
    average_marks[student] = avg

print("Average Marks of Students >75:")
for student, avg in average_marks.items():
    if avg > 75:
        print(f"{student}: {avg:.2f}")


numbers = [1, 2, 3, 4, 5]

squared_or_halved = [n**2 if n % 2 == 0 else n / 2 for n in numbers]
print(f"Squared or Halved: {squared_or_halved}")
print(sum(squared_or_halved))
print(sum([1,2,3,4,5]))

