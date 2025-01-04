import tkinter as tk
from tkinter import messagebox
from elevenlabs import play
from elevenlabs.client import ElevenLabs
from langdetect import detect, DetectorFactory

# Zabezpieczenie dla powtarzalności wyników langdetect
DetectorFactory.seed = 0

# Klucz API dla ElevenLabs
API_KEY = "twoj unikalny klucz - prosze zostaw go do sprawdzenia zadania"

# Inicjalizacja klienta ElevenLabs
client = ElevenLabs(api_key=API_KEY)

# Funkcja do rozpoznawania języka
def detect_language():
    pass # zamień na twój kod

# Funkcja do generowania i odtwarzania dźwięku
def play_audio():
    pass # zamień na twój kod
    

# Tworzenie GUI
root = tk.Tk()
root.title("Generowanie audio z ElevenLabs")
root.geometry("500x350")

# Etykieta wyboru języka
language_label = tk.Label(root, text="Wpisz tekst:")
language_label.pack(pady=5)

# Pole tekstowe
text_entry = tk.Text(root, height=10, width=50)
text_entry.pack(pady=5)

# Ramka do wyświetlania rozpoznanego języka
detected_language_frame = tk.Frame(root)
detected_language_frame.pack(pady=10)

detected_language_label = tk.Label(detected_language_frame, text="Rozpoznany język: --", fg="blue")
detected_language_label.pack()

# Przycisk do rozpoznawania języka
detect_button = tk.Button(root, text="Rozpoznaj język", command=detect_language)
detect_button.pack(pady=5)

# Przycisk odtwarzania audio
play_button = tk.Button(root, text="Odtwórz audio", command=play_audio)
play_button.pack(pady=5)

# Uruchomienie aplikacji
root.mainloop()
