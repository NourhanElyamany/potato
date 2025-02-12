from time import sleep
from numpy import min_scalar_type
import speech_recognition as sr
import pyttsx3 as tts
import os

class SpeechPatternRecognizer():

    def __init__(self):

        self.settings = {'speech_speed': 170, 'voice_number': 1, 'music_folder': ''}

        if os.name == "posix" :
            self.settings["voice_number"] = 33

        # init text to speech engine with specified settings
        self.speaker = tts.init()
        voices = self.speaker.getProperty('voices')
        self.speaker.setProperty('voice', voices[self.settings['voice_number']].id)
        self.speaker.setProperty('rate', self.settings["speech_speed"])

        # init speech recognizer engine with google
        self.recognizer = sr.Recognizer()
        self.recognizer.energy_threshold = 3000


    def speak(self, text):
        self.speaker.startLoop(False)
        self.speaker.say(text)
        
        self.speaker.iterate()
        while self.speaker.isBusy():
            sleep(0.3)
            
        self.speaker.endLoop()
        
            

    def listen(self, stealthMode = False):

        while True:
            try:
                with sr.Microphone() as mic:
                    print("mic")
                    self.recognizer.adjust_for_ambient_noise(mic, duration=0.1)
                    audio = self.recognizer.listen(mic)

                    text = self.recognizer.recognize_google(audio)
                    text = text.lower()
                    print(text)

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

