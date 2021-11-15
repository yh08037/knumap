from gtts import gTTS
from playsound import playsound


def save_tts(text, save_path):
    tts = gTTS(text=text, lang='ko')
    tts.save(save_path)


if __name__ == '__main__':
    text = '안녕하세요 저희는 융합 창업 캡스톤 디자인의 4조입니다.'
    path = 'src/hello.mp3'
    save_tts(text, path)
    playsound(path)
