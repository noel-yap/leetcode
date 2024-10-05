from typing import List


def insert_interval(intervals: List[List[int]], interval: List[int]):
    result = []

    i = 0
    while i < len(intervals):
        if interval[1] < intervals[i][0]:
            result.append(interval)
            result.extend(intervals[i:])

            return result
        elif intervals[i][0] <= interval[1] <= intervals[i][1]:
            result.append([min(interval[0], intervals[i][0]), intervals[i][1]])
            if i + 1 < len(intervals):
                result.extend(intervals[i + 1:])

            return result
        elif interval[0] < intervals[i][0] or intervals[i][0] <= interval[0] <= intervals[i][1]:
            j = i + 1
            while j < len(intervals):
                if interval[1] < intervals[j][0]:
                    result.append([min(interval[0], intervals[i][0]), interval[1]])
                    result.extend(intervals[j:])

                    return result
                elif intervals[j][0] <= interval[1] <= intervals[j][1]:
                    result.append([min(interval[0], intervals[i][0]), intervals[j][1]])
                    if j + 1 < len(intervals):
                        result.extend(intervals[j + 1:])

                    return result

                j += 1
            else:
                try:
                    result.append([min(interval[0], intervals[i][0]), intervals[j][1]])
                except IndexError:
                    result.append([min(interval[0], intervals[i][0]), interval[1]])

                return result
        else:
            result.append(intervals[i])

        i += 1
    else:
        result.append(interval)

    return result
