import pytesseract as pyt
import time
import pyscreenshot
import pyautogui as pag


pyt.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

pag.FAILSAFE = True

while True:
    LiveImage = pyscreenshot.grab(bbox=(55, 936, 414, 1021))
    time.sleep(0.1)
    text = pyt.image_to_string(LiveImage)
    partsOfText = text.split()
    print(partsOfText)
    for i in partsOfText:
        if i == "still":
            pag.press('enter')
            pag.write('666/555/444/333')
            time.sleep(0.05)
            pag.press('enter')
    partsOfText.clear()