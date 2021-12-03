from pynput import keyboard
from multiprocessing import Process, Queue


class KeyboardListener:
    def __init__(self):
        self.key_buffer = []
        self.word_queue = Queue()
        self.process = Process(target=self.listen)

    def on_press(self, key):
        if hasattr(key, 'vk') and key.vk is not None:
            if key.vk == 65437:
                self.key_buffer.append('5')
        elif key == keyboard.Key.enter:
            word = ''.join(self.key_buffer)
            self.word_queue.put(word)
            self.key_buffer = []
        elif hasattr(key, 'char') and key.char is not None:
            if key.char.isdigit():
                self.key_buffer.append(key.char)

    def listen(self):
        with keyboard.Listener(
                on_press=self.on_press) as listener:
            listener.join()

    def run(self):
        self.process.start()

    def available(self) -> bool:
        return not self.word_queue.empty()

    def get_word(self) -> str:
        if not self.word_queue.empty():
            return self.word_queue.get()
        return None


if __name__ == '__main__':
    key = KeyboardListener()
    key.run()
