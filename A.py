# Escrevendo Olá, mundo!
#'Olá, mundo!' - Português
def escrevaEntreLinhas(texto):
    tamanho = len(texto) + 2
    print("\033[4m_\033[m" * tamanho)
    print(f" \033[1m{texto}\033[m ")
    print("\033[9m_\033[m" * tamanho)


print("Por favor faça o que lhe for solicitado:")
while True:
    frase = 'Olá, mundo!'
    texto = input("escreva 'Olá, mundo!'\n").lower().strip()
    if texto == frase.lower():
        escrevaEntreLinhas('Parabéns, escreveu certo!!!')
        break
    else:
        escrevaEntreLinhas('Não era bem isso que você deveria escrever...')

escrevaEntreLinhas('Volte sempre!')
