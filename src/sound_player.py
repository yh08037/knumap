import os
import glob
from multiprocessing import Process


class SoundPlayer:
    def __init__(self, folder_path: str) -> None:
        self.path_dict: dict = self.get_path_dict(folder_path)
        self.process: Process = None

    def loop(self) -> None:
        self.print_available_building_number()
        while val := input():
            if val == 'a':
                self.stop_sound()
            else:
                self.play_sound(val)

    def play_sound(self, input_val: str):
        if self.process is not None:
            self.stop_sound()
        file_path = self.get_file_path(input_val)
        self.process = Process(target=self.mpg123_play, args=(file_path,))
        self.process.start()

    def stop_sound(self):
        if self.process is not None:
            self.mpg123_kill()
            self.process.join()
            self.process = None

    def mpg123_play(self, path: str) -> None:
        os.system('mpg123 -q ' + path)

    def mpg123_kill(self) -> None:
        os.system('pkill mpg123')

    def get_file_path(self, input_val: str) -> str:
        res = self.path_dict.get(input_val)
        if res is None:
            res = self.path_dict.get('000')
        return res

    def get_path_dict(self, folder_path: str) -> dict:
        path_list = glob.glob(folder_path + '/*.mp3')
        return {path[-7:-4]: path for path in path_list}

    def print_available_building_number(self):
        print(sorted(list(self.path_dict.keys()))[1:])


if __name__ == '__main__':
    folder_path = 'sounds'
    player = SoundPlayer(folder_path)
    player.loop()
