import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
import speech_recognition as sr
from deep_translator import GoogleTranslator
duration = 5  # segundos de gravação
sample_rate = 44100

import random

facil = {"gato":"cat",
         "cachorro":"dog",
         "carro":'car'
}

medio = {"escola":"school",
         "amigo":"friend",
         "computador":"computer"}

dificil = {"comfortavel":"confortable",
           "filha":"daughter",
           "literalmente":"literally"
}

print(" JOGO DE PRONUNCIA")
print("1 = facil")
print("2 = medio")
print("3 = dificil")

dificuldade = input("escolha a dificuldade:")

if dificuldade == "1":
    palavras = facil
elif dificuldade == "2":
    palavras = medio
elif dificuldade == "3":
    palavras = dificil
else:
    print("opção invalida")
    palavras = facil

palavra = random.choice(list(palavras.keys()))

print()
print('como vc acha que se pronuncia:')
print(palavra)

print("Fale agora...")
recording = sd.rec(
  int(duration * sample_rate), # o número de amostras a serem registradas
  samplerate=sample_rate,      # taxa de amostras
  channels=1,                  # 1 significa gravação mono
  dtype="int16")               # tipo de dados para as amostras registradas
sd.wait()  # aguardando o término da gravação

wav.write("output.wav", sample_rate, recording)
print("Gravação concluída, estou reconhecendo...")


recognizer = sr.Recognizer()
with sr.AudioFile("output.wav") as source:
    audio = recognizer.record(source)

try:
    text = recognizer.recognize_google(audio, language="en-UK")
    print("Você disse:", text)

except sr.UnknownValueError:             # - se o Google não conseguiu entender a fala devido a ruídos ou silêncio
    print("A fala não pôde ser reconhecida.")
except sr.RequestError as e:             # - se não houver conexão com a Internet ou a API estiver indisponível
    print(f"Service error: {e}")


print(f"o coreto é:{palavras[palavra]}")

if text == palavras[palavra]:
    print("congrats!")

else:
    print("vc agora tem uma dividada com o duolingo!")