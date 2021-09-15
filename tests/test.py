from time import sleep
from threading import Thread
from sys import exit

counting = True


def normal():
    global running
    running = True
    if running:
        print("normal")
        sleep(5)
        print("Bye")
        running = False


def extra():
    while running:
        print("working")
        sleep(1)
    
if __name__ == "__main__":
    t1 = Thread(target=normal)
    t1.start()
    t2 = Thread(target=extra)
    t2.start()
    