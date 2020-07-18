# Voice-Synthesis-Project
Using the tutorial made by AR compware, Written by Alex I. Ramirez @alexram1313 (arcompware.com) A voice synthesis model that collects wave files, concatenates them (depending on user input) and plays them back.

Main code: 
1) Reads the Carnegie Mellon University pronouncing dictionary
2) Loads the wave sample
3) Compares user input for words in dictionary
4) Outputs audio according to input

**In the "_play_audio" function I edited the data being added to the stream. 
**I wanted there to be a delay between all audio samples, as the audio seemed to output too quick.
