def by_day(schedule: list[tuple[str, str]]) -> dict[str, list[str]]:
    """Group courses by day and return a dictionary with sorted lists of courses per day."""
    timetable = {}
    
    for course, day in schedule:
        timetable.setdefault(day, []).append(course)
        
    for day, courses in timetable.items():
        courses.sort()
        
    return timetable