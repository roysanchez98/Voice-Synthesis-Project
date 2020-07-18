# Name: Roy Sanchez
# Date: 7/5/2020
# Description: This is a test of some code and
# recording that implement text to speech.
# OG code by Alex T. Ramirez


import re
# A regular expression is a special sequence
# of characters that helps you match or find
# other strings or sets of strings, using a
# specialized syntax held in a pattern.
import wave # read and write wave files
import pyaudio
import _thread
import time

# simply modify the value for the 'rate' parameter to change the playback speed
# <1 === slow down;  >1 === speed up
FRAMERATE_OFFSET =  int(1)

class TextToSpeech: # Creating a class

    CHUNK = 1024 # (arbitrarily chosen) number of frames the signals are split into.
    # chunk is like a buffer (each buffer will contain 1024 samples, which you can keep or throw away)
    # This allows for multiple steams of "some" data.
    # In this program we are not expecting a constant stream of audio. (We are expecting lots of small recordings of audio) This allows us to story into an array or a list

    def __init__(self, words_pron_dict:str = 'cmudict-0.7b.txt'): # constructor which its argument is a str which is = to the .txt file
        self._l = {} # empty dictionary
        self._load_words(words_pron_dict) # pointing to itself(arguemnt)

    def _load_words(self, words_pron_dict:str):
        with open(words_pron_dict, 'r') as file: # reading the file
            for line in file: # read each line in the file
                if not line.startswith(';;;'):
                    key, val = line.split('  ', 2) # split every 2 into space
                    self._l[key] = re.findall(r"[A-Z]+", val) #find all elements in key

    def get_pronunciation(self, str_input):
        list_pron = [] #empty list
        for word in re.findall(r"[\w']+", str_input.upper()): #regular expression: text string to describe a search pattern. Searching for the letter 'r' else its not identified.
            if word in self._l: # checking if this word is in our dictionary
                list_pron += self._l[word] #insert word into list
        print(list_pron)
        delay = 0
        for pron in list_pron: # for elements within list_pron
            _thread.start_new_thread(TextToSpeech._play_audio, (pron, delay,)) # creates a thread. Method call returns immediately and the child thread starts and calls function with the passed list of args. when function returns, the thread terminates.
            delay += 0.145

    def _play_audio(sound, delay):
        try:
            
            RECORD_SECONDS = 2
            
            time.sleep(delay)
            wf = wave.open("sounds/" + sound + ".wav", 'rb')
            p = pyaudio.PyAudio()
            stream = p.open(format = p.get_format_from_width(wf.getsampwidth()), #open file and returns sample width in bytes (to play audio)
            channels=wf.getnchannels(), rate=wf.getframerate(), output = True)
                       
            
            data = wf.readframes(TextToSpeech.CHUNK) # readframes: reads and returns at most n frames of audio, as a string of bytes (Which we have in our chunk)

            while data:
                stream.write(data * RECORD_SECONDS)
                data = wf.readframes(TextToSpeech.CHUNK)
                
            stream.stop_stream #pause playing or recording
            stream.close() # stop stream

            p.terminate() # exit program
            return
        except:
            pass


if __name__ == '__main__':
    tts = TextToSpeech()
    while True: # while you still get user input
        tts.get_pronunciation(input('Enter a word or phrase: '))
            
