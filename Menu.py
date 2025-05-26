d = int(input("Escolha qual você deseja iniciar: \n 1 - Calculadora de IMC \n 2 - Contador de Moedas \n 3 - Viagem de Carro \n 4 - Posso Votar \n 5 - Situação Escolar\n"))

if d == 1:
  print("Calculadora de IMC iniciada \n")

  p = float(input("Qual seu peso? "))
  a = float(input("Qual sua altura? "))

  imc = p / (a * a)

  print("\n Seu IMC é:", imc)

elif d == 2:
  print("Contador de moedas iniciado \n")

  m1 = int(input("quantas moedas de $1? "))
  m50 = int(input("quantas moedas de $0.50? "))
  m25 = int(input("quantas moedas de $0.25? "))
  m10 = int(input("quantas moedas de $0.10? "))
  m05 = int(input("quantas moedas de $0.05? "))

  m1 = m1 * 1
  m50 = m50 * 0.50
  m25 = m25 * 0.25
  m10 = m10 * 0.10
  m05 = m05 * 0.05
  t = m1 + m50 + m25 + m10 + m05

  print("\n total de moedas $1: ", m1)
  print("total de moedas $0.50: ", m50)
  print("total de moedas $0.25: ", m25)
  print("total de moedas $0.10: ", m10)
  print("total de moedas $0.05: ", m05)
  print("total de R$", t)

elif d == 3:
  print("Viagem de carro iniciada \n")

  d = float(input("Distância da viagem (em km) "))
  v = float(input("Velocidade média esperada (em km/h) "))
  c = float(input("Consumo do carro (km por litro) "))
  p = float(input("Preço do combustível (por litro) "))

  t = d / v
  co = d / c
  cu = c * p

  print("\n tempo: ",t,"horas")
  print("consumo: ", co)
  print("custo: ", cu, "Reais")


elif d == 4:
  print("Posso votar iniciado \n")

  idade = int(input("qual sua idade? "))

  if idade <= 18:
    print(" \n você é menor de idade, ainda não pode votar!")
  else:
    print("\n você é maior de idade, já pode votar!")

elif d == 5:
  print("Situação escolar iniciada \n")

  nota = float(input("Qual a nota? "))
  if nota >= 6:
    print("\n Aprovado! Ótimo.")
  elif 4 <= nota < 6:
   print("\n Recuperação! Boa sorte.")
  else:
   print("\n Reprovado! melhore!")

else:
  print("Opção inválida, porfavor digite um das opções acima!")
