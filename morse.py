from pydub import AudioSegment
import tkinter as tk
from tkinter import filedialog
import os

all_chars = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-',
    'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--',
    'X': '-..-', 'Y': '-.--', 'Z': '--..', 'Ą': '.-.-', 'Ć': '-.-..', 'Ę': '..-..', 'Ł': '.-..-', 'Ń': '--.--', 'Ó': '---.', 'Ś': '...-...', 'Ź': '--..-.', 'Ż': '--..-',
    'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---', 'k': '-.-',
    'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--',
    'x': '-..-', 'y': '-.--', 'z': '--..', 'ą': '.-.-', 'ć': '-.-..', 'ę': '..-..', 'ł': '.-..-', 'ń': '--.--', 'ó': '---.', 'ś': '...-...', 'ź': '--..-.', 'ż': '--..-',
    '.': '.-.-.-', ',': '--..--', '?': '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-', '@': '.--.-.',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', ' ': '/'
}

def make_mp3_translation():
    global translated
    program_path = os.path.dirname(os.path.abspath(__file__))
    dit_path = os.path.join(program_path, "dit.mp3")
    dah_path = os.path.join(program_path, "dah.mp3")

    dit = AudioSegment.from_mp3(dit_path)
    dah = AudioSegment.from_mp3(dah_path)
    half_sec_silence = AudioSegment.silent(duration=500)
    
    mp3 = {".": dit, "-": dah, "/": half_sec_silence}
    cos = ''.join(lista)
    test = []
    test[:0] = cos
    lista2 = []
    for i in range(len(cos)):
        lista2.append(mp3[cos[i]])
    translated = sum(lista2)
    
    output_path = filedialog.asksaveasfilename(defaultextension=".mp3", filetypes=(("MP3 files", "*.mp3"), ("All files", "*.*")))
    if output_path:
        translated.export(output_path, format="mp3")

def translate():
    global lista
    text_to_translate = input_text.get("1.0", "end-1c")
    lista = []
    try:
        for i in range(len(text_to_translate)):
            lista.append(all_chars[text_to_translate[i]])
            output_text.delete("1.0", "end")
            output_text.insert("end", ''.join(lista))
    except KeyError:
        output_text.delete("1.0", "end")
        output_text.insert("end", "You entered a character(s) that cannot be translated.")

def translate_and_generate_mp3():
    translate()
    make_mp3_translation()
    output_text.delete("1.0", "end")
    output_text.insert("end", ''.join(lista))

# GUI initialization
window = tk.Tk()
window.title("Morse Code Translator")

input_label = tk.Label(window, text="Text to Translate:")
input_label.pack(padx=5, pady=5)

input_text = tk.Text(window, height=4)
input_text.pack(padx=5, pady=5)

translate_button = tk.Button(window, text="TRANSLATE", command=translate)
translate_button.pack(padx=5, pady=5)

output_label = tk.Label(window, text="Translation:")
output_label.pack(padx=5, pady=5)

output_text = tk.Text(window, height=4)
output_text.pack(padx=5, pady=5)

generate_button = tk.Button(window, text="GENERATE MP3", command=make_mp3_translation)
generate_button.pack(padx=5, pady=5)

window.mainloop()
