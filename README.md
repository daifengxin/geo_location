# Geo Location Matcher

A simple and efficient Python module for matching points from one set of geographic locations to their closest counterparts in another set.

## Usage

```python
from geo_match import find_closest_matches

# Prepare two sets of coordinates (format: (latitude, longitude))
locations1 = [
    (40.7128, -74.0060),  # New York
    (34.0522, -118.2437), # Los Angeles
]

locations2 = [
    (40.7589, -73.9851),  # Target location 1
    (34.0407, -118.2468), # Target location 2
]

# Find closest matches
matches = find_closest_matches(locations1, locations2)

# Process results
for source_point, matched_point in matches.items():
    print(f"Source location {source_point} matches to target location {matched_point}")
```

## API Reference

### find_closest_matches(points1, points2)

Finds the closest point in the second array for each point in the first array.

Parameters:
- points1: List[Tuple[float, float]] - First array of coordinates
- points2: List[Tuple[float, float]] - Second array of coordinates

Returns:
- Dict[Tuple[float, float], Tuple[float, float]] - Dictionary with matches

### haversine_distance(lat1, lon1, lat2, lon2)

Calculates the distance between two GPS coordinates (in kilometers).

Parameters:
- lat1, lon1: float - Latitude and longitude of the first point
- lat2, lon2: float - Latitude and longitude of the second point

Returns:
- float - Distance between points in kilometers

## Running Tests

```bash
python -m unittest test_geo_match.py
```
