# Function to convert score to grade point
def score_to_grade_point(score):
    if score >= 70:
        return 5.0
    elif score >= 60:
        return 4.0
    elif score >= 50:
        return 3.0
    elif score >= 45:
        return 2.0
    elif score >= 40:
        return 1.0
    else:
        return 0.0


# List to store students data
students = [
    {
        "id": 1038,
        "name": "Sakinat Isah Agono",
        "level": 200,
        "courses": {
            "MAT201": 75,
            "CSC201": 72,
            "PHY201": 69,
        }
    },
    {
        "id": 1022,
        "name": "Musa Abdullahi",
        "level": 300,
        "courses": {
            "CSC301": 58,
            "MAT301": 62,
            "STA301": 55
        }
    },
    {
        "id": 1040,
        "name": "Zainab Sadiq",
        "level": 100,
        "courses": {
            "ENG101": 80,
            "MAT101": 74,
            "CSC101": 69
        }
    },
    {
        "id": 1024,
        "name": "Ibrahim Yusuf",
        "level": 400,
        "courses": {
            "CSC401": 45,
            "CSC402": 52,
            "CSC403": 60
        }
    },
    {
        "id": 1005,
        "name": "Fatima Lawal",
        "level": 200,
        "courses": {
            "BIO201": 66,
            "CHM201": 71,
            "PHY201": 63
        }
    }
]


# Calculate and display GPA for each student
for student in students:
    total_points = 0
    number_of_courses = len(student["courses"])

    for score in student["courses"].values():
        total_points += score_to_grade_point(score)

    gpa = total_points / number_of_courses

    print("Student Name:", student["name"])
    print("Student ID:", student["id"])
    print("Level:", student["level"])
    print("GPA:", round(gpa, 2))
    print("_" *30)