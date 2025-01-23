import unittest
from geo_match import haversine_distance, find_closest_matches

class TestGeoMatch(unittest.TestCase):
    def test_haversine_distance(self):
        # Test distance between two known points
        # Beijing (39.9042° N, 116.4074° E) to Shanghai (31.2304° N, 121.4737° E)
        distance = haversine_distance(39.9042, 116.4074, 31.2304, 121.4737)
        self.assertAlmostEqual(distance, 1067.0, delta=1.0)  # Allow 1km error margin
        
        # Test distance between same point
        self.assertEqual(haversine_distance(0, 0, 0, 0), 0)
    
    def test_find_closest_matches(self):
        points1 = [
            (40.7128, -74.0060),  # New York
            (34.0522, -118.2437), # Los Angeles
        ]
        
        points2 = [
            (40.7589, -73.9851),  # Near New York
            (34.0407, -118.2468), # Near Los Angeles
            (41.8781, -87.6298),  # Chicago
        ]
        
        matches = find_closest_matches(points1, points2)
        
        # Verify New York matches to nearest point
        self.assertEqual(matches[(40.7128, -74.0060)], (40.7589, -73.9851))
        
        # Verify Los Angeles matches to nearest point
        self.assertEqual(matches[(34.0522, -118.2437)], (34.0407, -118.2468))
    
    def test_empty_inputs(self):
        # Test empty inputs
        self.assertEqual(find_closest_matches([], []), {})
        self.assertEqual(find_closest_matches([(0, 0)], []), {})
        self.assertEqual(find_closest_matches([], [(0, 0)]), {})

if __name__ == '__main__':
    unittest.main()
