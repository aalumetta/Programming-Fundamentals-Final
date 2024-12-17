# Define the Student class
class Student:
    def __init__(self, name: str, grades: list):
        self.name = name  # String variable for the student's name
        self.grades = grades  # List variable for the grades
        self.average = 0.0  # Float variable to store the average grade

    def calculate_average(self):
        """Calculates and sets the average of the grades."""
        self.average = sum(self.grades) / len(self.grades)

    def get_letter_grade(self):
        """Returns a letter grade based on the average score."""
        if self.average >= 90:
            return "A"
        elif self.average >= 80:
            return "B"
        elif self.average >= 70:
            return "C"
        elif self.average >= 60:
            return "D"
        else:
            return "F"

# Function to collect student data
def get_student_data():
    """Collects data for multiple students."""
    students = []  # List to store student objects
    num_students = int(input("Enter the number of students: "))  # Integer variable for the number of students
    
    # Loop to get data for each student
    for i in range(num_students):
        name = input(f"Enter the name of student {i + 1}: ")  # String for student's name
        num_grades = int(input(f"How many grades does {name} have? "))  # Integer for the number of grades
        grades = []  # List to store grades
        
        # Loop to collect grades
        for j in range(num_grades):
            grade = float(input(f"Enter grade {j + 1} for {name}: "))  # Float for grades
            grades.append(grade)  # Add grade to the list
        
        # Create a student object and calculate their average grade
        student = Student(name, grades)
        student.calculate_average()
        students.append(student)  # Add the student object to the list of students

    return students

# Function to display the report
def display_report(students):
    """Displays the student report."""
    print("\nStudent Report:")
    for student in students:
        print(f"Student: {student.name}")
        print(f"Grades: {student.grades}")
        print(f"Average: {student.average:.2f}")
        print(f"Letter Grade: {student.get_letter_grade()}")
        print("-" * 30)

# Main function to execute the program
def main():
    students = get_student_data()  # Get data from the user
    display_report(students)  # Display the report of student grades

# Call the main function to run the program
if __name__ == "__main__":
    main()