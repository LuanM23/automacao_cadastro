import pyautogui
import time
import pandas as pd


pyautogui.PAUSE = 0.5 # regra de espera entre comandos


#abrir navegador
pyautogui.press('win')
pyautogui.write('edge')
pyautogui.press('enter')

#entrar no link
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')
time.sleep(3)

#fazer login
#selecionar o campo de e-mail
pyautogui.click(x=397, y=359) 
pyautogui.write('luanmfernandes95@gmail.com')
pyautogui.press('tab')
pyautogui.write('123')
pyautogui.click(x=686, y=520)


#importar base de produtos
tabela = pd.read_csv(r'C:\Users\Acer\Downloads\Python Insights\Aula 2\produtos.csv')
print(tabela)
#cadastrar produto
for linha in tabela.index:
    #clicar no campo de código
    pyautogui.click(x=401, y=242)
    #pegar da tabela o valor do campo que queremos preencher
    codigo = tabela.loc[linha, 'codigo']
    #preencher o campo
    pyautogui.write(str(codigo)) #garantia string 
    #continuar o cadastro
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'marca']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'tipo']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'categoria']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'preco_unitario']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'custo']))
    pyautogui.press('tab')
    if not pd.isna(tabela.loc[linha, 'obs']):
        pyautogui.write(str(tabela.loc[linha, 'obs']))
    pyautogui.press('tab')
    pyautogui.press('enter')
    #dar scroll pra cima
    pyautogui.scroll(5000) #negativo desce a tela, positivo sobe a tela