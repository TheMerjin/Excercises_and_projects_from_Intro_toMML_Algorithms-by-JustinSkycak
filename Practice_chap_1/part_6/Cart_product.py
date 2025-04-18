"""Excercises part 6 Intoro to MML Justin Skycak"""
import copy

def calc_cartesian_product(ranges):
    points = [[]]
    
    for r in ranges:
        extended_points = []
        for point in points:
            for item in r :
                new_point = list(point)
                new_point.append(item)
                extended_points.append(new_point)
        points = extended_points
    return points
        
                

    
    return points, copy_points

anges = [
 ['a'],
 [1, 2, 3], ["Y", "Z"]
 ]
print(calc_cartesian_product(anges))