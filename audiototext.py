import speech_recognition as sr
# initialize the recognizer
r = sr.Recognizer()

with sr.Microphone() as source:
    # read the audio data from the default microphone
    audio_data = r.record(source, duration=5)
    print("Recognizing...")
    # convert speech to text
    # text = r.recognize_google(audio_data)
    # text = r.recognize_google(audio_data, language="es-ES")
    text = r.recognize_google(audio_data, language='en-IN', show_all=True)
    print("I thinks you said '" + r.recognize_google(audio_data) + "'")
    print(text)