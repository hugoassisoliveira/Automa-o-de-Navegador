# -*- coding: utf-8 -*-

# NO SPYDER ESSA BOMBA TA BUGADA OU O CAMINHO TÁ ERRADO ;-;
# POR ENQUANTO USAR A IDE NORMAL DO PYTHON MSM


from selenium import webdriver
from selenium.webdriver.common.by import By


browser = webdriver.Firefox() # abre o firefox
browser.get('https://automatetheboringstuff.com') # abre o site

elemento = browser.find_element(by=By.CSS_SELECTOR, value=".content-body > ul:nth-child(24) > li:nth-child(2) > a:nth-child(1)")
# aqui deve-se ir no local desejado e clicar em inspecionar elemento e
# copiar o css selector para incluir como value

elemento.click() # aqui ele vai clicar sozinho no botão

message = browser.find_element(by=By.ID, value="literals")
# o find element by id pega uma seção que é definida por um id e coloca
# o texto na variável. Para imprimir o texto é só usar o .text

print(message.text)

# para digitar em uma barra de entrada/inserção de dados
# usa primeiro o find_element
# depois que achar usar as funções send_keys('texto aqui') e submit()
elemento.send_keys('curso de automação')  # digita no campo de inserção de texto
elemento.submit() # o enter

# porém aqui corre o risco de entrar numa pagina de captcha onde será
# necessário intervenção humana

# pra voltar pra pagina anterior
browser.back()

# pra avançar pra q estava
browser.forward()

# pra fechar no final 
browser.quit()

# a documentação do selenium fica em python readthedoc