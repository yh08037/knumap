 

if __name__ == '__main__':
    with open('/dev/usb/hiddev0', 'r') as f:
        while True:
            where = f.tell()
            line = f.readline().strip()
            print(line)
            if not line:
                f.seek(here)
            else:
                print(line)
