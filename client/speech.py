import speech_recognition as sr
import pyttsx3 as tts
import json
import os

class SpeechPatternRecognizer():

    def __init__(self):

        # getting settings from file or creating it if none 
        try:
            with open("settings.json") as f:
                self.settings = json.load(f)
        except Exception:
            self.settings = {'speech_speed': 170, 'voice_number': 0, 'music_folder': ''}
            with open('settings.json', 'w') as f:
                    json.dump(self.settings, f)

        if os.name == "posix" :
            self.settings["voice_number"] = 33

        # init text to speech engine with specified settings
        self.speaker = tts.init()
        voices = self.speaker.getProperty('voices')
        self.speaker.setProperty('voice', voices[self.settings['voice_number']].id)
        self.speaker.setProperty('rate', self.settings["speech_speed"])

        # init speech recognizer engine with google
        self.recognizer = sr.Recognizer()

    def speak(self, text):
        self.speaker.say(text)
        self.speaker.runAndWait()
        

    def listen(self, stealthMode = False):

        while True:
            try:
                with sr.Microphone() as mic:
                    self.recognizer.adjust_for_ambient_noise(mic)
                    audio = self.recognizer.listen(mic)

                    text = self.recognizer.recognize_google(audio)
                    text = text.lower()

                    return text
            except sr.UnknownValueError:
                if stealthMode:
                    continue
                else:
                    self.speak("Sorry didn't get that, try again")
            except Exception as e:
                self.speak("internal speech error")
                print(e)

    def waitForWakeupCall(self, text):

        while True:
            audio = self.listen(stealthMode=True)

            if audio.find(text) >= 0:
                self.speak("hey there")
                break
            else:
                continue

    def confirmCommand(self, text = "are you sure you want to confirm your last command"):
        self.speak(text)
        confirmation = self.listen()
        if confirmation.find("yes") >= 0:
            return True
        else:
            return False

