def by_day(courses):
    result = {}

    for course, day in courses:
        if day not in result:
            result[day] = []

        result[day].append(course)

    for day, course_list in result.items():
        course_list.sort()

    return result


courses = [("CSC10014", "Mon"), ("MTH00003", "Tue"), ("CSC10001", "Mon")]

print(by_day(courses))
