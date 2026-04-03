import requests

def consultar_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    
    try:
        resposta = requests.get(url)
        dados = resposta.json()

        if "erro" in dados:
            print("CEP não encontrado.")
            return

        print("\n📍 Endereço encontrado:")
        print(f"Rua: {dados['logradouro']}")
        print(f"Bairro: {dados['bairro']}")
        print(f"Cidade: {dados['localidade']}")
        print(f"Estado: {dados['uf']}")

    except Exception as e:
        print("Erro ao consultar API:", e)


def menu():
    while True:
        print("\n1. Consultar CEP")
        print("0. Sair")

        op = input("Escolha: ")

        if op == "1":
            cep = input("Digite o CEP (somente números): ")
            consultar_cep(cep)
        elif op == "0":
            break
        else:
            print("Opção inválida")


menu()