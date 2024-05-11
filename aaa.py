import webbrowser
import time

url = "http://jp.adorable-pet.com/pic_VmI3TjV0UkRjbEdQN1pCbmFPd0JhUT09"
count = 50
repeats = 4545

for _ in range(repeats):
    for _ in range(count):
        webbrowser.open(url)
    time.sleep(5)
