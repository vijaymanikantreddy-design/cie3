from student import student_details

def test_student_details():
    expected_output = (
        "student Name: mani\n"
        "student ID: 35\n"
        "course: bca\n"
        "year: 2025"
    )
    assert student_details("mani", "35", "bca", 2025) == expected_output