import pyautogui
import time
import datetime
import pyperclip
import locale

locale.setlocale(locale.LC_ALL, '')

def open_main_folder() -> None:
    main_path = "F:\\Python\\Bots_Python\\main"
    print('Acessando pasta principal...')
    pyautogui.hotkey('winleft', 'r')
    time.sleep(2)
    pyautogui.write(main_path, interval=0.01)
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.hotkey('winleft', 'up')   #Tela cheia
    time.sleep(2)
    pyautogui.hotkey('ctrl', 'shiftleft', '6')

def open_report_pdf() -> None:
    report_path = "F:\\Python\\Bots_Python\\main\\Relatorio.pdf"
    print('Abrindo Relatorio.pdf...')
    pyautogui.hotkey('winleft', 'r')
    time.sleep(2)
    pyautogui.write(report_path, interval=0.01)
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.hotkey('winleft', 'up')   #Tela cheia

def open_analysis_pdf() -> None:
    analysis_path = "F:\\Python\\Bots_Python\\analysis\\analysis.pdf"
    print('Abrindo analysis.pdf...')
    time.sleep(2)
    pyautogui.hotkey('winleft', 'r')
    time.sleep(2)
    pyautogui.write(analysis_path, interval=0.01)
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.hotkey('winleft', 'up')   #Tela cheia

def number_of_pages() -> int:
    print('Extraindo o número de páginas...')
    time.sleep(1)
    pyautogui.click(646, 715)   #Seleciona o número de páginas
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(1)
    str_contagem = pyperclip.paste()
    int_contagem = int(str_contagem.split(' / ')[1])
    print('Extração concluída!')
    return int_contagem

def zoom_adjust(value: str):
    print('Ajustando Zoom...')
    pyautogui.click(415, 66)    #Editar zoom
    time.sleep(1)
    pyautogui.write(value, interval=0.01)
    time.sleep(1)
    pyautogui.press('enter')

def skip_pages():
    print('Pulando as páginas que já estão enumeradas...')
    for n in range (12):
        time.sleep(0.5)
        pyautogui.press("pagedown")
    
def count_pages():
    print('Extraindo o número de páginas...')
    pyautogui.click(646, 715)   #Seleciona o número de páginas
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(1)
    str_contagem = pyperclip.paste()
    int_contagem = int(str_contagem.split(' / ')[1])
    print('Extração concluída!')
    return int_contagem
