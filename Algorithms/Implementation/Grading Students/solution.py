def gradingStudents(grades):
    for i in range(len(grades)):
        next_multiple = (grades[i] - (grades[i] % 5)) + 5
        if (next_multiple - grades[i]) < 3 and grades[i] >= 38:
            grades[i] = next_multiple

    return grades
