def find_invalid_registrations(d, course_code, lab_code):

    invalid_registrations = []

    if course_code in d and lab_code in d:
        course_code_list = d[course_code]
        lab_code_list = d[lab_code]
        for student in course_code_list:
            if student not in lab_code_list:
                invalid_registrations.append(student)

    return invalid_registrations


registrations = {
    "python101": ["Ojas", "Shyam", "Mohan", "Eli"],
    "python102": ["Helen", "Jesus", "Menna"],
    "python103": ["Lesley", "Eli", "Keala"],
    "lab_101": ["Ojas", "Shyam"],
    "lab_102": ["Menna", "Helen"],
    "lab_103": ["Lesley", "Keala"]

}


print(find_invalid_registrations(registrations, "python101", "lab_101"))
