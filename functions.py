import pyautogui
import time
import datetime
import pyperclip
import locale
import tasks

locale.setlocale(locale.LC_ALL, '')

def montar_relatorio():
    zoom = '45.52'
    mouse_x, mouse_y = (489, 647) #Ponto inicial -> Zoom = 45.52% -> Foxit Phantom PDF.
    mouse_x_f, mouse_y_f = (1000, 683) #Ponto final -> Zoom = 45.52% -> Foxit Phantom PDF.
    x_drag, y_drag = ((mouse_x_f - mouse_x), (mouse_y_f - mouse_y)) #Distância do drag -> Zoom = 45.52% -> Foxit Phantom PDF.
    print("Bot iniciado!")
    print("Atenção: Não utilize o mouse ou o teclado enquanto o bot estiver em funcionamento!")
    print("Pressione ctrl + alt + del caso queira interromper o bot!")
    pyautogui.alert("Atenção: Não utilize o mouse ou o teclado enquanto o bot estiver em funcionamento!", "Alerta", "Iniciar")
    time.sleep(3)
    pyautogui.hotkey('winleft', 'up')   #Tela cheia
    time.sleep(2)
    tasks.open_report_pdf()
    time.sleep(3)
    pyautogui.hotkey('winleft', 'up')   #Tela cheia
    time.sleep(3)
    int_contagem = tasks.number_of_pages()  #Armazena o número de páginas em uma variável
    time.sleep(1)
    tasks.open_analysis_pdf()
    time.sleep(3)
    print("Página 'Relatorio'...")
    pyautogui.click(268, 161)   #Página 'Relatorio'
    time.sleep(1)
    print('Primeira página...')
    pyautogui.press('home')
    time.sleep(1)
    print('Home...')
    pyautogui.click(95, 42)     #Home
    time.sleep(1)
    print('Alterando para visualização Single Page...')
    pyautogui.click(1035, 709)  #Single page
    time.sleep(1)
    tasks.zoom_adjust(zoom)
    time.sleep(1)
    print('Página "Criticidade"')
    pyautogui.click(432, 163)   #Página 'Criticidade'
    time.sleep(1)
    tasks.zoom_adjust(zoom)
    time.sleep(1)
    print('Editar...')
    pyautogui.click(222, 39)    #Editar
    time.sleep(2)
    print('Editar Objeto...')
    pyautogui.click(148, 77)    #Editar Objeto
    time.sleep(1)
    print("Copiando o conteúdo da página 'Criticidade'...")
    pyautogui.click(463, 184)   #Posicionar mouse
    time.sleep(1)
    pyautogui.drag(536, 530, duration=1)
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(1)
    pyautogui.click(257, 159)
    time.sleep(1)
    print('Editar Objeto...')
    pyautogui.click(148, 77)    #Editar Objeto
    time.sleep(1)
    print('Realizando a análise...')
    for i in range(int_contagem):
        print(f'Página: {i + 1}')
        time.sleep(0.5)
        pyautogui.click(mouse_x, mouse_y)
        time.sleep(0.5)
        pyautogui.drag(x_drag, y_drag, duration=0.4)
        time.sleep(0.5)
        pyautogui.press(keys='del')
        time.sleep(0.5)
        pyautogui.click(786, 621)   #Área em branco
        time.sleep(0.5)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(0.5)
        pyautogui.click(724, 714)   #Próxima página
    print('Análise concluída...')
    time.sleep(2)
    print('Salvando...')
    pyautogui.hotkey('ctrl', 's')
    time.sleep(10)
    pyautogui.alert("Análise concluída!", "Notificação", "Continuar")

def unir_pdf():
    print("Estruturando o relatório...")
    time.sleep(1)
    pyautogui.click(1106, 478)  #Área em branco
    time.sleep(2)
    print('Fechando janela...')
    pyautogui.click(1346, 11)   #Fechar arquivo
    time.sleep(1)
    pyautogui.click(676, 386)   #Close all tabs
    time.sleep(1)
    tasks.open_main_folder()
    time.sleep(3)
    print('Combinando arquivos...')
    pyautogui.click(445, 476)   #Posiciona o mouse para arrastar
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(1)
    pyautogui.rightClick(308, 160)
    time.sleep(3)
    pyautogui.click("images\\combine.png")
    time.sleep(3)
    pyautogui.click(297, 196)   #Posiciona o mouse para arrastar
    time.sleep(1)
    pyautogui.drag(0, 18, duration=0.5)
    time.sleep(1)
    pyautogui.click("images\\combine_1.png")
    #time.sleep(3)
    #pyautogui.click("images\\combine_yes.png")
    time.sleep(10)
    pyautogui.alert("Combinação de arquivos concluída!", "Notificação", "Continuar")

