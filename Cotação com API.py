import requests

def pegar_cotacoes():
  #Informações da API
  chave_api = "9da9c096bc4611ab9052850a830b219a373fef50996ecd41489b2d6e33299644"
  todas_moedas= "USD-BRL,EUR-BRL,BTC-BRL,GBP-BRL,JPY-BRL"


  link_do_api = f"https://economia.awesomeapi.com.br/json/last/{todas_moedas}?{chave_api}"


  resultado = requests.get(link_do_api)

  print(resultado.status_code)
  resultado = resultado.json()

  
  #Varoles das moedas
  dolar = resultado["USDBRL"]["ask"]
  euro = resultado["EURBRL"]["ask"]
  bitcoin = resultado["BTCBRL"]["ask"]
  libra = resultado["GBPBRL"]["ask"]
  iene = resultado["JPYBRL"]["ask"]

  #Codigos das moedas
  code_dolar = resultado["USDBRL"]["code"]
  code_euro = resultado["EURBRL"]["code"]
  code_bitcoin = resultado["BTCBRL"]["code"]
  code_libra = resultado["GBPBRL"]["code"]
  code_iene = resultado["JPYBRL"]["code"]
  
  
  
  # Função de cotação
  def cotacoes(dolar,euro,bitcoin,libra,iene):
    
    opcao_de_cotacao = int(input(''' Escolha uma opção (Digite o número da opção):
    [1] Dolar
    [2] Euro
    [3] Bitcoin
    [4] Libra 
    [5] Iene
    [6] Sair\n'''))

                             
    if opcao_de_cotacao == 1:
      print(f"Valo do dolar: R$ {dolar}")
    elif opcao_de_cotacao == 2:
      print(f"Valor do euro: R$ {euro}")
    elif opcao_de_cotacao == 3:
      print(f"Valor do bitcoin: R$ {bitcoin}")
    elif opcao_de_cotacao == 4:
      print(f"Valor da libra: R$ {libra}")
    elif opcao_de_cotacao == 5:
      print(f"Valor do Iene: R$ {iene}")
    elif opcao_de_cotacao == 6:
      return
    else:
      print("Opção Inválida!")

  #Função de converter
  def converter(dolar,euro,bitcoin,libra,iene,resultado,code_dolar,code_euro,code_bitcoin,code_libra,code_iene):
    print('''Escolha as moedas que deseja converter (Digite o número da opção):
    [1] Dolar
    [2] Euro
    [3] Bitcoin
    [4] Libra 
    [5] Iene\n''')

    opcao_de_conversao1 = int(input("Moeda 1: "))
    opcao_de_conversao2 = int(input("Moeda 2: "))

    
    if opcao_de_conversao1 == 1:
      moeda1 = float(dolar)
      code_moeda1 = code_dolar
    elif opcao_de_conversao1 == 2:
      moeda1 = float(euro)
      code_moeda1 = code_euro
    elif opcao_de_conversao1 == 3:
      moeda1 = float(bitcoin)
      code_moeda1 = code_bitcoin
    elif opcao_de_conversao1 == 4:
      moeda1 = float(libra)
      code_moeda1 = code_libra
    elif opcao_de_conversao1 == 5:
      moeda1 = float(iene)
      code_moeda1 = code_iene
    else:
      print("Opção Inválida!")


    if opcao_de_conversao2 == 1:
      moeda2 = float(dolar)
      code_moeda2 = code_dolar
    elif opcao_de_conversao2 == 2:
      moeda2 = float(euro)
      code_moeda2 = code_euro
    elif opcao_de_conversao2 == 3:
      moeda2 = float(bitcoin)
      code_moeda2 = code_bitcoin
    elif opcao_de_conversao2 == 4:
      moeda2 = float(libra)
      code_moeda2 = code_libra
    elif opcao_de_conversao2 == 5:
      moeda2 = float(iene)
      code_moeda2 = code_iene
    else:
      print("Opção Inválida!")


    if moeda1 == moeda2:
      print("As moedas são iguais")
    valor_convertido = moeda1 / moeda2
    valor_reduzido = round(valor_convertido,2)
    
    print(f"{code_moeda1} custa atualmente: {code_moeda2} {valor_reduzido}")



  #Menu
  def menu():
    print(''' Escolha uma opção:
  [1] Ver cotações
  [2] Converter
  [3] Sair\n''')


  #Painel de opções 
  while True:
    menu()
    opcao = int(input())
    if opcao == 1:
      cotacoes(dolar,euro,bitcoin,libra,iene)
    elif opcao == 2:
      converter(dolar,euro,bitcoin,libra,iene,resultado,code_dolar,code_euro,code_bitcoin,code_libra,code_iene)
    elif opcao == 3:
      print("Obrigado!!")
      break



pegar_cotacoes()