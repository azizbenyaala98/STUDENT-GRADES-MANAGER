"""
=====================================================================
 PYTHON ACTIVITY : STUDENT GRADES MANAGER
=====================================================================
 Student name : ______________________      Date : ______________

 GOAL
 ----
 Build a small program that manages the grades of a class.
 You will practise:
     - functions and parameters
     - conditions (if / elif / else)
     - loops (for)
     - lists
     - lists containing lists (a "list of lists")

 HOW TO WORK
 -----------
 1. Read the explanation above each function.
 2. Write your code where you see:   # >>> YOUR CODE HERE <<<
    (delete the line "pass" when you write your code)
 3. Run the file. At the bottom, each test prints PASS or FAIL.
 4. Your goal: get PASS on every test.

 THE DATA
 --------
 Each student is a small list:   [name, grades]
     - name    : text, example "Amine"
     - grades  : a list of numbers (marks out of 20), example [12, 14, 10]

 So a student looks like this:     ["Amine", [12, 14, 10]]

 All students together are stored in ONE big list (a list of lists):

     [ ["Amine", [12, 14, 10]],
       ["Sara",  [18, 17, 19]],
       ... ]

 Useful reminders:
     student[0]            -> the name            "Amine"
     student[1]            -> the grades list     [12, 14, 10]
     student[1][0]         -> the first grade     12
     students[0]           -> the first student   ["Amine", [12, 14, 10]]
     students[0][1][2]     -> third grade of first student  10
     len(a_list)           -> number of elements in a list
=====================================================================
"""


# ---------------------------------------------------------------------
# DATA PROVIDER (already written - do not change)
# Returns a NEW list every time it is called, so that the tests do
# not disturb each other.
# ---------------------------------------------------------------------
def make_data():
    return [
        ["Amine", [12, 14, 10]],
        ["Sara", [18, 17, 19]],
        ["Youssef", [8, 9, 7]],
        ["Lina", [15, 13, 16]],
    ]


# =====================================================================
# EXERCISE 1 - get_mention(average)                 [parameters + conditions]
# =====================================================================
# A function receives information through PARAMETERS (here: average)
# and gives back a result with "return".
#
# This function gives the mention that matches an average:
#     - "Excellent" if average >= 16
#     - "Good"      if average >= 14
#     - "Pass"      if average >= 10
#     - "Fail"      otherwise
#
# Order matters: test the highest limit first (if / elif / else).
#
# Example: get_mention(14.7)  ->  "Good"
# ---------------------------------------------------------------------
def get_mention(average):
    # >>> YOUR CODE HERE <<<
    pass


# =====================================================================
# EXERCISE 2 - student_average(grades)              [loop + accumulator]
# =====================================================================
# An ACCUMULATOR is a variable that adds up values in a loop:
#
#     total = 0
#     for grade in grades:
#         total = total + grade
#
# Compute the average of a list of grades:
#     average = total / number of grades      (len(grades) gives the number)
# Return the result rounded to 1 decimal:  round(value, 1)
#
# Example: student_average([12, 14, 10])  ->  12.0
# ---------------------------------------------------------------------
def student_average(grades):
    # >>> YOUR CODE HERE <<<
    pass


# =====================================================================
# EXERCISE 3 - display_students(students)           [loop + list of lists]
# =====================================================================
# A "for" loop repeats code for every element of a list. When the list
# contains lists, each turn of the loop gives you ONE small list:
#
#     for student in students:
#         print(student[0])      # prints the name of each student
#
# Print one line per student, in this format:
#     Amine | average 12.0 | Pass
# Use student_average() and get_mention() from the previous exercises.
# This function does not return anything, it only prints.
# ---------------------------------------------------------------------
def display_students(students):
    # >>> YOUR CODE HERE <<<
    pass


# =====================================================================
# EXERCISE 4 - add_student(students, name, grades)  [list.append]
# =====================================================================
# .append(x) adds x at the END of a list.
# To add a student, build a small list [name, grades] and append it
# to the big list.
#
# Important: the function MODIFIES the list it receives, so it does
# not need to return anything.
#
# Example: add_student(students, "Nour", [11, 9, 11])
#          -> students now ends with ["Nour", [11, 9, 11]]
# ---------------------------------------------------------------------
def add_student(students, name, grades):
    # >>> YOUR CODE HERE <<<
    pass


# =====================================================================
# EXERCISE 5 - count_by_mention(students, mention)  [loop + condition + counter]
# =====================================================================
# A COUNTER is a variable that starts at 0 and grows by 1 each time
# something is found:
#
#     count = 0
#     for student in students:
#         if (some condition):
#             count = count + 1
#     return count
#
# Count how many students have the given mention
# ("Excellent", "Good", "Pass" or "Fail").
# Hint: compute the average of the student, then its mention.
#
# Example: count_by_mention(students, "Fail") -> 1
# ---------------------------------------------------------------------
def count_by_mention(students, mention):
    # >>> YOUR CODE HERE <<<
    pass


# =====================================================================
# EXERCISE 6 - find_by_mention(students, mention)   [building a new list]
# =====================================================================
# Sometimes we want to COLLECT results. Start with an empty list [],
# then .append() each result found in the loop:
#
#     result = []
#     for student in students:
#         if (some condition):
#             result.append(student[0])
#     return result
#
# Return the list of NAMES of the students that have the given mention.
#
# Example: find_by_mention(students, "Good") -> ["Lina"]
# ---------------------------------------------------------------------
def find_by_mention(students, mention):
    # >>> YOUR CODE HERE <<<
    pass


