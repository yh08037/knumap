from gtts import gTTS


def get_info(info_path: str) -> dict:
    with open(info_path, 'r') as f:
        info_dict = {line[:3]: line[4:] for line in f}
    return info_dict


def save_tts(info_dict: str, save_folder_path: str) -> None:
    for key, val in info_dict.items():
        tts = gTTS(text=val, lang='ko')
        path = save_folder_path + '/' + key + '.mp3'
        tts.save(path)
        print('saved', path)


def generate_and_save_tts(info_txt_path: str, save_folder_path: str):
    info_dict = get_info(info_txt_path)
    save_tts(info_dict, save_folder_path)


if __name__ == '__main__':
    txt_path = 'information.txt'
    save_folder = 'sounds'
    generate_and_save_tts(txt_path, save_folder)
