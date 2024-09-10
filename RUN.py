import googlemaps
import folium
from datetime import datetime
import os

# Initialize the Google Maps client with your API key
API_KEY = 'BLANK'
gmaps = googlemaps.Client(key=API_KEY)

stations = {
    "Green B Line": [
        "Green B Line Boston College Station, MA",
        "Green B Line South Street Station, MA",
        "Green B Line Chestnut Hill Avenue Station, MA",
        "Green B Line Chiswick Road Station, MA",
        "Green B Line Sutherland Road Station, MA",
        "Green B Line Washington Street Station, MA",
        "Green B Line Warren Street Station, MA",
        "Green B Line Allston Street Station, MA",
        "Green B Line Griggs Street Station, MA",
        "Green B Line Harvard Avenue Station, MA",
        "Green B Line Packards Corner Station, MA",
        "Green B Line Babcock Street Station, MA",
        "Green B Line Amory Street Station, MA",
        "Green B Line Boston University Central Station, MA",
        "Green B Line Boston University East Station, MA",
        "Green B Line Blandford Street Station, MA",
        "Green B Line Kenmore Station, MA",
        "Green B Line Hynes Convention Center Station, MA",
        "Green B Line Copley Station, MA",
        "Green B Line Arlington Station, MA",
        "Green B Line Boylston Station, MA",
        "Green B Line Park Street Station Boston, MA",
        "Green B Line Boston Government Center Station, MA"
    ],
    "Green C Line": [
        "Green C Line Cleveland Circle Station, MA",
        "Green C Line Englewood Avenue Station, MA",
        "Green C Line Dean Road Station, MA",
        "Green C Line Tappan Street Station, MA",
        "Green C Line Washington Square Station, MA",
        "Green C Line Fairbanks Street Station, MA",
        "Green C Line Brandon Hall Station, MA",
        "Green C Line Summit Avenue Station, MA",
        "Green C Line Coolidge Corner Station, MA",
        "Green C Line Saint Paul Street Station, MA",
        "Green C Line Kent Street Station, MA",
        "Green C Line Hawes Street Station, MA",
        "Green C Line Saint Mary’s Street Station, MA",
        "Green C Line Kenmore Station, MA",
        "Green C Line Hynes Convention Center Station, MA",
        "Green C Line Copley Station, MA",
        "Green C Line Arlington Station, MA",
        "Green C Line Boylston Station, MA",
        "Green C Line Park Street Station, MA",
        "Green C Line Boston Government Center Station, MA"
    ],
    "Green D Line": [
        "Green D Line Riverside Station, MA",
        "Green D Line Woodland Station, MA",
        "Green D Line Waban Station, MA",
        "Green D Line Eliot Station, MA",
        "Green D Line Newton Highlands Station, MA",
        "Green D Line Newton Centre Station, MA",
        "Green D Line Chestnut Hill Station, MA",
        "Green D Line Reservoir Station, MA",
        "Green D Line Beaconsfield Station, MA",
        "Green D Line Brookline Hills Station, MA",
        "Green D Line Brookline Village Station, MA",
        "Green D Line Longwood Station, MA",
        "Green D Line Fenway Station, MA",
        "Green D Line Kenmore Station, MA",
        "Green D Line Hynes Convention Center Station, MA",
        "Green D Line Copley Station, MA",
        "Green D Line Arlington Station, MA",
        "Green D Line Boylston Station, MA",
        "Green D Line Park Street Station, MA",
        "Green D Line Boston Government Center Station, MA",
        "Green D Line Haymarket Station, MA",
        "Green D Line North Station, MA",
        "Green D Line Science Park/West End Station, MA",
        "Green D Line Lechmere Station, MA",
        "Green D Line Union Square Station, MA"
    ],
    "Green E Line": [
        "Green E Line Heath Street Station, MA",
        "Green E Line Back of the Hill Station, MA",
        "Green E Line Riverway Station, MA",
        "Green E Line Mission Park Station, MA",
        "Green E Line Fenwood Road Station, MA",
        "Green E Line Brigham Circle Station, MA",
        "Green E Line Longwood Medical Area Station, MA",
        "Green E Line Museum of Fine Arts Station, MA",
        "Green E Line Northeastern University Station, MA",
        "Green E Line Symphony Station, MA",
        "Green E Line Prudential Station, MA",
        "Green E Line Massachusetts Avenue Station, MA",
        "Green E Line Symphony Station, MA",
        "Green E Line Hynes Convention Center Station, MA",
        "Green E Line Copley Station, MA",
        "Green E Line Arlington Station, MA",
        "Green E Line Boylston Station, MA",
        "Green E Line Park Street Station, MA",
        "Green E Line Boston Government Center Station, MA",
        "Green E Line Haymarket Station, MA",
        "Green E Line North Station, MA",
        "Green E Line Science Park/West End Station, MA",
        "Green E Line Lechmere Station, MA",
        "Green E Line East Somerville Station, MA",
        "Green E Line Gilman Square Station, MA",
        "Green E Line Magoun Square Station, MA",
        "Green E Line Ball Square Station, MA",
        "Green E Line Medford/Tufts Station, MA"
    ],
    "Orange Line": [
        "Orange Line Forest Hills Station, MA",
        "Orange Line Green Street Station, MA",
        "Orange Line Stony Brook Station, MA",
        "Orange Line Jackson Square Station, MA",
        "Orange Line Roxbury Crossing Station, MA",
        "Orange Line Ruggles Station, MA",
        "Orange Line Massachusetts Avenue Station, MA",
        "Orange Line Back Bay Station, MA",
        "Orange Line Tufts Medical Center Station, MA",
        "Orange Line Chinatown Station, MA",
        "Orange Line Downtown Crossing Station, MA",
        "Orange Line State Street Station, MA",
        "Orange Line Haymarket Station, MA",
        "Orange Line North Station, MA",
        "Orange Line Community College Station, MA",
        "Orange Line Sullivan Square Station, MA",
        "Orange Line Assembly Station, MA",
        "Orange Line Wellington Station, MA",
        "Orange Line Malden Center Station, MA",
        "Orange Line Oak Grove Station, MA"
    ],
     "Mattapan Line": [
        "Mattapan Line Red Line Ashmont Station, Boston, MA",
        "Mattapan Line Cedar Grove Station, Boston, MA",
        "Mattapan Line Butler Station, Boston, MA",
        "Mattapan Line Milton Station, Milton, MA",
        "Mattapan Line Central Avenue Station, Milton, MA",
        "Mattapan Line Valley Road Station, Milton, MA",
        "Mattapan Line Capen Street Station, Milton, MA",
    ],
    "Red Line": [
        "Red Line Alewife Station, MA",
        "Red Line Davis Station, MA",
        "Red Line Porter Station, MA",
        "Red Line Harvard Station, MA",
        "Red Line Central Station, MA",
        "Red Line Kendall/MIT Station, MA",
        "Red Line Park Street Station, MA",
        "Red Line Downtown Crossing Station, MA",
        "Red Line South Station Boston, MA",
        "Red Line Broadway Station, MA",
        "Red Line Andrew Station, MA",
        "Red Line JFK/UMass Station, MA",
        "Red Line Fields Corner Station, MA",
        "Red Line Shawmut Station, MA",
        "Red Line Ashmont Station, MA",
        "Red Line Shawmut Station, MA",
        "Red Line Fields Corner Station, MA",
        "Red Line North Quincy Station, MA",
        "Red Line Wollaston Station, MA",
        "Red Line Quincy Center Station, MA",
        "Red Line Quincy Adams Station, MA",
        "Red Line Braintree Station, MA"
    ],
    "Blue Line Part 2": [
        "Blue Line Aquarium Station, Boston, MA",
        "Blue Line State Street Station, Boston, MA",
        "Blue Line Government Center Station, Boston, MA",
        "Blue Line Bowdoin Station, Boston, MA"
    ],
     "Blue Line": [
        "Blue Line Wonderland Station, MA",
        "Blue Line Revere Beach Station, MA",
        "Blue Line Beachmont Station, MA",
        "Blue Line Suffolk Downs Station, MA",
        "Blue Line Orient Heights Station Boston, MA",
        "Blue Line Wood Island Station, MA",
        "Blue Line Airport Station, MA",
        "Blue Line Maverick Station, MA"
    ]
}

