import speech_recognition as sr

def speech_to_text():
    """
    Converts speech input to text using the microphone.
    Returns:
        str: The recognized speech as text.
    """
    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            # Inform the user that the system is ready
            print("Listening... Please speak now.")
            recognizer.adjust_for_ambient_noise(source)  # Adjust for background noise
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)

        # Attempt to recognize speech
        voice_data = recognizer.recognize_google(audio)
        print(f"You said: {voice_data}")
        return voice_data

    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio. Please try again.")
        return "Error: Could not understand the audio."

    except sr.RequestError as e:
        print(f"Could not process the request due to network issues. Error: {str(e)}")
        return "Error: Network issues."

    except sr.WaitTimeoutError:
        print("Listening timed out. Please try speaking again.")
        return "Error: Listening timed out."

    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
        return f"Error: {str(e)}"

# Example usage:
if __name__ == "__main__":
    print(speech_to_text())
