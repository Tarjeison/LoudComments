from gtts import gTTS
from playsound import playsound
import os


def tts_windows(word: str):
    # languages = ['no', 'fr', 'da', 'it', 'pl']
    # language = random.choice(languages)
    language = 'no'
    myobj = gTTS(text=word, lang=language, slow=False)
    myobj.save("comment.mp3")
    playsound("comment.mp3")
    os.remove("comment.mp3")


def tts_pi(word: str):
    language = 'no'
    myobj = gTTS(text=word, lang=language, slow=False)
    myobj.save("comment.mp3")
    os.system('mpg321 foo.mp3 &')
    os.remove("comment.mp3")


if __name__ == '__main__':
    tts_pi("Dette er en test")
