
import statistics
import matplotlib.pyplot as plt

# Sample student marks
students = ["Aman", "Priya", "Rahul", "Neha", "Riya"]
marks = [78, 92, 65, 88, 74]

# Calculate statistics
average_marks = statistics.mean(marks)
highest_marks = max(marks)
lowest_marks = min(marks)

print("STUDENT MARKS ANALYSIS")
print("")
print("Average marks:", round(average_marks, 2))
print("Highest marks:", highest_marks)
print("Lowest marks:", lowest_marks)
print("Top student:", students[marks.index(highest_marks)])

# Create a bar chart
plt.bar(students, marks)
plt.title("Student Marks Analysis")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.ylim(0, 100)
plt.tight_layout()
plt.savefig("student_marks.png")
plt.show()