# =====================================================================
# EXERCISE 7 - add_grade(students, name, grade)     [search + modify a list]
# =====================================================================
# Loop through the students; when student[0] equals the given name,
# add the new grade to HIS grades list (student[1].append(grade))
# and return True.
# If the loop ends without finding the name, return False.
#
# Tip: "return" stops the function immediately.
#
# Example: add_grade(students, "Amine", 16) -> True
#          Amine's grades become [12, 14, 10, 16]
#          add_grade(students, "Ghost", 10) -> False
# ---------------------------------------------------------------------
def add_grade(students, name, grade):
    # >>> YOUR CODE HERE <<<
    pass


# =====================================================================
# EXERCISE 8 - best_student(students)               [finding the maximum]
# =====================================================================
# To find the best element, keep the best value found so far:
#
#     best_name = ""
#     best_average = -1
#     for student in students:
#         ... compute the average of this student ...
#         if average > best_average:
#             best_average = average
#             best_name = student[0]
#
# Return the NAME of the student with the highest average.
#
# Example: with the starting data -> "Sara"
# ---------------------------------------------------------------------
def best_student(students):
    # >>> YOUR CODE HERE <<<
    pass


# =====================================================================
# EXERCISE 9 - class_average(students)              [nested loops]
# =====================================================================
# A loop can be placed INSIDE another loop (nested loops).
# The outer loop goes through the students, the inner loop goes
# through the grades of the current student:
#
#     for student in students:
#         for grade in student[1]:
#             ... use grade ...
#
# Compute the average of ALL the grades of the whole class
# (every grade counts once): add all the grades in a total, count them
# in a counter, then divide. Return the result rounded to 1 decimal.
#
# Example: with the starting data -> 13.2
# ---------------------------------------------------------------------
def class_average(students):
    # >>> YOUR CODE HERE <<<
    pass


# =====================================================================
# EXERCISE 10 - build_report(students)              [creating a list of lists]
# =====================================================================
# You can also CREATE a list of lists: append a small list to a big list.
#
#     report = []
#     report.append(["Amine", 12.0, "Pass"])
#
# Return a new list where each element is [name, average, mention].
#
# Example: [["Amine", 12.0, "Pass"], ["Sara", 18.0, "Excellent"], ...]
# ---------------------------------------------------------------------
def build_report(students):
    # >>> YOUR CODE HERE <<<
    pass


# =====================================================================
# FINAL CHALLENGE - put everything together
# =====================================================================
# Write your code in the function below. Use ONLY the functions you
# wrote above. Steps:
#   1. create the data with make_data()
#   2. add a new student: "Nour" with the grades [11, 9, 11]
#   3. add the grade 14 to "Youssef"
#   4. display all students with display_students()
#   5. print the best student, example:   "Best student: ..."
#   6. print the class average, example:  "Class average: ..."
#   7. print the names of the students who failed, example:
#      "Failed: [...]"
# ---------------------------------------------------------------------
def final_challenge():
    # >>> YOUR CODE HERE <<<
    pass


# =====================================================================
# SELF-CHECK SECTION (already written - do not change)
# =====================================================================
# check() runs a test safely and prints PASS or FAIL.
# "lambda: ..." is just a way to give the test to check() so that an
# error in your code does not stop the whole program.
# ---------------------------------------------------------------------
score = 0
total_tests = 0


def check(label, test, expected):
    global score, total_tests
    total_tests += 1
    try:
        result = test()
    except Exception as error:
        result = "ERROR: " + str(error)
    if result == expected:
        score += 1
        print("PASS -", label)
    else:
        print("FAIL -", label, "| expected:", expected, "| got:", result)


def run_tests():
    print("-" * 60)
    print("RESULTS")
    print("-" * 60)

    # Exercise 1
    check("1a get_mention Excellent", lambda: get_mention(16), "Excellent")
    check("1b get_mention Good", lambda: get_mention(14), "Good")
    check("1c get_mention Pass", lambda: get_mention(10), "Pass")
    check("1d get_mention Fail", lambda: get_mention(9.9), "Fail")

    # Exercise 2
    check("2 student_average", lambda: student_average([12, 14, 10]), 12.0)

    # Exercise 4
    def test_add():
        data = make_data()
        add_student(data, "Nour", [11, 9, 11])
        return len(data), data[-1]
    check("4 add_student", test_add, (5, ["Nour", [11, 9, 11]]))

    # Exercise 5
    check("5a count Fail", lambda: count_by_mention(make_data(), "Fail"), 1)
    check("5b count Pass", lambda: count_by_mention(make_data(), "Pass"), 1)

    # Exercise 6
    check("6 find Good", lambda: find_by_mention(make_data(), "Good"), ["Lina"])

    # Exercise 7
    def test_add_grade():
        data = make_data()
        found = add_grade(data, "Amine", 16)
        return found, data[0][1]
    check("7a add_grade found", test_add_grade, (True, [12, 14, 10, 16]))
    check("7b add_grade not found", lambda: add_grade(make_data(), "Ghost", 10), False)

    # Exercise 8
    check("8 best_student", lambda: best_student(make_data()), "Sara")

    # Exercise 9
    check("9 class_average", lambda: class_average(make_data()), 13.2)

    # Exercise 10
    check(
        "10 build_report",
        lambda: build_report(make_data()),
        [["Amine", 12.0, "Pass"], ["Sara", 18.0, "Excellent"],
         ["Youssef", 8.0, "Fail"], ["Lina", 14.7, "Good"]],
    )

    print("-" * 60)
    print("SCORE:", score, "/", total_tests)
    print("-" * 60)


# =====================================================================
# PROGRAM START (do not change)
# =====================================================================
if __name__ == "__main__":
    print("=== Exercise 3 : display ===")
    display_students(make_data())
    print()
    run_tests()
    print()
    print("=== Final challenge ===")
    final_challenge()
