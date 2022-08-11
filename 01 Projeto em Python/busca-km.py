import numpy as np
import cv2
import pyautogui as pg
import pytesseract
from PIL import ImageGrab
from time import sleep

# REGRAS DE USO 
pytesseract.pytesseract.tesseract_cmd = r'C:/Users/euleroliveira/AppData/Local/Programs/Tesseract-OCR/Tesseract.exe' 
config_tesseract = '--tessdata-dir tessdata --psm 6 -c load_number_dawg=0'

sleep(3)
quantidade = 0
pg.PAUSE = .4

# TER UMA PLANILHA EXCEL COM A SEGUINTE COMPOSIÇÃO:
# 1ª COLUNA = NOME DO LUGAR
# 2ª COLUNA = LATITUDE E LONGITUDE DO LUGAR
# 3ª COLUNA = CÉLULA VAZIA PARA O INPUT DA DISTÂNCIA

# COMEÇA NA PLANILHA E COM O MAPS NO ALT TAB
while quantidade < 100:
    quantidade += 1

    # PEGAR A LATITUDE E LONGITUDE
    pg.hotkey('tab')
    pg.hotkey('f2')
    pg.hotkey('ctrl', 'a')
    pg.hotkey('ctrl', 'c')
    pg.hotkey('esc')

    # IR PARA O MAPS E COLAR A DISTÂNCIA
    pg.hotkey('alt', 'tab')
    pg.moveTo(150,200)
    pg.leftClick()
    pg.hotkey('ctrl', 'v')
    pg.hotkey('enter')
    sleep(6)

    # LER COM O TESSERACT A DISTÂNCIA NO MAPS
    while True:
        # MAIS ESPAÇOSO PRA PEGAR MILHAR
        quadrado = (335, 450, 385, 480) # 315, 445, 405, 480 ← esse é o que tava dando certo antes
        img = ImageGrab.grab(bbox=(quadrado))
        img_np = np.array(img)
        frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)
        cv2.imshow("Contador", frame)
        sleep(2)
        texto = pytesseract.image_to_string(
            frame, lang='por', config=config_tesseract)

        if cv2.waitKey(5):
            break
    
    # VOLTAR PARA A PLANILHA E IMPUTAR A DISTÂNCIA
    pg.hotkey('alt', 'tab')
    pg.hotkey('tab')
    pg.write(texto)