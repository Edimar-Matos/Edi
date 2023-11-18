import openai
import speech_recognition as sr
import pyttsx3
import requests
import webbrowser
from bs4 import BeautifulSoup

# Configurações da OpenAI GPT-3
openai.api_key = "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"
modelo_gpt3 = 'text-davinci-003'  # Ou outro modelo disponível

# Função para interagir com o modelo GPT-3
def gpt3_chat(prompt):
    response = openai.Completion.create(
        engine=modelo_gpt3,
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

# Função para reconhecimento de voz
def reconhecimento_de_voz():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Fale algo:")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        texto = recognizer.recognize_google(audio, language='pt-BR')
        print(f"Você disse: {texto}")
        return texto
    except sr.UnknownValueError:
        print("Não foi possível entender o áudio.")
        return ""
    except sr.RequestError as e:
        print(f"Erro no serviço de reconhecimento de voz: {e}")
        return ""

# Função para síntese de voz
def fala(texto):
    engine = pyttsx3.init()
    engine.say(texto)
    engine.runAndWait()

# Loop principal do chat
while True:
    # Reconhecimento de voz
    entrada_audio = reconhecimento_de_voz()

    # Verificar condição de parada
    if "obrigado" in entrada_audio.lower():
        print("Chat encerrado.")
        break 
    
    # Interagir com o modelo GPT-3
    resposta_gpt3 = gpt3_chat(entrada_audio)

    # Exibir resposta do modelo e falar
    print(f"Resposta GPT-3: {resposta_gpt3}")
    fala(resposta_gpt3)

