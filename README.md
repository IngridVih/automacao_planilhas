# 📊 Automação de Planilha + Envio por E-mail

Este projeto lê dados de um arquivo `.txt` e de uma planilha Excel existente, gera uma nova planilha automaticamente e envia por e-mail via Gmail.

---

## 🚀 Funcionalidades

- Lê dados de um arquivo `anotações.txt`
- Lê dados de uma planilha Excel existente (`vendas_de_lanches.xlsx`)
- Cria uma planilha `contas_a_pagar.xlsx` combinando as informações
- Envia a planilha por e-mail como anexo

---

## 💻 Tecnologias utilizadas

- **Python 3.10+**
- **openpyxl** — para ler e criar planilhas `.xlsx`
- **smtplib** — para envio de e-mails via protocolo SMTP
- **email.message** — para criar e formatar a mensagem do e-mail

---

## 🧪 Pré-requisitos

- Python instalado na máquina
- Conta Gmail com **senha de app** ativada
- Pip funcionando corretamente

---

## 🛠 Como rodar na sua máquina

1. **Clone o repositório:**
```bash
git clone https://github.com/IngridVih/automacao_planilhas.git
cd automacao_planilhas
