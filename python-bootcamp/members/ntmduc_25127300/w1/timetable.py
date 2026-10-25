def by_day(timetable: list[tuple[str, str]]) -> dict[str, list[str]]:
    """
    Nhóm các môn học theo ngày trong tuần và sắp xếp tên môn học theo thứ tự từ điển.

    Args:
        timetable (list[tuple[str, str]]): Danh sách các tuple chứa thông tin (tên môn học, ngày học).

    Returns:
        dict[str, list[str]]: Từ điển ánh xạ từ ngày học sang danh sách các môn học trong ngày đó.
    """
    result = {}
    for courses, days in timetable:
        result.setdefault(days, []).append(courses)

    for days, courses in result.items():
        courses.sort()

    return result