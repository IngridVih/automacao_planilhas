from openpyxl import Workbook
import smtplib
from email.message import EmailMessage

# --- 1. Criar a planilha Excel a partir do arquivo TXT ---
planilha_contas = Workbook()
pagina1 = planilha_contas.active

with open('anotações.txt', 'r', encoding='utf-8') as arquivo:
    for linha in arquivo:
        pagina1.append(linha.strip().split(','))

planilha_contas.save('contas_a_pagar.xlsx')
print("Planilha criada com sucesso!")

# --- 2. Preparar o e-mail ---
msg = EmailMessage()
msg['Subject'] = 'Planilha de Contas a Pagar'
msg['From'] = 'SEUEMAIL597@gmail.com'
msg['To'] = 'EMAILDESTINATARIO@gmail.com'
msg.set_content('Segue em anexo a planilha de contas a pagar.')

# Anexa o arquivo Excel
with open('contas_a_pagar.xlsx', 'rb') as f:
    msg.add_attachment(
        f.read(),
        maintype='application',
        subtype='vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        filename='contas_a_pagar.xlsx'
    )

# --- 3. Enviar o e-mail via Gmail ---
try:
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login('SEUEMAIL@gmail.com', 'SUA SENHA')  # Use sua senha de app
        smtp.send_message(msg)
    print("E-mail enviado com sucesso!")
except Exception as e:
    print(f"Erro ao enviar e-mail: {e}")
