# Morse Code Translator

This program allows you to translate text into Morse code and generate an accompanying MP3 audio file.

## Description

The Morse Code Translator is a simple graphical user interface (GUI) application built using the Tkinter library in Python. It provides a convenient way to translate text into Morse code and generate an MP3 file representing the translated message.

The program uses the PyDub library to handle audio processing and file operations. It includes a dictionary (all_chars) that maps each character to its corresponding Morse code representation.
## Features

- Text-to-Morse code translation: Enter the text you want to translate into the input area.
- Translation display: The translated Morse code will be displayed in the output area.
- MP3 generation: Click the "GENERATE MP3" button to save the translated Morse code as an MP3 audio file.
- File selection: The program allows you to choose the location and name of the output MP3 file using a file dialog.

## Usage

1. Run the program.
2. Enter the text you want to translate into the "Text to Translate" input area.
3. Click the "TRANSLATE" button to see the translated Morse code in the "Translation" output area.
4. If desired, click the "GENERATE MP3" button to save the translated Morse code as an MP3 file.
   - A file dialog will open, allowing you to choose the output location and name for the MP3 file.
   - If you cancel the file dialog, no MP3 file will be generated.

Please note that characters not present in the Morse code dictionary (all_chars) will be skipped during translation, and a warning message will be displayed in the output area.

## Requirements

- Python 3.x
- PyDub library
- Tkinter library

## Contact
Created by [@DrPatroleum](https://github.com/DrPatroleum) - feel free to contact me!
