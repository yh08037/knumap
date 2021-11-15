from gtts import gTTS


def get_info(info_path: str) -> dict:
    with open(info_path, 'r') as f:
        info_dict = {line[:3]: line[4:] for line in f}
    return info_dict


def save_tts(info_dict: str, save_folder: str) -> None:
    for key, val in info_dict.items():
        tts = gTTS(text=val, lang='ko')
        path = save_folder + '/' + key + '.mp3'
        tts.save(path)
        print('saved', path)


if __name__ == '__main__':
    txt_path = 'information.txt'
    save_folder = 'sounds'

    info_dict = get_info(txt_path)
    save_tts(info_dict, save_folder)
