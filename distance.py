def distance(query1: str,query2: str):
    """
    Determines distance in kilometers between two places.

    Args:
        query1 (str): The name of the first location.
        query2 (str): The name of the second location.

    Returns:
        str: A single paragraph containing the distance between two locations in kilometers.
    """
    from geopy.geocoders import Nominatim
    from geopy.distance import geodesic
    
    geolocator = Nominatim(user_agent="distance_calculator")
    
    location1 = query1
    location2 = query2
    
    try:
        loc1 = geolocator.geocode(location1)
        loc2 = geolocator.geocode(location2)
    
        if loc1 and loc2:
            distance = geodesic((loc1.latitude, loc1.longitude), (loc2.latitude, loc2.longitude)).km
            return(f"The distance between {location1} and {location2} is {distance:.2f} kilometers.")
        else:
            return("Could not find one or both locations.")
    
    except Exception as e:
        return(f"An error occurred: {e}")

