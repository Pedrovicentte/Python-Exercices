import os
#import datetime
#import pyautogui

lis_arquivos = os.listdir("Metodos_Bibliotecas/arquivos")

for arquivo in lis_arquivos:
    if ".txt" in arquivo:
       if "22" in arquivo:
           os.rename(f"Metodos_Bibliotecas/arquivos/{arquivo}", f"Metodos_Bibliotecas/arquivos/22/{arquivo}")
           print("Movimentar para a pasta 22", arquivo)
       else:
           os.rename(f"Metodos_Bibliotecas/arquivos/{arquivo}", f"Metodos_Bibliotecas/arquivos/23/{arquivo}")
           print("Movimentar para a pasta 23", arquivo)
      





'''
pyautogui.press("win")
pyautogui.write("Chrome")
pyautogui.moveTo(x = 925, y=528)
pyautogui.click(button ='left')
pyautogui.moveTo(x = 717, y = 518)
pyautogui.click(button = 'left')
pyautogui.write("youtube.com")
pyautogui.press('enter')


print('Press Ctrl-C to quit.')
try:
    while True:
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)
except KeyboardInterrupt:
    print('\n')

'''

#print(os.listdir("Metodos_Bibliotecas/arquivos"))
#print(datetime.date.today())