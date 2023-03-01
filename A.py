# Escrevendo "Olá, mundo!" em Portugês e em python
def escrevaEntreLinhas(texto):
    tamanho = len(texto) + 2
    print("\033[4m_\033[m" * tamanho)
    print(f" \033[1m{texto}\033[m ")
    print("\033[9m_\033[m" * tamanho)

print("Por favor faça o que lhe for solicitado:")
print("Este programa apenas ira conferir se voce tem a capacidade de reescrever um texto que será exibido na tela")

print("Por favor, copie exatamente da forma que está escrita, incluindo acentos, caracteres especiais, e etc...")

print("O uso incorreto de maiúsculas e minusculas é permitido, porem sera considerado para o resultado final")
while True:
    frase = 'Olá, mundo!'
    texto = input("escreva 'Olá, mundo!'\n").lower().strip()
    if texto == frase.lower():
        escrevaEntreLinhas('Parabéns, escreveu certo!!!')
        break
    else:
        escrevaEntreLinhas('Não era bem isso que você deveria escrever...')

escrevaEntreLinhas('Volte sempre!')

#-------------------------Faculdade---------------------------------
def escrevaEntreLinhas(texto):
    tamanho = len(texto) + 2
    print("\033[4m_\033[m" * tamanho)
    print(f" \033[1m{texto}\033[m ")
    print("\033[9m_\033[m" * tamanho)

print("\033[4m_\033[m" * 45)
print("Ecolha um representante para lider de turma:\n"
"Candidato1 = 1\nCandidato2 = 2\nCandidato3 = 3\nCandidato4 = 4\nCandidato5 = 5")
print("\033[9m_\033[m" * 45)


while True:
    quantidadeDeAlunos = int(input("Quantos alunos tem na sala?"))
    if quantidadeDeAlunos < 0 or quantidadeDeAlunos == 0:
        print("Quantidade inexistente")
    else:
        break

votoCandidato1 = 0
votoCandidato2 = 0
votoCandidato3 = 0
votoCandidato4 = 0
votoCandidato5 = 0
quantidadeDeVotos = 0

while True:
    if quantidadeDeVotos == quantidadeDeAlunos:
        break
    print("\nAperte [1] Para votar em 'Candidato1'"
    "\nAperte [2] Para votar em 'Candidato2'"
    "\nAperte [3] Para votar em 'Candidato3'"
    "\nAperte [4] Para votar em 'Candidato4'"
    "\nAperte [5] Para votar em 'Candidato5'")
    voto = int(input("Qual o seu voto? "))
    voto = int(input("Qual o seu voto? "))
    if voto == 1:
        while True:
            confirmar = input("Tem certeza que deseja votar em candidato1? [S/N]").upper()[0]
            if confirmar == "S":
                escrevaEntreLinhas("Voto confirmado para candidato 1!")
                votoCandidato1 += 1
                quantidadeDeVotos += 1
                break
            elif confirmar == "N":
                print("Voltando Sistema")
                break
            else:
                print("Resposta inválida\n")
    elif voto == 2:
        while True:
            confirmar = input("Tem certeza que deseja votar em candidato2? [S/N]").upper()[0]
            if confirmar == "S":
                escrevaEntreLinhas("Voto confirmado para candidato 2!")
                votoCandidato2 += 1
                quantidadeDeVotos += 1
                break
            elif confirmar == "N":
                print("Voltando Sistema")
                break
            else:
                print("Resposta inválida\n")
    elif voto == 3:
        while True:
            confirmar = input("Tem certeza que deseja votar em candidato3? [S/N]").upper()[0]
            if confirmar == "S":
                escrevaEntreLinhas("Voto confirmado para candidato 3!")
                votoCandidato3 += 1
                quantidadeDeVotos += 1
                break
            elif confirmar == "N":
                print("Voltando Sistema")
                break
            else:
                print("Resposta inválida\n")
    elif voto == 4:
        while True:
            confirmar = input("Tem certeza que deseja votar em candidato4? [S/N]").upper()[0]
            if confirmar == "S":
                escrevaEntreLinhas("Voto confirmado para candidato 4!")
                votoCandidato4 += 1
                quantidadeDeVotos += 1
                break
            elif confirmar == "N":
                print("Voltando Sistema")
                break
            else:
                print("Resposta inválida\n")
    elif voto == 5:
        while True:
            confirmar = input("Tem certeza que deseja votar em candidato5? [S/N]").upper()[0]
            if confirmar == "S":
                escrevaEntreLinhas("Voto confirmado para candidato 5!")
                votoCandidato5 += 1
                quantidadeDeVotos += 1
                break
            elif confirmar == "N":
                print("Voltando Sistema")
                break
            else:
                print("Resposta inválida\n")
    else:
        escrevaEntreLinhas("voto inválido")

print("\033[4m_\033[m" * 30)
print(f"Quantidade de votos: \nCandidato 1: {votoCandidato1}\nCandidato 2: {votoCandidato2}\nCandidato 3: {votoCandidato3}\nCandidato 4: {votoCandidato4}\nCandidato 5: {votoCandidato5}")
print("\033[9m_\033[m" * 30)
