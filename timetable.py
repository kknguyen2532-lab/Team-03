def by_day(timetable: list[tuple[str,str]]) -> dict[str, list[str]]:
    result = {}
    for courses, days in timetable:
        result.setdefault(days, []).append(courses)

    for days in result:
        result[days].sort()

    return result