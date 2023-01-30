# Escrevendo Olá, mundo!
#'Olá, mundo!' - Português
def escrevaEntreLinhas(texto):
    print("________________")
    print(texto)
    print("________________")
texto = input("escreva 'Olá, mundo!'\n")
while True:
    if texto == 'Olá, mundo!':
        input(texto)
        print("\nParabéns, escreveu certo!!!\n")
        escrevaEntreLinhas(texto)
        break
    else:
        print("Não era bem isso que você deveria escrever...\n")
print("________________")
print("Volte sempre!")
print("________________")

