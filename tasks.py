import pyautogui
import time
import pyperclip
import locale
import paths

locale.setlocale(locale.LC_ALL, '')

def open_file(path: str):
    file_path = path.split("\\")
    print(f'Acessando {file_path[file_path.__len__() - 1]}')
    pyautogui.hotkey('winleft', 'r')
    time.sleep(2)
    pyautogui.write(path, interval=0.01)
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.hotkey('winleft', 'up')   #Tela cheia
    time.sleep(2)
    pyautogui.hotkey('ctrl', 'shiftleft', '6')

def zoom_adjust(value: str):
    """Modifica o zoom para o valor da variável"""
    print('Ajustando Zoom...')
    pyautogui.click(415, 66)    #Editar zoom
    time.sleep(1)
    pyautogui.write(value, interval=0.01)
    time.sleep(1)
    pyautogui.press('enter')

def skip_pages():
    """Pula as páginas que já estão enumeradas"""
    print('Pulando as páginas que já estão enumeradas...')
    for n in range (12):
        time.sleep(0.5)
        pyautogui.press("pagedown")
    
def count_pages():
    """Retorna o número total de páginas"""
    print('Extraindo o número de páginas...')
    pyautogui.click(646, 715)   #Seleciona o número de páginas
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(1)
    str_contagem = pyperclip.paste()
    int_contagem = int(str_contagem.split(' / ')[1])
    print('Extração concluída!')
    return int_contagem