def enumerar_paginas():
    zoom = '75'
    print("Enumeração de páginas iniciado!")
    time.sleep(2)
    int_contagem = tasks.count_pages()
    time.sleep(1)
    pyautogui.click(1148, 437)  #Área em branco
    time.sleep(1)
    print('Primeira página...')
    pyautogui.press('home')
    time.sleep(2)
    pyautogui.click(97, 45)     #Home
    time.sleep(1)
    tasks.zoom_adjust(zoom)
    time.sleep(2)
    print('Editar...')
    pyautogui.click(221, 35)    #Editar
    time.sleep(1)
    print('Editar texto...')
    pyautogui.click(105, 76)    #Editar Texto
    time.sleep(1)
    print('Alterando para a visualização Single Page...')
    pyautogui.click(1035, 709)  #Single page
    time.sleep(1)
    pyautogui.click(1106, 478)  #Área em branco
    time.sleep(1)
    tasks.skip_pages()
    time.sleep(1)
    print('Enumeração inicializada...')
    cont = 7
    for n in range(int_contagem - 6):
        print(f'Página: {cont}')
        time.sleep(0.5)
        pyautogui.press('pagedown')
        time.sleep(0.5)
        pyautogui.click(932, 666)   #Editar número da página
        time.sleep(0.5)
        pyautogui.press('backspace')
        time.sleep(0.5)
        pyautogui.write(f'{cont}')
        time.sleep(0.5)
        pyautogui.click(1106, 478)  #Área em branco
        time.sleep(0.5)
        pyautogui.press('pagedown')
        cont += 1
    time.sleep(4)
    pyautogui.alert("Enumeração concluída!", "Notificação", "Continuar")

def informacoes():
    print("Inserção de informações inicializada...")
    zoom = '75'
    ano = int(input("Digite o ano do relatório (número inteiro): "))
    mes = str(input("Digite o mês do relatório  (número inteiro): "))
    objeto_mes = datetime.datetime.strptime(mes, "%m")
    nome_mes = objeto_mes.strftime("%B")
    dia = int(input("Digite o dia do relatório (número inteiro): "))
    embarcacao = input("Digite o nome da embarcação (sem caractere especial ou acento): ")
    time.sleep(2)
    print("Inserindo informações...")
    time.sleep(1)
    pyautogui.click(95, 42)     #Home
    time.sleep(1)
    tasks.zoom_adjust(zoom)
    time.sleep(1)
    pyautogui.click(222, 39)
    time.sleep(2)
    pyautogui.click(148, 77)    #Editar Objeto
    time.sleep(1)
    pyautogui.click(559, 715)   #Voltar para a primeira página
    print('Alterando para visualização Single Page...')
    time.sleep(1)
    pyautogui.click(1035, 709, clicks=2, interval=0.5)  #Single page
    time.sleep(1)
    pyautogui.click(1106, 478)  #Área em branco
    time.sleep(1)
    pyautogui.press("pagedown")
    time.sleep(1)
    print(f'Inserindo a imagem da embarcação {embarcacao}...')
    pyautogui.click(783, 378)   #Seleciona a imagem
    time.sleep(1)
    pyautogui.press("delete")
    time.sleep(1)
    pyautogui.click(334, 90)    #Adicionar imagem
    time.sleep(1)
    pyautogui.click(397, 108)   #Adicionar imagem 2°
    time.sleep(2)
    pyautogui.click("images\\editar_caminho_imagem.png")   #Editar caminho da imagem
    time.sleep(2)
    pyautogui.write('F:\\Python\\Bots_Python\\images\\vessels', interval=0.01)
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.click("images\\nome_imagem.png")
    time.sleep(3)
    pyautogui.write(f'{embarcacao}.jpg', interval=0.02)
    time.sleep(1)
    pyautogui.click("images\\abrir_imagem.png")   #Abrir imagem
    time.sleep(2)
    pyautogui.rightClick(490, 316)   #Propriedades da imagem da embarcação
    time.sleep(4)
    pyautogui.press('tab')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.click('images\\appearance.png')
    time.sleep(2)
    pyautogui.click('images\\general.png')
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(1)
    pyautogui.write('2.54', interval=0.01)
    time.sleep(1)
    pyautogui.press('tab')
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(1)
    pyautogui.write('2.79', interval=0.01)
    time.sleep(1)
    pyautogui.press('tab')
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(1)
    pyautogui.write('5', interval=0.01)
    time.sleep(1)
    pyautogui.press('tab')
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(1)
    pyautogui.write('2.9', interval=0.01)
    time.sleep(1)
    pyautogui.hotkey('alt', 'f4')
    time.sleep(1)
    print('Inserindo o nome da embarcação...')
    pyautogui.click(703, 556)   #Posiciona o mouse
    time.sleep(1)
    pyautogui.drag(-135, -64, duration=0.5)
    time.sleep(1)
    pyautogui.press('delete')
    time.sleep(1)
    pyautogui.click(325, 62)    #Adicionar texto
    time.sleep(1)
    pyautogui.click(580, 525)   #Seleciona o local para adicionar o texto
    time.sleep(1)
    pyautogui.write(f"{embarcacao}", interval=0.01)
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(1)
    pyautogui.click(680, 76)    #Editar o tamanho da fonte
    time.sleep(1)
    pyautogui.write("18", interval=0.01)
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    print('Inserindo a data do relatório...')
    pyautogui.click(325, 62)    #Adicionar texto
    time.sleep(1)
    pyautogui.click(580, 545)   #Seleciona o local para adicionar a data
    time.sleep(1)
    pyautogui.write(f'{dia} de {nome_mes.title()} de {ano}', interval=0.01)
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(1)
    pyautogui.click(680, 76)    #Editar o tamanho da fonte
    time.sleep(1)
    pyautogui.write("18", interval=0.01)
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.alert('Informações inseridas com sucesso!','Notificação', button= 'Continuar')
    time.sleep(1)

