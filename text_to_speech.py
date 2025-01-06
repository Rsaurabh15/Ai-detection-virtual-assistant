import pyttsx3

# Initialize the TTS engine once
engine = pyttsx3.init()

def text_to_speech(text):
    """
    Converts text to speech.
    Args:
        text (str): The text to be spoken.
    """
    try:
        # Set speech rate
        rate = engine.getProperty('rate')
        engine.setProperty('rate', rate - 70)  # Reduce the rate for slower speech
        
        # Speak the text
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print(f"An error occurred during text-to-speech conversion: {str(e)}")

# Example usage
text_to_speech(" How can I assist you today?")

