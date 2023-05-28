import pytesseract
from windowcapture import WindowCapture
import pydirectinput
from time import sleep
import pyautogui


# Mention the installed location of Tesseract-OCR in your system
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Read image from which text needs to be extracted
wincap = WindowCapture("BLACK DESERT - 442911")


#num_workers = input("Enter number of workers (total):")
#num_workers = int(num_workers)
num_workers = 6



pydirectinput.click(button="middle", x=1574, y=410)
# First worker

# get an updated image of the game
screenshot = wincap.get_screenshot()

# yn-(yn+1) = 95; xn = (xn+1)
roi = screenshot[380:397, 1412:1429]

# show cropped image
#cv2.imshow("ROI", roi)

# OCR
txt = pytesseract.image_to_string(
    roi, lang='eng', config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789')
print(txt)

if "0" in txt:
    print(" Worker 1 is TIRED")
    sleep(2)
    print("Feeding...")

    sleep(0.5)
    # Click Recover
    pydirectinput.mouseDown(button="left", x=1818, y=366)
    sleep(0.5)
    pydirectinput.mouseUp(button="left", x=1818, y=366)
    #Click Beer
    pydirectinput.mouseDown(button="right", x=1499, y=464)
    sleep(0.5)
    pydirectinput.mouseUp(button="right", x=1499, y=464)
    # Close
    sleep(0.5)
    pydirectinput.mouseDown(button="left", x=1827, y=404)
    sleep(0.5)
    pydirectinput.mouseUp(button="left", x=1827, y=404)

else:
    print("Worker 1 is OK")

# Second worker

# get an updated image of the game
screenshot = wincap.get_screenshot()
 
roi = screenshot[477:490, 1412:1426]

# show cropped image
#cv2.imshow("ROI", roi)

# OCR
txt = pytesseract.image_to_string(
    roi, lang='eng', config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789')
print(txt)

if "0" in txt:
    print("Worker 2 is TIRED")
    sleep(2)
    print("Feeding...")

    sleep(0.5)
    # Click recover
    pydirectinput.mouseDown(button="left", x=1818, y=463)
    sleep(0.5)
    pydirectinput.mouseUp(button="left", x=1818, y=463)
    #Click Beer
    pydirectinput.mouseDown(button="right", x=1499, y=559)
    sleep(0.5)
    pydirectinput.mouseUp(button="right", x=1499, y=559)
    # Close
    sleep(0.5)
    pydirectinput.mouseDown(button="left", x=1827, y=501)
    sleep(0.5)
    pydirectinput.mouseUp(button="left", x=1827, y=501)

else:
    print("Worker 2 is OK")

# Third worker

# get an updated image of the game
screenshot = wincap.get_screenshot()


roi = screenshot[572:585, 1412:1426]

# show cropped image
#cv2.imshow("ROI", roi)

# OCR
txt = pytesseract.image_to_string(
    roi, lang='eng', config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789')
print(txt)

if "0" in txt:
    print("Worker 3 is TIRED")
    sleep(2)
    print("Feeding...")

    sleep(0.5)
    # Click recover
    pydirectinput.mouseDown(button="left", x=1818, y=560)
    sleep(0.5)
    pydirectinput.mouseUp(button="left", x=1818, y=560)
    #Click Beer
    pydirectinput.mouseDown(button="right", x=1499, y=655)
    sleep(0.5)
    pydirectinput.mouseUp(button="right", x=1499, y=655)
    # Close
    sleep(0.5)
    pydirectinput.mouseDown(button="left", x=1827, y=596)
    sleep(0.5)
    pydirectinput.mouseUp(button="left", x=1827, y=596)

else:
    print("Worker 3 is OK")
    
    
    
# Fourth worker

# get an updated image of the game
screenshot = wincap.get_screenshot()


roi = screenshot[667:680, 1412:1426]

# show cropped image
#cv2.imshow("ROI", roi)

# OCR
txt = pytesseract.image_to_string(
    roi, lang='eng', config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789')
print(txt)

if "0" in txt:
    print("Worker 4 is TIRED")
    sleep(2)
    print("Feeding...")

    sleep(0.5)
    # Click recover
    pydirectinput.mouseDown(button="left", x=1818, y=655)
    sleep(0.5)
    pydirectinput.mouseUp(button="left", x=1818, y=655)
    #Click Beer
    pydirectinput.mouseDown(button="right", x=1499, y=750)
    sleep(0.5)
    pydirectinput.mouseUp(button="right", x=1499, y=750)
    # Close
    sleep(0.5)
    pydirectinput.mouseDown(button="left", x=1827, y=691)
    sleep(0.5)
    pydirectinput.mouseUp(button="left", x=1827, y=691)

else:
    print("Worker 4 is OK")




# Fifth worker

# get an updated image of the game
screenshot = wincap.get_screenshot()


roi = screenshot[762:775, 1412:1426]

# show cropped image
#cv2.imshow("ROI", roi)

# OCR
txt = pytesseract.image_to_string(
    roi, lang='eng', config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789')
print(txt)

if "0" in txt:
    print("Worker 5 is TIRED")
    sleep(2)
    print("Feeding...")

    sleep(0.5)
    # Click recover
    pydirectinput.mouseDown(button="left", x=1818, y=750)
    sleep(0.5)
    pydirectinput.mouseUp(button="left", x=1818, y=750)
    #Click Beer
    pydirectinput.mouseDown(button="right", x=1499, y=845)
    sleep(0.5)
    pydirectinput.mouseUp(button="right", x=1499, y=845)
    # Close
    sleep(0.5)
    pydirectinput.mouseDown(button="left", x=1827, y=786)
    sleep(0.5)
    pydirectinput.mouseUp(button="left", x=1827, y=786)

else:
    print("Worker 5 is OK")


if num_workers > 5:
    scrollsup_count = 1
    scrollsdown_count = -1
    while scrollsup_count <= num_workers-5:
        pyautogui.scroll (scrollsdown_count)
        sleep (3)
        #Worker 5+n
        # get an updated image of the game
        screenshot = wincap.get_screenshot()

    
        roi = screenshot[767:780, 1412:1426]
    
        # show cropped image
        #cv2.imshow("ROI", roi)
    
        # OCR
        txt = pytesseract.image_to_string(
            roi, lang='eng', config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789')
        print(txt)
    
        if "0" in txt:
            print("Worker",num_workers + scrollsup_count -1,"is TIRED")
            sleep(2)
            print("Feeding...")
    
            sleep(0.5)
            # Click recover
            pydirectinput.mouseDown(button="left", x=1818, y=750)
            sleep(0.5)
            pydirectinput.mouseUp(button="left", x=1818, y=750)
            #Click Beer
            pydirectinput.mouseDown(button="right", x=1499, y=845)
            sleep(0.5)
            pydirectinput.mouseUp(button="right", x=1499, y=845)
            # Close
            sleep(0.5)
            pydirectinput.mouseDown(button="left", x=1827, y=786)
            sleep(0.5)
            pydirectinput.mouseUp(button="left", x=1827, y=786)
    
        else:
            print("Worker",num_workers + scrollsup_count -1,"is OK")
        
        scrollsdown_count = scrollsdown_count -1
        pyautogui.scroll (scrollsup_count)
        scrollsup_count = scrollsup_count + 1
        sleep (3)
    else:
        pyautogui.scroll (scrollsup_count)
        
