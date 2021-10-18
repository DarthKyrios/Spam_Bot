import pyautogui
import time
import os

global f
global programa
global mensaje
global hud2time
global lista
global hud2set
global switchtime
global msgtime
global reprange


class func:

    def HUD1():
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
            Soft.spambot()
        if opt == 2:
            msgtime = int(msgtime)
            switchtime = int(switchtime)
            reprange = int(reprange)
            func.config()

        if opt == 3:
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
            func.HUD1()
        func.HUD1()


    def HUD2():

        global mensaje
        global hud2time
        global lista
        global hud2set
        global f
        os.system("cls")
        f = pyautogui.getWindowsWithTitle(programa)
        lista = list(f)
        os.system("cls")
        print("#############################################################################")
        print("###                        TROLL BOT MULTI ACCOUNT                        ###")
        print("#############################################################################")
        print("###                           Ver Pre-alpha 1.1                           ###")
        print("#############################################################################")
        print("###                           CHOOSE AN OPTION                            ###")
        print("#############################################################################")
        mensaje = str(input("### 1. Message to Spam -> "))
        hud2time = int(input("### 2. Seconds between Sets -> "))
        hud2set = int(input("### 3. Number of Sets -> "))
        print("#############################################################################")
        Soft.multispam()

    def HUD3():
        os.system("cls")
        print("#############################################################################")
        print("###                          PROCESS FINISHED                             ###")
        print("#############################################################################")
        print("###                          CHOOSE AN OPTION                             ###")
        print("#############################################################################")
        print("### 1. Restart the process all over again                                 ###")
        print("### 2. Reset parameters and start again                                   ###")
        print("### 3. Go back to main menu                                               ###")
        print("#############################################################################")
        opt = int(input("### -> "))
        print("#############################################################################")
        if opt == 1:
            Soft.multispam()
        if opt == 2:
            func.HUD2()
        if opt == 3:
            main()

class Soft:

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
        print("Return to Spambot in 15 seconds")
        time.sleep(15)
        func.HUD1()


    def multispam():

        opt = pyautogui.confirm
        var = opt(text='Are you sure you want to start?', title='ATTENTION!', buttons=['VIVA UMMO', 'AMORALES'])
        if var == 'VIVA UMMO':
            for k in range(len(lista)):
                f[k].minimize()
                k = +1

            for j in range(hud2set):
                for i in range(len(lista)):
                    print("ventana ", i)
                    f[i].maximize()
                    time.sleep(0.05)
                    pyautogui.write(mensaje)
                    pyautogui.press("enter")
                    f[i].minimize()
                    i = +1
            j = +1
            time.sleep(hud2time)
        else:
            pyautogui.alert(text='AMORALES', title='AMORALES', button='AMORALES')
            os.system("cls")
            print("#############################################################################")
            print("###                         PROCCESS FINISHED                             ###")
            print("###                   GOING BACK TO UMMO IN 5 SECONDS                     ###")
            print("#############################################################################")
            time.sleep(5)
            func.HUD3()

        print("PROCESS FINISHED")
        func.HUD3()


loop = bool(True)
msgtime = int(1)
switchtime = int(120)
reprange = int(100)


def main():
    global loop
    while loop:
        os.system("cls")
        print("")
        print("#############################################################################")
        print("###                              MAIN MENU                                ###")
        print("#############################################################################")
        print("###                     CHOOSE A PROGRAM TO EXECUTE                       ###")
        print("#############################################################################")
        print("### 1. Single Spam Bot                                                    ###")
        print("### 2. Multi Spam Bot                                                     ###")
        print("### 3. Exit                                                               ###")
        print("#############################################################################")
        var = int(input("### -> "))
        if var == 1:
            func.HUD1()
        else:
            if var == 2:
                global programa
                os.system("cls")
                programa = str(input("### 1. What's the EXACT name of the software you will use? -> "))
                func.HUD2()
            else:
                if var == 3:
                    loop = bool(False)
                else:
                    print("Not elegible, try again")


main()
