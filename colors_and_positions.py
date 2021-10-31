import pyautogui as pt
from time import sleep
import pyperclip
import random

sleep(2)

position1 = pt.locateAllOnScreen("smiely.PNG", confidence=.6)
x = position1[0]
y = position1[1] 

# Gets message
def get_message():
    global x,y

    position = pt.locateAllOnScreen("smiely.PNG", confidence=.6)
    x = position[0]
    y = position[1]
    pt.moveTo(x,y, duration=0.5)
    pt.moveTo(x+70, y-40, duration=.5)
    pt.tripleClick()
    pt.rightClick()
    pt.moveRel(12,15)
    pt.click()
    whatsapp_message = pyperclip.paste()
    pt.click()
    print("message received: "+ whatsapp_message)

    return whatsapp_message

def post_response(message):
    global x,y

    position = pt.locateOnScreen('smiely.PNG', confidence=.6)
    x = position[0]
    y = position[1]
    pt.moveTo(x+200, y +20, durations=.5)
    pt.click()
    pt.typewrite(message, interval=0.1)
    
    pt.typewrite("\n", interval=0.1)


def process_response(message):
    random_no = random.randrange(3)

    if "?" in str(message).lower():
        return "Don't ask me any questions!"
    
    else:
        if random_no == 0:
            return "That's cool!"
        elif random_no ==1:
            return "Remeber to subscribe to code palace!"
        else:
            return "i want to eat something."

def check_for_new_messages():
    pt.moveTo(x+50,y-35, duration=.5)

    while True:
        try:
            position = pt.locateAllOnScreen('green_circle.png', confidence=.7)

            if position is not None:
                pt.moveTo(position)
                pt.moveRel(-100, 0)
                pt.cilck()
                sleep(.5)
            else:
                pass
        except Exception as e :
            print(e)

        if pt.pixelMatchesColor(int(x+50), int(y-35), (255,255,255), tolerance=10):
            print("is_white")
            processed_message = process_response(get_message())
            post_response(processed_message)
        else:
            print("No new messages yet...")
        sleep(5)
processed_message = process_response(get_message())

post_response(processed_message)