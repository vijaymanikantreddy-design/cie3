import pytest
def student_details(name, id, course, year):
    result = (
        f"student Name: {name}\n"
        f"student ID: {id}\n"
        f"course: {course}\n"
        f"year: {year}"
    )
    return result
if _name_ == "_main_":
    #Sample Output
    name = "mani"
    id = 035
    quantity = 10
    price = 48000
    print(product_details(name, id, course, year))