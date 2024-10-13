### Exercício 1: Verificação de Qualidade de Dados
# Você está analisando um conjunto de dados de vendas e precisa garantir 
# que todos os registros tenham valores positivos para `quantidade` e `preço`. 
# Escreva um programa que verifique esses campos e imprima "Dados válidos" se ambos 
# forem positivos ou "Dados inválidos" caso contrário.

#try:
#    q_produto = int(input("Digite a quantidade de produtos: "))
#    preco = float(input("Digite o preço: "))
#
#    if q_produto >= 0 and preco >= 0:
#        print("Dados válidos")
#    else:
#        print("Dados inválidos")

#except ValueError:
#    print("Dado invalido")

### Exercício 2: Classificação de Dados de Sensor
# Imagine que você está trabalhando com dados de sensores IoT. 
# Os dados incluem medições de temperatura. Você precisa classificar cada leitura 
# como 'Baixa', 'Normal' ou 'Alta'. Considerando que:
#Temperatura < 18°C é 'Baixa'
#Temperatura >= 18°C e <= 26°C é 'Normal'
#Temperatura > 26°C é 'Alta'

#try:
#    temperatuda = float(input("Digite uma temperatura em celsius: "))
#
#    if temperatuda < 18:
#        print((f"{temperatuda} é uma temperatura baixa"))
#    elif temperatuda > 26:
#        print((f"{temperatuda} é uma temperatura alta"))
#    else:
#        print((f"{temperatuda} é uma temperatura normal"))
#except ValueError:
#    print("Digite um valor válido")

### Exercício 3: Filtragem de Logs por Severidade
# Você está analisando logs de uma aplicação e precisa filtrar mensagens 
# com severidade 'ERROR'. Dado um registro de log em formato de dicionário 
# como `log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}`, 
# escreva um programa que imprima a mensagem se a severidade for 'ERROR'.

#log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}

#if log['level'] == 'ERROR':
#    print(log['message'])

### Exercício 4: Validação de Dados de Entrada
# Antes de processar os dados de usuários em um sistema de recomendação, 
# você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e tenha 
# fornecido um email válido. Escreva um programa que valide essas condições 
# e imprima "Dados de usuário válidos" ou o erro específico encontrado.

#idade = int(input("Digite sua idade: "))
#email = str(input("Digite seu melhor e-mail: "))

#if idade < 18 and idade < 65:
#    print("Idade não permitida")
#elif "@" not in email or ".com" not in email:
#    print("O email não é valido")
#else:
#    print("Dados de usuário válidos")

### Exercício 5: Detecção de Anomalias em Dados de Transações
# Você está trabalhando em um sistema de detecção de fraude e precisa identificar 
# transações suspeitas. Uma transação é considerada suspeita se o valor for superior 
# a R$ 10.000 ou se ocorrer fora do horário comercial (antes das 9h ou depois das 18h). 
# Dada uma transação como `transacao = {'valor': 12000, 'hora': 20}`, verifique se ela é suspeita.

#transacao = {'valor': 12000, 'hora': 20}

#if transacao['valor'] > 10000 and (transacao['hora'] > 18 or transacao['hora'] < 6):
#    print('Essa é uma transação suspeita')
#else:
#    print("Transação segura")

### Exercício 6. Contagem de Palavras em Textos
# Objetivo:** Dado um texto, contar quantas vezes cada palavra única aparece nele.

#frase  = input("Escreva uma frase: ")

#palavras = frase.replace(',', "").split()
#contagem_palavras = {}

#for palavra in palavras:
#    if palavra in contagem_palavras:
#        contagem_palavras[palavra] = contagem_palavras[palavra] + 1
#    else:
#        contagem_palavras[palavra] = 1
#    print(contagem_palavras)

#print(contagem_palavras)

### Exercício 7. Normalização de Dados
# Objetivo:** Normalizar uma lista de números para que fiquem na escala de 0 a 1.

#numeros = [1, 2, 3, 4, 5]

#minimo = min(numeros)
#maximo = max(numeros)
#normalizados = [(x - minimo) / (maximo - minimo) for x in numeros]

#print(normalizados)

### Exercício 8. Filtragem de Dados Faltantes
# Objetivo:** Dada uma lista de dicionários representando dados de usuários, filtrar aqueles que têm um campo específico faltando

#usuario = [
#    {"nome" : "lucas", "user_id": ""},
#    {"nome" : "lais", "user_id": "124"},
#    {"nome" : "carol", "user_id": "123"}
#]

#for x in usuario:
#    if x["user_id"] == "":
#        print(f"usuairo {x['nome']} não possui user_id ")
#    else:
#        print(f"usuairo {x['nome']} possui user_id")

### Exercício 9. Extração de Subconjuntos de Dados
# Objetivo:** Dada uma lista de números, extrair apenas aqueles que são pares.

#numeros = [1, 2, 3, 4, 5]

#extracao_numero = []

#for x in numeros:
#    if x % 2 == 0:
#        extracao_numero.append(x)

#print(extracao_numero)

        
### Exercício 10. Agregação de Dados por Categoria
# Objetivo:** Dado um conjunto de registros de vendas, calcular o total de vendas por categoria.

#vendas = [
#    {"categoria": "shop", "vendas": 2},
#    {"categoria": "shop", "vendas": 5},
#    {"categoria": "shop", "vendas": 3},
#    {"categoria": "mercado", "vendas": 1},
#    {"categoria": "mercado", "vendas": 5},
#    {"categoria": "mercado", "vendas": 2},
#]

#vendas_shop = 0
#vendas_mercado = 0

#for x in vendas:
#    if x["categoria"] == "shop":
#        vendas_shop = vendas_shop + x["vendas"]
#    else:
#        vendas_mercado = vendas_mercado + x["vendas"]

#print(f"Quantida de vendas por merdaco: {vendas_mercado}, por shop: {vendas_shop}")
### Exercícios com WHILE

### Exercício 11. Leitura de Dados até Flag
# Ler dados de entrada até que uma palavra-chave específica ("sair") seja fornecida.

#esposta = ""

#while resposta.lower() != "sair":
#    resposta = input("Gostaria de continuar, ou gostaria de sair (digite sair)? ")

### Exercício 12. Validação de Entrada
# Solicitar ao usuário um número dentro de um intervalo específico até que a entrada seja válida.

#result = int(input("Digite um número entre 1 e 10: "))

#while (result < 1 or result > 10):
#    result = int(input("Digite um número entre 1 e 10: "))


### Exercício 13. Consumo de API Simulado
# Simular o consumo de uma API paginada, onde cada "página" de dados é processada em loop até que não haja mais páginas.

#atual_pagina = 1
#total_paginas = 5

#while atual_pagina != total_paginas:
#    print(f"Página {atual_pagina} processada")
#    atual_pagina = atual_pagina + 1

#print("Todas páginas foram processadas")

### Exercício 14. Tentativas de Conexão
# Simular tentativas de reconexão a um serviço com um limite máximo de tentativas.

#limit = 5
#tentativa = 0
#
#while tentativa != limit:
#    print(f"Tentando se conectar... {tentativa}")
#    tentativa = tentativa + 1

### Exercício 15. Processamento de Dados com Condição de Parada
# Processar itens de uma lista até encontrar um valor específico que indica a parada.

#frase = input("Digite uma frase: ")

#lista = frase.split()

#n = 0

#while lista[n] != "parar":
#    print(f"Processando lista... {lista[n]}")
#    n = n + 1
#    if lista == 'parar':
#        print("Encerrando processamento")
    
