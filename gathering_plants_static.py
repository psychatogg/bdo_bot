import cv2 as cv
from time import sleep
from windowcapture import WindowCapture
import pydirectinput
import datetime


wincap = WindowCapture("BLACK DESERT - 442911")

needle = cv.imread(
    "C:\\GDrive1\\proyectos\\botting\\bdo_bot\\Needles\\logo_gathering_plants.jpg", 0)




# get an updated image of the game
screenshot = wincap.get_screenshot()
screenshot = cv.cvtColor(screenshot, cv.COLOR_BGR2GRAY)
#cv.imshow('Computer Vision', screenshot)
#if cv.waitKey(1) == ord('q'):
    #cv.destroyAllWindows()
# Initiate SIFT detector
sift = cv.SIFT_create()
# find the keypoints and descriptors with SIFT
kp1, des1 = sift.detectAndCompute(needle, None)
kp2, des2 = sift.detectAndCompute(screenshot, None)
# BFMatcher with default paramsr
bf = cv.BFMatcher()
matches = bf.knnMatch(des1, des2, k=2)
# Apply ratio testr
good = []
for m, n in matches:
    if m.distance < 0.75*n.distance:
        good.append([m])
# cv.drawMatchesKnn expects list of lists as matches.
result = cv.drawMatchesKnn(needle, kp1, screenshot, kp2, good,
                           None, flags=cv.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)



ts = datetime.datetime.now()


if len(good) > 4:
    print("JACKPOT", ts)

    pydirectinput.click(button="middle", x=1090, y=366)

    sleep(0.5)
    print("Gathering", ts)
    pydirectinput.press('r')
    #barehand = 7
    #Hoe = 22/12r
    sleep(7)
    print("Getting all", ts)
    pydirectinput.press('r')

else:
    print("No match", ts)

    