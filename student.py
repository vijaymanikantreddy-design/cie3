

def student_details(name, id, course, year):
    result = (
        f"student Name: {name}\n"
        f"student ID: {id}\n"
        f"course: {course}\n"
        f"year: {year}"
    )
    return result

if __name__ == "__main__":
    # Sample Output
    name = "mani"
    id = "035"
    course = "bca"
    year = 2025
    print(student_details(name, id, course, year))
