import tkinter as tk
import speech_recognition as sr
import pyttsx3


def encrypt(text, key):
    # Simple substitution cipher as a placeholder
    encrypted_text = ""
    for char in text:
        encrypted_text += chr(ord(char) + key)
    return encrypted_text


def decrypt(ciphertext, key):
    # Reverse the substitution cipher for decryption
    decrypted_text = ""
    for char in ciphertext:
        decrypted_text += chr(ord(char) - key)
    return decrypted_text


def play_audio_output():
    # Placeholder implementation for playing audio output
    pass


def encrypt_action():
    text = text_input.get()
    ciphertext = encrypt(text, key)
    text_output.insert(tk.END, f"Encrypted: {ciphertext}\n")


def decrypt_action():
    # Get the currently selected text
    selected_text = text_output.get(tk.SEL_FIRST, tk.SEL_LAST)
    if selected_text:
        plaintext = decrypt(selected_text, key)
        text_output.insert(tk.END, f"Decrypted: {plaintext}\n")
    else:
        text_output.insert(tk.END, "No text selected for decryption\n")


def stt_action():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        text_input.delete(0, tk.END)  # Clear existing text
        text_input.insert(tk.END, text)
        text_output.delete(1.0, tk.END)  # Clear existing output
        encrypt_action()  # Automatically encrypt after speech-to-text
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service: {e}")


def tts_action():
    text = text_input.get()
    engine.say(text)
    engine.runAndWait()


root = tk.Tk()
root.title("Encryption and Decryption with STT and TTS")

# Create input fields for text and audio data
text_input = tk.Entry(root)
text_input.pack()

audio_input = tk.Button(root, text="Record Audio Input", command=stt_action)
audio_input.pack()

# Create output fields for text and audio data
text_output = tk.Text(root, height=10, width=50)
text_output.pack()

audio_output = tk.Button(root, text="Play Audio Output", command=tts_action)
audio_output.pack()

# Create buttons for encryption, decryption, STT, and TTS functionalities
encrypt_button = tk.Button(root, text="Encrypt", command=encrypt_action)
encrypt_button.pack()

decrypt_button = tk.Button(root, text="Decrypt", command=decrypt_action)
decrypt_button.pack()

# Initialize STT recognizer
recognizer = sr.Recognizer()

# Initialize TTS engine
engine = pyttsx3.init()

# Define or generate a key for encryption and decryption
key = 3  # add secret key 

root.mainloop()
