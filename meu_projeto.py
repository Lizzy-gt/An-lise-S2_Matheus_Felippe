# Programa para verificar a altura do usuário e fornecer uma classificação

# Função para classificar a altura
def classificar_altura(altura):
    if altura < 1.60:
        return "baixo"
    elif 1.60 <= altura <= 1.80:
        return "normal"
    else:
        return "alto"

# Função para pedir a altura e garantir uma entrada válida
def obter_altura():
    while True:
        try:
            altura = float(input("Digite sua altura em metros (ex: 1.75): "))
            if altura <= 0:
                print("Por favor, insira uma altura válida maior que zero.")
            else:
                return altura
        except ValueError:
            print("Valor inválido! Por favor, insira um número.")

# Solicitar altura do usuário
altura_usuario = obter_altura()

# Classificar o usuário com base na altura
categoria = classificar_altura(altura_usuario)

# Exibir a classificação
print(f"Sua altura é {altura_usuario} metros, você é considerado {categoria}.")

# Exibir uma mensagem adicional dependendo da classificação
if categoria == "baixo":
    print("sua cor favorita á azul")
elif cor == "verde":
    print("sua cor favorit é verde")
else:
    print("você tem 30 anos de idade")