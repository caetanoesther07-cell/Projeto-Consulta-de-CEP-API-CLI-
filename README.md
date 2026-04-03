',  # 📍 Consulta de CEP com Python

Projeto desenvolvido em Python que realiza a **consulta de endereços a partir de um CEP**, utilizando integração com API externa. O sistema funciona via terminal (CLI) e retorna informações completas do endereço de forma rápida e prática.

---

## 🚀 Funcionalidades

* Consulta de CEP em tempo real
* Integração com API externa (ViaCEP)
* Exibição de:

  * Rua
  * Bairro
  * Cidade
  * Estado
* Tratamento de erros (CEP inválido ou inexistente)
* Menu interativo no terminal

---

## 🛠️ Tecnologias utilizadas

* Python 3
* Biblioteca `requests`
* API ViaCEP

---

## ▶️ Como executar o projeto

1. Clone este repositório:

```bash
git clone https://github.com/seu-usuario/consulta-cep-python.git
```

2. Acesse a pasta:

```bash
cd consulta-cep-python
```

3. Instale as dependências:

```bash
pip install requests
```

4. Execute o projeto:

```bash
python consulta_cep.py
```

---

## 💻 Estrutura do projeto

```
consulta-cep-python/
│
├── consulta_cep.py
└── README.md
```

---

## 🧠 Conceitos aplicados

* Consumo de API (requisições HTTP)
* Manipulação de JSON
* Tratamento de exceções (`try/except`)
* Estrutura de funções
* Entrada e saída de dados

---

## ⚠️ Possíveis melhorias

* Validação de CEP (apenas números e 8 dígitos)
* Histórico de consultas
* Salvamento em arquivo `.json`
* Interface gráfica (GUI)
* Transformar em API com Flask

---

## 📌 Objetivo

Este projeto tem como objetivo praticar conceitos de programação e demonstrar conhecimentos básicos em integração com APIs, sendo ideal para portfólio de iniciantes na área de desenvolvimento.

---

## 👩‍💻 Autora

Desenvolvido por Esther Caetano
📧 [caetanoesther07@gmail.com](mailto:caetanoesther07@gmail.com)
