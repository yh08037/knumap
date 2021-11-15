import os
import glob


def get_path_dict(folder_path: str) -> dict:
    path_list = glob.glob(folder_path + '/*.mp3')
    return {path[-7:-4]: path for path in path_list}


def play_sound(path: str) -> None:
    os.system('mpg123 -q ' + path)


def loop(path_dict) -> None:
    while True:
        res = path_dict.get(input())
        if res == None:
            print('invalid input')
        else:
            play_sound(res)


if __name__ == '__main__':
    folder_path = 'src/sounds'
    path_dict = get_path_dict(folder_path)
    print(path_dict)
    loop(path_dict)
