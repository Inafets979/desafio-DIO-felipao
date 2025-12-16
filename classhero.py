nome_heroi = input("Qual é seu nome heroi?")
Xprience = int(input("Quantos pontos de experiência você tem? "))


if Xprience < 1000:
    nivel_heroi = "Ferro"
elif Xprience >= 1001 and Xprience < 2000:
    nivel_heroi = "Bronze"
elif Xprience >= 2001 and Xprience < 5000:
    nivel_heroi = "Prata"
elif Xprience >= 5001 and Xprience < 7000:  
    nivel_heroi = "Ouro"
elif Xprience >= 7001 and Xprience < 8000:
    nivel_heroi = "Platina"
elif Xprience >= 8001 and Xprience < 9000:
    nivel_heroi = "Ascendente"        
elif Xprience >= 9001 and Xprience < 10000:
    nivel_heroi = "Imortal"
else:
    nivel_heroi = "Radiante"

print ("O Herói de nome ", nome_heroi, "está no nível de " , Xprience, "e é classificado como ", nivel_heroi)
