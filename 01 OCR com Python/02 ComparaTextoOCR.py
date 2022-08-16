import numpy as np
import cv2
import pytesseract
from PIL import ImageGrab
from time import sleep

# REGRAS DE USO
pytesseract.pytesseract.tesseract_cmd = r'C:/Users/euleroliveira/AppData/Local/Programs/Tesseract-OCR/Tesseract.exe'
config_tesseract = '--tessdata-dir tessdata --psm 6 -c load_number_dawg=0'

# FUNÇÃO PARA COLETAR O TEXTO VIA OPENCV + TESSERACT
def CirculaTexto(left_x, top_y, right_x, bottom_y):
    i = 0
    tempo = 5
    Armazem = []
    while True:
        # ÁREA ONDE PRECISA SER ACESSADA PARA TRANSFORMAR EM TEXTO
        posicionamento = [[left_x, top_y, right_x, bottom_y]]
        telateste = np.array(ImageGrab.grab(bbox=(posicionamento[i])))
        frame = cv2.cvtColor(telateste, cv2.COLOR_BGR2GRAY)
        cv2.imshow('INTERFACE DE CAPTURA', frame)
        sleep(1)
        tempo -= 1

        # TRANSFORMA A IMAGEM ESCOLHIDA EM TEXTO E DEPOIS INTERPRETA PRA STRING
        texto = pytesseract.image_to_string(frame, lang='por', config=config_tesseract)
        Armazem.append(texto)

        # TEMPORIZADOR PARA FINALIZAR A GRAVAÇÃO
        print(f"o texto captado foi → {Armazem[i]} ←\n e o processo será encerrado em {tempo}...\n")
        if (cv2.waitKey(25) & 0xFF == ord('q')) or tempo == 0:
            cv2.destroyAllWindows()
            return Armazem[i]     

# TRANSFORMA O INPUT DE TEXTO EM LISTAS/VETOR
def ConversorDeTexto(texto):
    lista1 = []
    lista1[:0] = texto

    return lista1

# RECEBE O INPUT DE STRING [PODE SER TEXTO INTERPRETADO PELO TESSERACT]
Texto1 = CirculaTexto(130, 130, 240, 152)
sleep(2)
Texto2 = CirculaTexto(135, 150, 315, 172)

print(f"Dentro de Texto1 temos: {Texto1}")
print(f"Dentro de Texto2 temos: {Texto2}")

# PREENCHE COM "*" A DIFERENÇA DE TAMANHO DA LISTA
if len(Texto1) > len(Texto2):
    while len(Texto2) != len(Texto1):
        Texto2 += '*'
if len(Texto2) > len(Texto1):
    while len(Texto1) != len(Texto2):
        Texto1 += '*'

# CONVERTE AS STRINGS EM LISTAS
separado1 = ConversorDeTexto(Texto1)
separado2 = ConversorDeTexto(Texto2)

# CONDIÇÃO DE FUNCIONAMENTO DO LOOP
Tamanho = len(separado1)
contador = 0
i = 0

# DEFINE A QUANTIDADE DE SEMELHANÇA ENTRE OS TEXTOS
while i < Tamanho:
    if separado1[i] == separado2[i]:
        contador += 1
    i += 1
    porcento = (contador / Tamanho)*100

print(f"\nnde {Tamanho} caracteres, tivemos correspondência de: {contador}, com uma semelhança de: {round(porcento, 2)}%\n")