def sumario():
    zoom = "45.52"
    print("Inserindo sumário...")
    paginas_array = []
    nome_indices_array = []
    i = 1
    sair = False
    while sair == False:
        print(f"Digite o título do {i}° índice:")
        nome_indice = str(input())
        print(f"Digite a página do {i}° índice")
        pagina = int(input())
        nome_indices_array.append(nome_indice)
        paginas_array.append(pagina)
        i+=1
        break_loop = int(input("Existem mais índices?\n0 -> Não\n1 -> Sim\n-> "))
        if break_loop == 0:
            sair = True
        else:
            continue
    time.sleep(2)
    pyautogui.click(660, 712)   #Editar número de páginas
    time.sleep(2)
    pyautogui.write("2")
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(2)
    pyautogui.click("images\\indice.png")
    time.sleep(2)
    pyautogui.click(141, 406)
    time.sleep(1)
    pyautogui.hotkey("ctrl", "a")
    time.sleep(1)
    pyautogui.press("delete")
    time.sleep(1)
    for n in range(4):
        time.sleep(1)
        pyautogui.click(127, 210)
        time.sleep(1)
        if n == 0:
            pyautogui.write("01 - Objetivo", interval=0.01)
            time.sleep(1)
            pyautogui.press("enter")
        elif n == 1:
            pyautogui.write("02 - Principios da Termografia", interval=0.01)
            time.sleep(1)
            pyautogui.press("enter")
        elif n == 2:
            pyautogui.write("03 - Aplicacoes", interval=0.01)
            time.sleep(1)
            pyautogui.press("enter")
        elif n == 3:
            pyautogui.write("04 - Criterios de Localizacao", interval=0.01)
            time.sleep(1)
            pyautogui.press("enter")
    time.sleep(1)
    pyautogui.click(660, 712)   #Editar número de páginas
    time.sleep(1)
    pyautogui.write("3")
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(2)
    for n in range(3):
        time.sleep(1)
        pyautogui.click(127, 210)
        time.sleep(1)
        if n == 0:
            pyautogui.write("05 - Emissividade", interval=0.01)
            time.sleep(1)
            pyautogui.press("enter")
        elif n == 1:
            pyautogui.write("06 - Maxima Temperatura Admissivel", interval=0.01)
            time.sleep(1)
            pyautogui.press("enter")
        elif n == 2:
            pyautogui.write("07 - Tipos de Defeitos Encontrados", interval=0.01)
            time.sleep(1)
            pyautogui.press("enter")
    time.sleep(1)
    pyautogui.click(660, 712)   #Editar número de páginas
    time.sleep(1)
    pyautogui.write("4")
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(2)
    for n in range(4):
        time.sleep(1)
        pyautogui.click(127, 210)
        time.sleep(1)
        if n == 0:
            pyautogui.write("08 - Normalizacao do Relatorio", interval=0.01)
            time.sleep(1)
            pyautogui.press("enter")
        elif n == 1:
            pyautogui.write("09 - Equipamentos Utilizados", interval=0.01)
            time.sleep(1)
            pyautogui.press("enter")
        elif n == 2:
            pyautogui.write("10 - Recomendacoes", interval=0.01)
            time.sleep(1)
            pyautogui.press("enter")
        elif n == 3:
            pyautogui.write("11 - Conclusao", interval=0.01)
            time.sleep(1)
            pyautogui.press("enter")
    cont = 12
    for n in range(paginas_array.__len__()):
        time.sleep(1)
        pyautogui.click(660, 712)   #Editar número de páginas
        time.sleep(1)
        pyautogui.write(str(paginas_array[n]), interval=0.01)
        time.sleep(1)
        pyautogui.press("enter")
        time.sleep(2)
        pyautogui.click(127, 210)
        time.sleep(1)
        pyautogui.write(f"{cont} - {str(nome_indices_array[n])}", interval=0.01)
        time.sleep(1)
        pyautogui.press("enter")
        cont+=1
    time.sleep(1)
    pagina_assinaturas = tasks.count_pages()
    pagina_assinaturas -= 1
    time.sleep(1)
    pyautogui.write(str(pagina_assinaturas), interval=0.01)
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(2)
    pyautogui.click(127, 210)
    time.sleep(1)
    pyautogui.write(f"{cont} - Assinaturas", interval=0.02)
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(1)
    pyautogui.click(48, 211)    #Adicionar Sumário
    time.sleep(2)
    pyautogui.click("images\\new_toc_from_bookmarks.png")
    time.sleep(2)
    pyautogui.press("enter")
    time.sleep(1)
    pyautogui.press("home")
    time.sleep(1)
    pyautogui.click(18, 286)    #Páginas
    time.sleep(1)
    pyautogui.click(147, 284)   #Selecionar página
    time.sleep(1)
    pyautogui.drag(0, 260, duration=0.5)
    time.sleep(1)
    pyautogui.click("images\\hide.png")
    time.sleep(1)
    pyautogui.click(660, 712)   #Editar número de páginas
    time.sleep(1)
    pyautogui.write("2")
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(1)
    print('Home...')
    pyautogui.click(95, 42)     #Home
    time.sleep(1)
    print('Alterando para visualização Single Page...')
    pyautogui.click(1035, 709)  #Single page
    time.sleep(1)
    tasks.zoom_adjust(zoom)
    time.sleep(1)
    pyautogui.click(226, 36)    #Editar
    time.sleep(1)
    pyautogui.click(103, 74)    #Editar Texto
    time.sleep(1)
    pyautogui.click(699, 220)
    time.sleep(1)
    pyautogui.hotkey("ctrl", "a")
    time.sleep(1)
    pyautogui.write("Sumario", interval=0.02)
    time.sleep(1)
    pyautogui.hotkey("ctrl", "a")
    time.sleep(1)
    pyautogui.click(682, 73)
    time.sleep(1)
    pyautogui.write("22", interval=0.02)
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(1)
    pyautogui.click(1073, 430)  #Área em branco
    time.sleep(1)
    pyautogui.click(660, 712)   #Editar número de páginas
    time.sleep(1)
    pyautogui.write(str(pagina_assinaturas+1), interval=0.05)
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(1)
    print("Editar...")
    pyautogui.click(225, 37)    #Editar
    time.sleep(1)
    print("Editar Texto...")
    pyautogui.click(105, 73)    #Editar Texto
    time.sleep(1)
    pyautogui.click(550, 242)   #Editar índice das assinaturas
    time.sleep(1)
    pyautogui.hotkey("shiftleft", "home")
    time.sleep(1)
    pyautogui.write(str(cont), interval=0.02)
    time.sleep(1)
    pyautogui.click(1073, 430)  #Área em branco
    time.sleep(1)
    pyautogui.alert("Sumário criado com sucesso!", "Notificação", "Continuar")
    

