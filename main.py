# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from geo_match import find_closest_matches

def main():
    # Sample data
    locations1 = [
        (40.7128, -74.0060),  # New York
        (34.0522, -118.2437), # Los Angeles
        (51.5074, -0.1278),   # London
    ]
    
    locations2 = [
        (40.7589, -73.9851),  # Near New York
        (34.0407, -118.2468), # Near Los Angeles
        (51.5072, -0.1276),   # Near London
        (48.8566, 2.3522),    # Paris
    ]
    
    # Find closest matches
    matches = find_closest_matches(locations1, locations2)
    
    # Print results
    print("Matching Results:")
    for loc1, loc2 in matches.items():
        print(f"Location 1 {loc1} matches to nearest Location 2 {loc2}")

if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
