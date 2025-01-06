import text_to_speech
import datetime
import webbrowser
import weather


def speak_and_return(response):
    """Speak and return the response."""
    text_to_speech.text_to_speech(response)
    return response


def open_website(url, name):
    """Open a website and return a response."""
    try:
        webbrowser.open(url)
        return speak_and_return(f"{name} is now ready for you.")
    except Exception as e:
        return speak_and_return(f"Failed to open {name}. Error: {str(e)}")


def action(data):
    user_data = data.strip().lower()  # Normalize and clean input

    if "what is your name" in user_data:
        return speak_and_return("My name is Virtual Assistant.")

    elif any(greeting in user_data for greeting in ["hello", "hii", "hi"]):
        return speak_and_return("Hey, sir. How can I help you?")

    elif "good morning" in user_data:
        return speak_and_return("Good morning, sir.")

    elif "time now" in user_data or "what time is it" in user_data:
        current_time = datetime.datetime.now()
        time_response = f"The current time is {current_time.hour} Hour and {current_time.minute} Minute."
        return speak_and_return(time_response)

    elif "shutdown" in user_data:
        return speak_and_return("Okay, sir. Shutting down.")

    elif "play music" in user_data:
        return open_website("https://open.spotify.com/", "Spotify")

    elif "youtube" in user_data:
        return open_website("https://www.youtube.com/", "YouTube")

    elif "open google" in user_data or "google" in user_data:
        return open_website("https://www.google.com/", "Google")

    elif "weather" in user_data:
        try:
            weather_info = weather.Weather()  # Ensure this function exists and works as intended
            return speak_and_return(weather_info)
        except Exception as e:
            return speak_and_return(f"Failed to fetch weather information. Error: {str(e)}")

    else:
        return speak_and_return("I am not able to understand.")
