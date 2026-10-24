scores = [85, 91, 64, 72, 78]

print("Student scores:")

for x in scores:
    print(x)

print()

passed = 0
failed = 0

total_scores = sum(scores)
avg_scores = total_scores / len(scores)
highest_scores = max(scores)
lowest_scores = min(scores)

for i in range (len(scores)):
    x = scores[i]

    if x >= 75:
        if x >= 90:
            remark = "Excellent"
        elif x >= 80:
            remark = "Very Good"
        else:
            remark = "Good"

        print(f"Student {i + 1}: {x} - {remark} - Passed")
        passed += 1
    else:
        print(f"Student {i + 1}: {x} - Failed")
        failed += 1

print()

print(f"Total score: {total_scores}")
print(f"Average score: {avg_scores}")
print(f"Highest score: {highest_scores}")
print(f"Lowest: {lowest_scores}")
print(f"Passed: {passed}")
print(f"Failed: {failed}")