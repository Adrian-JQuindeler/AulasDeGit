# Escrevendo Olá, mundo!
#'Olá, mundo!' - Português
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
