nome_heroi = input("Qual é seu nome heroi?").strip()

def ler_int(prompt):
    while True:
        s = input(prompt).strip()
        try:
            return int(s)
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")

experiencia = ler_int("Quantos pontos de experiência você tem? ")

if experiencia < 1000:
    nivel_heroi = "Ferro"
elif experiencia < 2000:
    nivel_heroi = "Bronze"
elif experiencia < 5000:
    nivel_heroi = "Prata"
elif experiencia < 7000:
    nivel_heroi = "Ouro"
elif experiencia < 8000:
    nivel_heroi = "Platina"
elif experiencia < 9000:
    nivel_heroi = "Ascendente"
elif experiencia < 10000:
    nivel_heroi = "Imortal"
else:
    nivel_heroi = "Radiante"

print(f"O Herói de nome {nome_heroi} está no nível de {experiencia} e é classificado como {nivel_heroi}")
