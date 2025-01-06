from requests_html import HTMLSession

def Weather(location="prayagraj"):
    """
    Fetch weather information for the specified location using Google's weather data.
    Args:
        location (str): The name of the location to fetch weather for.
    Returns:
        str: Weather details including temperature, unit, and description, or an error message.
    """
    try:
        # Initialize session and prepare URL
        s = HTMLSession()
        url = f'https://www.google.com/search?q=weather+{location}'
        
        # Custom headers to mimic a browser request
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
        }
        
        # Send the request
        r = s.get(url, headers=headers)
        
        # Extract weather details
        temp_element = r.html.find('span#wob_tm', first=True)
        unit_element = r.html.find('div.vk_bk.wob-unit span.wob_t', first=True)
        desc_element = r.html.find('span#wob_dc', first=True)
        
        # Validate elements and extract text
        if temp_element and unit_element and desc_element:
            temp = temp_element.text
            unit = unit_element.text
            desc = desc_element.text
            return f"The current weather in {location.capitalize()} is {temp} {unit} with {desc}."
        else:
            return "Could not retrieve weather information. The structure of the webpage might have changed."
    except Exception as e:
        return f"An error occurred while fetching weather data: {str(e)}"

# Example usage
print(Weather("prayagraj"))

