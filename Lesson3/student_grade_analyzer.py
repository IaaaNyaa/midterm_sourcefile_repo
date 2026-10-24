# Store the raw comma-separated records.
raw_records = [
    "Ana,88,92,90",
    "Ben,70,72,74",
    "Cara,95,91,94",
    "Dan,78,80,76",
    "Ella,85,89,87",
    "Fred,90,85",
    "Gina",
    "Henry,90,eighty,85",
    "Ivy,"
]

# Store the passing average.
PASSING_GRADE = 75

# Create the dictionary that will map names to score lists.
student_scores = {}

# PART A: Parse and organize the records
for record in raw_records:
    # TODO: Split the record into fields.
    fields = record.split(",")

     # TODO: Add a guardian condition for an invalid field count.
    if len(fields) != 4:  
        print(f"Skipped invalid record: {record}")
        continue

    # TODO: Store the student's name.
    name = fields[0]

    # TODO: Convert the score fields to numbers safely.
    try:
        scores = [int(score) for score in fields[1:]]
    except ValueError:
        print(f"Skipped invalid record: {record}")
        continue

    # TODO: Add the name and scores to student_scores.
    student_scores[name] = scores

# PART B: Display records alphabetically
print("ORGANIZED STUDENT RECORDS")
# TODO: Sort the names and display every student and score list.
for name in sorted(student_scores.keys()):
    print(f"{name}: {student_scores[name]}")

# Create a list for result tuples.
ranking = []

# Create counters for the class summary.
passed_count = 0
failed_count = 0
sum_of_averages = 0

# PART C: Calculate results
for name, scores in student_scores.items():
    # TODO: Guard against an empty score list.
    if not scores:
        continue

    # TODO: Calculate total, average, highest, and lowest.
    total = sum(scores)
    average = total / len(scores)
    highest_score = max(scores)
    lowest_score = min(scores)

    # TODO: Determine the student's remark.
    remark = "Passed" if average >= PASSING_GRADE else "Failed"

    # TODO: Update the passed or failed counter.
    if remark == "Passed":
        passed_count += 1
    else:
        failed_count += 1

    # TODO: Add the average to sum_of_averages.
    sum_of_averages += average

    # TODO: Append the result tuple to ranking.
    ranking.append((average, name, highest_score, lowest_score, remark))

# PART D: Sort and display ranking
# TODO: Sort ranking from highest to lowest average.
ranking.sort(reverse=True, key=lambda x: x[0])

print("\nSTUDENT GRADE REPORT")
print("Rank  Name       Average  Highest  Lowest  Remark")

# TODO: Use enumerate() and tuple unpacking to display the ranking.
for idx, (average, name, high, low, remark) in enumerate(ranking, start=1):
    print(f"{idx:<5} {name:<10} {average:<7.2f} {high:<7} {low:<7} {remark}")

# PART E: Class summary
# TODO: Calculate the class average safely.
class_average = sum_of_averages / len(ranking) if ranking else 0

# TODO: Use ranking[0] and ranking[-1] safely.
highest_student = ranking[0] if ranking else None
lowest_student = ranking[-1] if ranking else None

print("\nCLASS SUMMARY")

# TODO: Display all required summary information.
print(f"Number of Students: {len(ranking)}")
print(f"Passed: {passed_count}")
print(f"Failed: {failed_count}")
print(f"Class Average: {class_average:.2f}")
if highest_student:
    print(f"Highest: {highest_student[1]} - {highest_student[0]:.2f}")
if lowest_student:
    print(f"Lowest: {lowest_student[1]} - {lowest_student[0]:.2f}")