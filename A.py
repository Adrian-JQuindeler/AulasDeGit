# Escrevendo Olá, mundo!
#'Olá, mundo!' - Português
def escrevaEntreLinhas(texto):
    print("________________")
    print(texto)
    print("________________")
print("Por favor faça o que lhe for solicitado:")
while True:
    frase = 'Olá, mundo!'
    texto = input("escreva 'Olá, mundo!'")
    if texto == frase:
        escrevaEntreLinhas('Parabéns, escreveu certo!!!')
        break
    else:
        print("Não era bem isso que você deveria escrever...\n")
        print("escreva 'Olá, mundo!'\n")
print("________________")
print("Volte sempre!")
print("________________")
