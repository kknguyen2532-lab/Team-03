def by_day(timetable):
    result = {}
    for course, day in timetable:
        result.setdefault(day, []).append(course)

    return {day: sorted(courses) for day, courses in result.items()}


print(by_day([("CSC10014", "Mon"), ("MTH00003", "Tue"), ("CSC10001", "Mon")]))
