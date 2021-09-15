from time import sleep
import pyautogui
from threading import Thread
# from sys import exit


def fixed_time():
    global can_run
    can_run = True
    try:
        # print("Partito fixed time")
        sleep(int(input_time))
        print("Stopping Spamming. For Spam More Re-Open the File Spammer.exe")
        can_run = False
    except Exception as e:
        print(f"Something Went Wrong... Try Re-Opening the file or report it to us! Github: @Pit869\n\n[ERROR]: {e}")


def spamming():
    try:
        # print("Partito spamming")
        print("Spamming!")
        for word in f:
            while can_run:
                pyautogui.typewrite(word)
                pyautogui.press("enter")
    except Exception as e:
        print(f"Something Went Wrong... Try Re-Opening the file or report it to us! Github: @Pit869\n\n[ERROR]: {e}")


def running():
    try:
        t1 = Thread(target=fixed_time)
        t1.start()
        t2 = Thread(target=spamming)
        t2.start()
    except Exception as e:
        print(f"Something Went Wrong... Try Re-Opening the file or report it to us! Github: @Pit869\n\n[ERROR]: {e}") 


if __name__ == "__main__":
    print("I'll give you five seconds to write for how many seconds you want the spammer to write the message")
    input_time = input()
    if not input_time.isnumeric():
        print("The Input must be numeric!")
    else:
        print("I'll Give you other Five Seconds to Open your Window")
        sleep(5)
        f = open("words.txt", 'r')
        running()
