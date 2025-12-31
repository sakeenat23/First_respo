# ================================
# Course Class
# ================================
class Course:
    def __init__(self, code, title, credit_unit, level):
        self.code = code
        self.title = title
        self.credit_unit = credit_unit
        self.level = level


# ================================
# Course Registration Class
# ================================
class CourseRegistration:
    def __init__(self, course, score):
        self.course = course
        self.score = score
        self.grade = self._calculate_grade()
        self.grade_point = self._calculate_grade_point()

    def _calculate_grade(self):
        if self.score >= 70:
            return "A"
        elif self.score >= 60:
            return "B"
        elif self.score >= 50:
            return "C"
        elif self.score >= 45:
            return "D"
        elif self.score >= 40:
            return "E"
        else:
            return "F"

    def _calculate_grade_point(self):
        grade_points = {
            "A": 5,
            "B": 4,
            "C": 3,
            "D": 2,
            "E": 1,
            "F": 0
        }
        return grade_points[self.grade]


# ================================
# Semester Class
# ================================
class Semester:
    def __init__(self, name):
        self.name = name
        self.registrations = []

    def register_course(self, course_registration):
        # Prevent duplicate course registration in same semester
        for reg in self.registrations:
            if reg.course.code == course_registration.course.code:
                print(f"Course {reg.course.code} already registered in this semester.")
                return
        self.registrations.append(course_registration)

    def calculate_gpa(self):
        total_units = 0
        total_points = 0

        for reg in self.registrations:
            total_units += reg.course.credit_unit
            total_points += reg.course.credit_unit * reg.grade_point

        return round(total_points / total_units, 2) if total_units > 0 else 0.00


# ================================
# Session Class
# ================================
class Session:
    def __init__(self, session_name, level):
        self.session_name = session_name
        self.level = level
        self.first_semester = Semester("First Semester")
        self.second_semester = Semester("Second Semester")

    def course_registered_in_session(self, course_code):
        for reg in self.first_semester.registrations + self.second_semester.registrations:
            if reg.course.code == course_code:
                return True
        return False


# ================================
# Student Class
# ================================
class Student:
    def __init__(self, matric_no, name):
        self.matric_no = matric_no
        self.name = name
        self.sessions = []

    def add_session(self, session):
        self.sessions.append(session)

    def calculate_cgpa(self):
        total_units = 0
        total_points = 0

        for session in self.sessions:
            for semester in [session.first_semester, session.second_semester]:
                for reg in semester.registrations:
                    total_units += reg.course.credit_unit
                    total_points += reg.course.credit_unit * reg.grade_point

        return round(total_points / total_units, 2) if total_units > 0 else 0.00

    def print_transcript(self):
        print("\n" + "=" * 50)
        print("        STUDENT ACADEMIC TRANSCRIPT")
        print("=" * 50)
        print(f"Name       : {self.name}")
        print(f"Matric No  : {self.matric_no}")

        for session in self.sessions:
            print("\n" + "-" * 50)
            print(f"Session: {session.session_name} | Level: {session.level}")

            self._print_semester(session.first_semester)
            self._print_semester(session.second_semester)

        print("\n" + "=" * 50)
        print(f"FINAL CGPA: {self.calculate_cgpa()}")
        print("=" * 50)

    def _print_semester(self, semester):
        print(f"\n{semester.name}")
        print("-" * 50)

        if not semester.registrations:
            print("No courses registered.")
            return

        for reg in semester.registrations:
            print(
                f"{reg.course.code} | {reg.course.title} | "
                f"Unit: {reg.course.credit_unit} | "
                f"Score: {reg.score} | "
                f"Grade: {reg.grade}"
            )

        print(f"GPA: {semester.calculate_gpa()}")


# ================================
# MAIN PROGRAM (TEST CASE)
# ================================
if __name__ == "__main__":
    # Create Student
    student = Student("U22SE1234", "Sakinat Isah")

    # Create Courses
    mth101 = Course("MTH101", "Calculus I", 3, 100)
    cos101 = Course("COS101", "Introduction to Programming", 3, 100)
    gst101 = Course("GST101", "Use of English", 2, 100)

    mth201 = Course("MTH201", "Linear Algebra", 3, 200)
    cos201 = Course("COS201", "Data Structures", 3, 200)

    # Session 1 (100 Level)
    session1 = Session("2022/2023", 100)

    session1.first_semester.register_course(CourseRegistration(mth101, 78))
    session1.first_semester.register_course(CourseRegistration(cos101, 42))  # spill-over
    session1.second_semester.register_course(CourseRegistration(gst101, 65))

    student.add_session(session1)

    # Session 2 (200 Level - Spill-over included)
    session2 = Session("2023/2024", 200)

    session2.first_semester.register_course(CourseRegistration(cos101, 68))  # re-registered spill-over
    session2.first_semester.register_course(CourseRegistration(mth201, 72))
    session2.second_semester.register_course(CourseRegistration(cos201, 81))

    student.add_session(session2)

    # Print Transcript
    student.print_transcript()