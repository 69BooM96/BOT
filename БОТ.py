import pyautogui
import keyboard


#пауза и досрочное прекращение
pyautogui.PAUSE = 0.1
pyautogui.FAILSAFE = True

#разрешение и позиция
pyautogui.size()
pyautogui.position()

#Запуск
isClicking = False
def set_clicker():
    global isClicking
    if isClicking:
        isClicking = False
        print("off")
    else:
        isClicking = True
        print("on")


keyboard.add_hotkey("b",set_clicker)

while True:
    if isClicking:
        from time import sleep

        sleep(0.5)
        print('3%')
        pyautogui.press('f3')
        pyautogui.move(0, 150, duration=1)
        pyautogui.keyDown('-')
        sleep(5.0)
        print('6%')
        pyautogui.keyUp('-')
        pyautogui.move(0, -30, duration=1)
        pyautogui.move(60, 0, duration=1)
        pyautogui.keyDown('up')
        pyautogui.keyDown('-')
        sleep(29.0)
        print('9%')
        pyautogui.keyUp('-')
        pyautogui.keyUp('up')
        pyautogui.keyDown('down')
        sleep(7.5)
        print('12%')
        pyautogui.keyUp('down')
        pyautogui.move(-59, 0, duration=1)

        # Перемещение игрока
        # 1
        pyautogui.keyDown('up')
        pyautogui.keyDown('-')
        sleep(18.0)
        print('15%')
        pyautogui.keyUp('up')
        pyautogui.keyUp('-')

        # 2
        pyautogui.keyDown('down')
        sleep(6.0)
        print('18%')
        pyautogui.keyUp('down')
        pyautogui.keyDown('right')
        sleep(0.11)
        print('21%')
        pyautogui.keyUp('right')

        # 3
        pyautogui.keyDown('up')
        pyautogui.keyDown('-')
        sleep(18.0)
        print('24%')
        pyautogui.keyUp('up')
        pyautogui.keyUp('-')
        pyautogui.keyDown('down')
        sleep(4.5)
        print('27%')
        pyautogui.keyUp('down')
        pyautogui.keyDown('right')
        sleep(0.11)
        print('30%')
        pyautogui.keyUp('right')

        # 4
        pyautogui.keyDown('up')
        pyautogui.keyDown('-')
        sleep(18.0)
        print('33%')
        pyautogui.keyUp('up')
        pyautogui.keyUp('-')
        pyautogui.keyDown('down')
        sleep(4.5)
        print('36%')
        pyautogui.keyUp('down')
        pyautogui.keyDown('right')
        sleep(0.11)
        print('39%')
        pyautogui.keyUp('right')
        #Переключение
        pyautogui.press('2')

        # 5
        pyautogui.keyDown('up')
        pyautogui.keyDown('-')
        sleep(18.0)
        print('42%')
        pyautogui.keyUp('up')
        pyautogui.keyUp('-')
        pyautogui.keyDown('down')
        sleep(4.5)
        print('45%')
        pyautogui.keyUp('down')
        pyautogui.keyDown('right')
        sleep(0.11)
        print('48%')
        pyautogui.keyUp('right')

        # 6
        pyautogui.keyDown('up')
        pyautogui.keyDown('-')
        sleep(18.0)
        print('51%')
        pyautogui.keyUp('up')
        pyautogui.keyUp('-')
        pyautogui.keyDown('down')
        sleep(4.5)
        print('54%')
        pyautogui.keyUp('down')
        pyautogui.keyDown('right')
        sleep(0.11)
        print('57%')
        pyautogui.keyUp('right')

        # 7
        pyautogui.keyDown('up')
        pyautogui.keyDown('-')
        sleep(18.0)
        print('60%')
        pyautogui.keyUp('up')
        pyautogui.keyUp('-')
        pyautogui.keyDown('down')
        sleep(4.5)
        print('63%')
        pyautogui.keyUp('down')
        pyautogui.keyDown('right')
        sleep(0.11)
        print('66%')
        pyautogui.keyUp('right')
        #Переключение
        pyautogui.press('3')

        # 8
        pyautogui.keyDown('up')
        pyautogui.keyDown('-')
        sleep(18.0)
        print('69%')
        pyautogui.keyUp('up')
        pyautogui.keyUp('-')
        pyautogui.keyDown('down')
        sleep(4.5)
        print('72%')
        pyautogui.keyUp('down')
        pyautogui.keyDown('right')
        sleep(0.11)
        print('75%')
        pyautogui.keyUp('right')

        # 9
        pyautogui.keyDown('up')
        pyautogui.keyDown('-')
        sleep(18.0)
        print('78%')
        pyautogui.keyUp('up')
        pyautogui.keyUp('-')
        pyautogui.keyDown('down')
        sleep(4.5)
        print('81%')
        pyautogui.keyUp('down')
        pyautogui.keyDown('right')
        sleep(0.11)
        print('84%')
        pyautogui.keyUp('right')
        #Переключение
        pyautogui.press('4')

        # 10
        pyautogui.keyDown('up')
        pyautogui.keyDown('-')
        sleep(18.0)
        print('87%')
        pyautogui.keyUp('up')
        pyautogui.keyUp('-')
        pyautogui.keyDown('down')
        sleep(4.5)
        print('90%')
        pyautogui.keyUp('down')
        pyautogui.keyDown('right')
        sleep(0.11)
        print('93%')
        pyautogui.keyUp('right')
        pyautogui.press('f3')
        print('100%')
        sleep(0.5)
        print('STOP')

        #занаво2

        print('№2')
        sleep(0.5)
        print('103%')
        pyautogui.press('f3')
        pyautogui.move(0, 150, duration=1)
        pyautogui.keyDown('-')
        sleep(1.5)
        print('106%')
        pyautogui.keyUp('-')
        pyautogui.move(0, -30, duration=1)
        pyautogui.move(60, 0, duration=1)
        pyautogui.keyDown('up')
        pyautogui.keyDown('-')
        sleep(29.0)
        print('109%')
        pyautogui.keyUp('-')
        pyautogui.keyUp('up')
        pyautogui.keyDown('down')
        sleep(7.5)
        print('112%')
        pyautogui.keyUp('down')
        pyautogui.move(-59, 0, duration=1)
        print('Всё')
        quit()