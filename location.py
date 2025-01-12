def location():
    """
    gets the user location

    Returns:
        str: The location of the user.
    """
    import requests
    from ip2geotools.databases.noncommercial import DbIpCity
    
    def printDetails(ip):
        res = DbIpCity.get(ip, api_key="free")
        return(f"Location: {res.city}, {res.region}, {res.country}")
     
    def get_public_ip(): 
            response = requests.get('https://api.ipify.org') 
            return response.text 
     
    public_ip = get_public_ip() 
    
    return(printDetails(public_ip))