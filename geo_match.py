import math
from typing import List, Tuple, Dict

def haversine_distance(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """
    Calculate the distance between two GPS coordinates (in kilometers)
    using the Haversine formula for spherical distance
    """
    # Earth's mean radius (in kilometers)
    R = 6371.0

    # Convert latitude and longitude to radians
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])

    # Haversine formula
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.asin(math.sqrt(a))
    
    return R * c

def find_closest_matches(points1: List[Tuple[float, float]], 
                        points2: List[Tuple[float, float]]) -> Dict[Tuple[float, float], Tuple[float, float]]:
    """
    Find the closest point in the second array for each point in the first array
    
    Args:
        points1: First array of coordinates, each element is a tuple of (latitude, longitude)
        points2: Second array of coordinates, each element is a tuple of (latitude, longitude)
    
    Returns:
        Dictionary with points from points1 as keys and their closest matches from points2 as values
    """
    if not points1 or not points2:
        return {}
    
    matches = {}
    
    for p1 in points1:
        min_distance = float('inf')
        closest_point = None
        
        for p2 in points2:
            distance = haversine_distance(p1[0], p1[1], p2[0], p2[1])
            if distance < min_distance:
                min_distance = distance
                closest_point = p2
        
        matches[p1] = closest_point
    
    return matches