def salvar():
    print("Salvando relatório...")
    ano = int(input("Digite o ano do relatório (número inteiro): "))
    mes = int(input("Digite o mês do relatório (número inteiro): "))
    dia = int(input("Digite o dia do relatório (número inteiro): "))
    embarcacao = str(input("Digite o nome da embarcação: "))
    time.sleep(2)
    pyautogui.click(266, 370)   #Área em branco
    time.sleep(2)
    pyautogui.hotkey("ctrl", "s")
    time.sleep(3)
    pyautogui.click("images\\editar_caminho_imagem.png")
    time.sleep(1)
    pyautogui.write("F:\\Python\\Bots_Python\\relatorio_finalizado", interval=0.02)
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(1)
    for n in range(6):
        pyautogui.press("tab")
        time.sleep(0.5)
    pyautogui.write(f"{ano}{mes}{dia}_Termografia_{embarcacao}", interval=0.02)
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(1)
    pyautogui.hotkey("winleft", "r")
    time.sleep(2)
    pyautogui.write("F:\\Python\\Bots_Python\\relatorio_finalizado", interval=0.02)
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(1)
    hoje = datetime.datetime.today()
    hoje_formatado = hoje.strftime("%d/%m/%Y %H:%M:%S")
    pyautogui.alert(f"""RELATÓRIO FINALIZADO!
                    \nEmbarcação: {embarcacao}
                    \nData do relatório: {dia}/{mes}/{ano}
                    \nCriado em: {hoje_formatado}
                    \nDesenvolvedor: João Pedro Rodrigues""", "Notificação")
