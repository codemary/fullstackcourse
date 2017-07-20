def notify_exam_conflict(d, course_codes):

    exam_time_conflict_students = []

    for couese_code, v in d.items():
        exam_slot = v[1][0]
        for couese_code2, v2 in d.items():
            if couese_code2 == couese_code:
                continue
            exam_slot2 = v2[1][0]
            if exam_slot2 == exam_slot:
                tmp = []
                tmp.extend(v[0])
                tmp.extend(v2[0])
                student_conflicts = [s for s in tmp if tmp.count(s) == 2]
                exam_time_conflict_students.extend(student_conflicts)

    exam_time_conflict_students = list(set(exam_time_conflict_students))

    return exam_time_conflict_students


registration_record = {
    "python101": [["Ojas", "Helen", "Keala", "Eli"], ["1300_hours"]],
    "python102": [["Helen", "Jesus", "Menna"], ["900_hours"]],
    "python103": [["Lesley", "Menna", "Keala"], ["1300_hours"]]
}


print(notify_exam_conflict(registration_record, "python101"))
