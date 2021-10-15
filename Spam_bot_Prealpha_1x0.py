import pyautogui
import time
import os
global switch
global switchtime
global msgtime
global reprange


def spambot():
    os.system("cls")
    msg = input("Message to Spam:")
    rep = int(input("Number of 100 Sets:"))
    x = int(input("Seconds to execute: "))

    time.sleep(x)

    for j in range(rep):
        for i in range(reprange):
            pyautogui.typewrite(msg)
            pyautogui.press("enter")
            print("Message_ " + str(i) + " _sent")
            i = int(i) + 1
            time.sleep(msgtime)
            if i == 100:
                i = int(1)
        j = int(j) + 1
        print("--------------")
        print("Set Completed")
        print("--------------")
        if j == rep:
            j = int(1)
        else:
            time.sleep(switchtime)

    print("--------------")
    print("Last message was sent")
    time.sleep(3)
    print("Process is over")
    time.sleep(3)
    print("Return to Main in 15 seconds")
    time.sleep(15)
    main()


def config():

    os.system("cls")
    print("---------------------------------------")
    print("Troll Bot. Pre-alpha 1.0 - CONFIG")
    print("---------------------------------------")
    print("")
    print("CHOOSE YOUR OPTION:")
    print("---------------------------------------")
    print("1.Change Switching Sets Time (Def: 120)")
    print("2.Change Message Delay (Def: 1)")
    print("3.Change Set Range (Def: 100)")
    print("4.Return")
    print("---------------------------------------")
    opt = int(input("Type your number -> "))
    if opt == 1:
        global switchtime
        switchtime = int(input("Select your switch time in secs -> "))
    if opt == 2:
        global msgtime
        msgtime = int(input("Select your delay time in secs -> "))
    if opt == 3:
        global reprange
        reprange = int(input("Select your Set Range -> "))
    if opt == 4:
        main()


def main():

    os.system("cls")
    global msgtime
    global switchtime
    global reprange
    reprange = str(reprange)
    msgtime = str(msgtime)
    switchtime = str(switchtime)
    print("---------------------------------------")
    print("Welcome to Troll Bot. Pre-alpha 1.0")
    print("---------------------------------------")
    print("Message Delay         -> " + msgtime)
    print("Switching Sets Delay  -> " + switchtime)
    print("Sets Range            -> " + reprange)
    print("---------------------------------------")
    print("CHOOSE YOUR OPTION:")
    print("---------------------------------------")
    print("1.Spam Bot - PreAlpha 1.0")
    print("2.Config")
    print("3.Exit")
    print("---------------------------------------")
    opt = int(input("Type your number -> "))

    if opt == 1:
        msgtime = int(msgtime)
        switchtime = int(switchtime)
        reprange = int(reprange)
        spambot()
    if opt == 2:
        msgtime = int(msgtime)
        switchtime = int(switchtime)
        reprange = int(reprange)
        config()
    else:
        global switch
        switch = bool(False)

msgtime = int(1)
switchtime = int(120)
reprange = int(100)
switch = bool(True)

while switch is True:
    main()
