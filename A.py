# Escrevendo Olá, mundo!
#'Olá, mundo!' - Português
def escrevaEntreLinhas(texto):
    print("________________")
    print(texto)
    print("________________")
print("Este programa espera que você digite o texto solicitado extamebte como está escrito.\n")
while True:
    texto = input("escreva 'Olá, mundo!'\n")
    if texto == 'Olá, mundo!':
        print("\nParabéns, escreveu certo!!!\n")
        escrevaEntreLinhas(texto)
        break
    else:
        print("Não era bem isso que você deveria escrever...\n")
        print("escreva 'Olá, mundo!'\n")
        
print("________________")
print("Volte sempre!")
print("________________")

