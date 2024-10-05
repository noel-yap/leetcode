from typing import List, Tuple


def get_adjacent_matching_cell_coordinates(grid: List[List[int]], coord: Tuple[int, int]) -> List[Tuple[int, int]]:
    result = []

    sr = coord[0]
    sc = coord[1]

    for coord in [
        (max(0, sr - 1), sc),
        (min(len(grid) - 1, sr + 1), sc),
        (sr, max(0, sc - 1)),
        (sr, min(len(grid[sr]) - 1, sc + 1))]:
        tr = coord[0]
        tc = coord[1]

        if grid[tr][tc] == grid[sr][sc] and coord not in result:
            result.append(coord)

    return result


def flood_fill(grid: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
    result = grid

    if grid[sr][sc] != color:
        coords = [(sr, sc)]

        i = 0
        while i < len(coords):
            tr = coords[i][0]
            tc = coords[i][1]

            for c in get_adjacent_matching_cell_coordinates(grid, (tr, tc)):
                if c not in coords:
                    coords.append(c)
            i += 1

        for c in coords:
            tr = c[0]
            tc = c[1]

            result[tr][tc] = color

    return result
