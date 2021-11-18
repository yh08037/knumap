from src.tts_generator import generate_and_save_tts
from src.sound_player import SoundPlayer


if __name__ == '__main__':
    info_txt_path = 'src/information.txt'
    sound_folder_path = 'src/sounds'

    player = SoundPlayer(sound_folder_path)
    player.loop()
