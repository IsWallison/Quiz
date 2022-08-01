def perguntas():
    contador = 0
    questoes = {
        'Normalmente, quantos litros de sangue uma pessoa tem? ': '\n 1 - Tem entre 2 a 4 litros\n 2 - Tem entre 4 a 6 litros\n 3 - Tem 10 litros\n 4 - Tem 7 litros\n 5 - Tem 0,5 litros. ',
        'De quem é a famosa frase “Penso, logo existo”? ': '\n 1 - Platão \n 2 - Galileu Galilei\n 3 - Descartes\n 4 - Sócrates\n 5 - Francis Bacon',
        'De onde é a invenção do chuveiro elétrico?': '\n 1 - França\n 2 - Inglaterra\n 3 - Brasil\n 4 - Austrália\n 5 - Itália',
        'Quais o menor e o maior país do mundo?' :'\n 1 - Vaticano e Rússia\n 2 - Nauru e China\n 3 - Mônaco e Canadá\n 4 - Malta e Estados Unidos\n 5 - São Marino e Índia',
        'Qual o nome do presidente do Brasil que ficou conhecido como Jango?' : '\n 1 - Jânio Quadros\n 2 - Jacinto Anjos\n 3 - Getúlio Vargas\n 4 - João Figueiredo\n 5 - João Goulart' }
    correta = [ 2, 3, 3, 1, 5]
    resultado = []
    for i, k in questoes.items():
        print(i, k)
        resposta = int(input('Selecione uma opção: [1 ~ 5]: '))
        while resposta not in range(1,6):
            if resposta <= 0 or resposta >= 6:
                print('Opção inválida. Selecione a opção desejada entre "1 e 5"')
            resposta = int(input('Selecione uma opção: [1 ~ 5]: '))
        resultado.append(resposta)
    for cont in range(len(correta)):
        if correta[cont] == resultado [cont]:
            contador += 1
            
    print(f'Voce acertou {contador} respostas ')
    sair = input('Aperte entrer para sair: ') #Nao fechar automaticamente no executavel 

perguntas()
