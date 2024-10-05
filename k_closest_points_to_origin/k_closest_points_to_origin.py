from typing import List, Tuple

import math

def k_closest_points_to_origin(points: List[Tuple[int, int]], k: int) -> List[Tuple[int, int]]:
    return sorted(points, key=lambda p: math.sqrt(p[0] ** 2 + p[1] ** 2))[:k]
