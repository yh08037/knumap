from google.cloud import texttospeech


class GoogleCloudTTS:
    def __init__(self) -> None:
        self.client = texttospeech.TextToSpeechClient()
        self.voice = texttospeech.VoiceSelectionParams(
            language_code='ko-KR',
            ssml_gender=texttospeech.SsmlVoiceGender.FEMALE
        )
        self.config = texttospeech.AudioConfig(
            audio_encoding=texttospeech.AudioEncoding.MP3
        )

    def get_info(self, info_path: str) -> dict:
        with open(info_path, 'r') as f:
            info_dict = {line[:3]: line[4:] for line in f}
        return info_dict

    def save(self, info_path: str, save_path: str) -> None:
        info_dict = self.get_info(info_path)
        for key, val in info_dict.items():
            synthesis_input = texttospeech.SynthesisInput(text=val)
            response = self.client.synthesize_speech(
                input=synthesis_input,
                voice=self.voice,
                audio_config=self.config
            )
            path = save_path + '/' + key + '.mp3'
            with open(path, 'wb') as out:
                out.write(response.audio_content)
                print(f'saved {path}')


if __name__ == '__main__':
    info_path = 'information.txt'
    save_path = 'sounds'
    tts = GoogleCloudTTS()
    tts.save(info_path, save_path)
