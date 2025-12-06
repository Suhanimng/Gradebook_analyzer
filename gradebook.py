import csv

"""
Gradebook Analyzer
Name: Suhani
Date: 6/12/2025
Title: Gradebook Analyzer
"""

# Function to calculate average score
def calculate_average(marks_dict):
    if not marks_dict:
        return 0
    return sum(marks_dict.values()) / len(marks_dict)


# Function to calculate median score
def calculate_median(marks_dict):
    if not marks_dict:
        return 0

    sorted_values = sorted(marks_dict.values())
    length = len(sorted_values)
    mid_index = length // 2

    if length % 2 == 0:
        return (sorted_values[mid_index - 1] + sorted_values[mid_index]) / 2
    return sorted_values[mid_index]


# Function to calculate maximum score
def find_max_score(marks_dict):
    if not marks_dict:
        return 0
    return max(marks_dict.values())


# Function to calculate minimum score
def find_min_score(marks_dict):
    if not marks_dict:
        return 0
    return min(marks_dict.values())

# -----------------Main Program------------#
def main():
    print("Welcome to the Gradebook Analyzer!")

    while True:
        print("\n--- Menu ---")
        print("1. Enter Marks Manually")
        print("2. Read from CSV File")
        print("3. Exit")

        try:
            choice = int(input("Choose an option: "))
        except ValueError:
            print("Invalid input. Enter a number.")
            continue

        if choice == 3:
            print("Program Closed.")
            break

        if choice not in (1, 2):
            print("Invalid option. Try again.")
            continue

        marks_dict = {}

        # Manual Entry
        if choice == 1:
            try:
                count = int(input("How many students? "))
                for i in range(1, count + 1):
                    name = input(f"Student {i} name: ")
                    score = int(input(f"Marks for {name}: "))
                    marks_dict[name] = score
            except ValueError:
                print("Error: Marks should be a number.")
                continue

        # CSV Entry
        elif choice == 2:
            try:
                with open("marks.csv", "r", newline="") as f:
                    reader = csv.reader(f)
                    for row in reader:
                        if row:
                            marks_dict[row[0]] = int(row[1])
            except FileNotFoundError:
                print("marks.csv not found.")
                continue
            except (ValueError, IndexError):
                print("File contains invalid data.")
                continue

        # Statistics
        print("\n--- Analysis Report ---")
        print(f"Average Score:  {calculate_average(marks_dict):.2f}")
        print(f"Median Score:   {calculate_median(marks_dict)}")
        print(f"Highest Score:  {find_max_score(marks_dict)}")
        print(f"Lowest Score:   {find_min_score(marks_dict)}")

        # Grades
        grades = {}
        grade_count = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}

        for student, score in marks_dict.items():
            if score >= 90:
                g = "A"
            elif score >= 80:
                g = "B"
            elif score >= 70:
                g = "C"
            elif score >= 60:
                g = "D"
            else:
                g = "F"

            grades[student] = g
            grade_count[g] += 1

        print("\nGrade Distribution:")
        for grade, count in grade_count.items():
            print(f"{grade}: {count}")

        # Pass / Fail
        passed = [name for name in marks_dict if marks_dict[name] >= 40]
        failed = [name for name in marks_dict if marks_dict[name] < 40]

        print("\nPassed:", ", ".join(passed) if passed else "None")
        print("Failed:", ", ".join(failed) if failed else "None")

        # Final table
        print("\n----------- Final Results -----------")
        print("Name\t\tMarks\tGrade")
        print("-------------------------------------")
        for name, score in marks_dict.items():
            print(f"{name}\t\t{score}\t{grades[name]}")

        print("\n" + "=" * 40)


# Run the program
if __name__ == "__main__":
    main()
