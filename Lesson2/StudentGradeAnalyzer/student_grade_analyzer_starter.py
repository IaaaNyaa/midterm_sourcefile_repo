def classify_grade(grade):
    """Return the classification and status of a grade."""
    if 90 <= grade <= 100:
        return ("Excellent", "Passed")
    elif 85 <= grade <= 89:
        return ("Very Good", "Passed")
    elif 80 <= grade <= 84:
        return ("Good", "Passed")
    elif 75 <= grade <= 79:
        return ("Satisfactory", "Passed")
    else:
        return ("Needs Improvement", "Failed")


def load_students(filename):
    """Read valid student records from a text file and return them as a list."""
    students = []
    try:
        with open(filename, "r") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                parts = line.split(",")
                if len(parts) != 3:
                    continue
                student_id, name, grade_str = parts
                try:
                    grade = float(grade_str)
                    if 0 <= grade <= 100:
                        students.append({
                            "student_id": student_id,
                            "name": name,
                            "grade": grade
                        })
                except ValueError:
                    continue
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    return students


def calculate_statistics(students):
    """Calculate and return the class statistics."""
    if not students:
        return None

    total_grade = 0
    passed_count = 0
    failed_count = 0
    highest_student = students[0]
    lowest_student = students[0]

    for student in students:
        grade = student["grade"]
        total_grade += grade
        classification, status = classify_grade(grade)
        if status == "Passed":
            passed_count += 1
        else:
            failed_count += 1
        if grade > highest_student["grade"]:
            highest_student = student
        if grade < lowest_student["grade"]:
            lowest_student = student

    average = total_grade / len(students)

    return {
        "count": len(students),
        "average": average,
        "passed": passed_count,
        "failed": failed_count,
        "highest": highest_student,
        "lowest": lowest_student
    }


def display_students(students):
    """Display all student records in a formatted table."""
    print("\nSTUDENT LIST")
    print(f"{'ID':<10} {'Name':<20} {'Grade':<8} {'Classification':<15} {'Status':<10}")
    print("-" * 65)
    for student in students:
        classification, status = classify_grade(student["grade"])
        print(f"{student['student_id']:<10} {student['name']:<20} {student['grade']:<8.2f} {classification:<15} {status:<10}")


def display_statistics(statistics):
    """Display the calculated class statistics."""
    print("\nCLASS STATISTICS")
    print(f"Number of students: {statistics['count']}")
    print(f"Class average: {statistics['average']:.2f}")
    print(f"Passed: {statistics['passed']}")
    print(f"Failed: {statistics['failed']}")
    print(f"Highest: {statistics['highest']['name']} - {statistics['highest']['grade']:.2f}")
    print(f"Lowest: {statistics['lowest']['name']} - {statistics['lowest']['grade']:.2f}")


def search_student(students, keyword):
    """Return records whose student number or name matches the keyword."""
    matches = []
    keyword = keyword.strip().lower()
    for student in students:
        if keyword in student["student_id"].lower() or keyword in student["name"].lower():
            matches.append(student)
    return matches


def save_report(students, statistics, filename):
    """Write the student results and class statistics to a report file."""
    try:
        with open(filename, "w") as file:
            file.write("GRADE REPORT\n\n")
            file.write(f"{'ID':<10} {'Name':<20} {'Grade':<8} {'Classification':<15} {'Status':<10}\n")
            file.write("-" * 65 + "\n")
            for student in students:
                classification, status = classify_grade(student["grade"])
                file.write(f"{student['student_id']:<10} {student['name']:<20} {student['grade']:<8.2f} {classification:<15} {status:<10}\n")

            file.write("\nCLASS STATISTICS\n")
            file.write(f"Number of students: {statistics['count']}\n")
            file.write(f"Class average: {statistics['average']:.2f}\n")
            file.write(f"Passed: {statistics['passed']}\n")
            file.write(f"Failed: {statistics['failed']}\n")
            file.write(f"Highest: {statistics['highest']['name']} - {statistics['highest']['grade']:.2f}\n")
            file.write(f"Lowest: {statistics['lowest']['name']} - {statistics['lowest']['grade']:.2f}\n")
        print(f"Report saved to {filename}")
    except OSError:
        print("Error: Could not save the report.")


def main():
    """Run the menu-driven Student Grade Analyzer."""
    students = load_students("grades.txt")

    if not students:
        print("No valid student records were loaded.")
        return

    statistics = calculate_statistics(students)

    while True:
        print("\nSTUDENT GRADE ANALYZER")
        print("[1] Display all students")
        print("[2] Display class statistics")
        print("[3] Search for a student")
        print("[4] Save report")
        print("[5] Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            display_students(students)
        elif choice == "2":
            display_statistics(statistics)
        elif choice == "3":
            keyword = input("Enter student number or name: ")
            matches = search_student(students, keyword)
            if matches:
                display_students(matches)
            else:
                print("No matching student found.")
        elif choice == "4":
            save_report(students, statistics, "grade_report.txt")
        elif choice == "5":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
            continue


if __name__ == "__main__":
    main()
