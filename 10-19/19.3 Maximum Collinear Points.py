from typing import List, Tuple
import math
from collections import defaultdict

def maximum_collinear_points(points: List[List[int]]) -> int:
    # call helper function for all points, to track the point with maxcollinear points
    # helper function requires, another helper for slope calculation of any two points, which requires gcd helper to avoid decimal precision issues
    res = 0
    for i in range(len(points)):
        res = max(res, max_collinear_pts_one_focal_point(i, points))
    return res
    
def max_collinear_pts_one_focal_point(focal_pt_idx: int, points: List[List[int]]) -> int:
    max_points = 0
    slopes_map = defaultdict(int)
    for j in range(len(points)):
        if j != focal_pt_idx:
            curr_slope = get_slope(points[j], points[focal_pt_idx])
            slopes_map[curr_slope] += 1
            max_points = max(max_points, slopes_map[curr_slope])
    
    return max_points + 1 # 1 for the focal point itself

def get_slope(p1: List[int], p2: List[int]) -> Tuple[int, int]:
    rise = p1[1] - p2[1]
    run = p1[0] - p2[0]

    # edge case, vertical slope, since div by 0 is undefined
    if run == 0:
        return (1, 0)
    
    # simplifying slope, making uniform by div by gcd
    gcd_val = gcd(rise, run)
    rise //= gcd_val
    run //= gcd_val

    # normalise signs, so (-1, -2) (1, 2) arenot treated differently
    if run < 0:
        rise = -rise
        run = -run
    
    return (rise, run)

def gcd(num1: int, num2: int):
    while num2 != 0:
        num1, num2 = num2, num1 % num2
    return num1