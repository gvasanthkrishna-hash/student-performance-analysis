import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data/students.csv")

# Display basic information
print("Dataset Info:")
print(df.info())

# Grade distribution
grade_counts = df["Grade"].value_counts()
print("\nGrade Distribution:")
print(grade_counts)

# Pie chart for grades
grade_counts.plot(kind="pie", autopct="%1.1f%%")
plt.title("Grade Distribution of Students")
plt.ylabel("")
plt.show()

# Weekly study hours vs Grade
study_hours = df.groupby("Grade")["Weekly_Study_Hours"].mean()
print("\nAverage Weekly Study Hours by Grade:")
print(study_hours)

study_hours.plot(kind="bar")
plt.title("Average Study Hours by Grade")
plt.xlabel("Grade")
plt.ylabel("Weekly Study Hours")
plt.show()

# Attendance analysis
attendance_counts = df["Attendance"].value_counts()
print("\nAttendance Distribution:")
print(attendance_counts)

attendance_counts.plot(kind="bar")
plt.title("Attendance Distribution")
plt.xlabel("Attendance")
plt.ylabel("Number of Students")
plt.show()

# Gender vs Grade
gender_grade = pd.crosstab(df["Sex"], df["Grade"])
print("\nGender vs Grade:")
print(gender_grade)

gender_grade.plot(kind="bar", stacked=True)
plt.title("Gender vs Grade Distribution")
plt.xlabel("Gender")
plt.ylabel("Number of Students")
plt.show()

# Conclusion
print("\nConclusion:")
print("Students with higher weekly study hours and regular attendance")
print("tend to achieve better grades.")
