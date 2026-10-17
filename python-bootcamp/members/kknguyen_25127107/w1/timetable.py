def by_day(timetable: list[tuple[str, str]]) -> dict[str, list[str]]:
    result = {}

    for course, day in timetable:
        if day not in result:
            result[day] = []

        result[day].append(course)
    for day, courses in result.items():
        courses.sort()
    return result


print(by_day([("CSC10014", "Mon"), ("MTH00003", "Tue"), ("CSC10001", "Mon")]))
