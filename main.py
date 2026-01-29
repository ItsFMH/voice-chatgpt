from openai import OpenAI
import speech_recognition as sr
from gtts import gTTS
from langdetect import detect
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

AUDIO_INPUT = "audio/input.wav"
AUDIO_OUTPUT = "audio/output.mp3"

os.makedirs("audio", exist_ok=True)


def ouvir_microfone():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Fale algo...")
        audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)

    with open(AUDIO_INPUT, "wb") as f:
        f.write(audio.get_wav_data())

    return AUDIO_INPUT


def transcrever_e_traduzir_audio(audio_file):
    with open(audio_file, "rb") as f:
        translation = client.audio.translations.create(
            file=f,
            model="whisper-1"
        )
    return translation.text


def perguntar_chatgpt(texto):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Você é um assistente inteligente e prestativo."},
            {"role": "user", "content": texto}
        ]
    )
    return response.choices[0].message.content


def texto_para_voz(texto):
    idioma = detect(texto)
    tts = gTTS(text=texto, lang=idioma)
    tts.save(AUDIO_OUTPUT)

    if os.name == "nt":
        os.system(f"start {AUDIO_OUTPUT}")
    else:
        os.system(f"mpg123 {AUDIO_OUTPUT}")


def main():
    audio = ouvir_microfone()

    texto_traduzido = transcrever_e_traduzir_audio(audio)
    print(f"📝 Texto transcrito e traduzido: {texto_traduzido}")

    resposta = perguntar_chatgpt(texto_traduzido)
    print(f"🤖 ChatGPT: {resposta}")

    texto_para_voz(resposta)


if __name__ == "__main__":
    main()