# Function to get geocoded coordinates for a place name
def get_coordinates(place):
    geocode_result = gmaps.geocode(place)
    if geocode_result:
        location = geocode_result[0]['geometry']['location']
        return (location['lat'], location['lng'])
    return None

# Function to get walking distance between two coordinates
def get_walking_distance(coord1, coord2):
    result = gmaps.distance_matrix(coord1, coord2, mode="walking", departure_time=datetime.now())
    distance = result['rows'][0]['elements'][0]['distance']['value']  # distance in meters
    return distance / 1000  # convert to kilometers

# Function to get walking route between two coordinates
def get_walking_route(coord1, coord2):
    directions_result = gmaps.directions(coord1, coord2, mode="walking", departure_time=datetime.now())
    route = []
    if directions_result:
        for step in directions_result[0]['legs'][0]['steps']:
            start_location = step['start_location']
            end_location = step['end_location']
            route.append((start_location['lat'], start_location['lng']))
            route.append((end_location['lat'], end_location['lng']))
    return route

# Calculate total distance for each line and create maps with routes
total_distances = {}
maps = {}
for line, places in stations.items():
    total_distance = 0
    coords = [get_coordinates(place) for place in places]
    coords = [coord for coord in coords if coord]  # Filter out None values
    # Create a map centered at the first station of the line
    if coords:
        maps[line] = folium.Map(location=coords[0], zoom_start=13)
        for i in range(len(coords) - 1):
            coord1 = coords[i]
            coord2 = coords[i + 1]
            total_distance += get_walking_distance(coord1, coord2)
            route = get_walking_route(coord1, coord2)
            if route:
                folium.PolyLine(locations=route, color='blue').add_to(maps[line])
        total_distances[line] = total_distance

# Output the distances
for line, distance in total_distances.items():
    print(f"Total running distance for {line}: {distance:.2f} km")

# Save the maps
for line, folium_map in maps.items():
    folium_map.save(f"{line.replace(' ', '_')}_route_map.html")

print("Maps with routes have been created and saved.")