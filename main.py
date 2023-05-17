dia_inicial = 1
dias_finais = int(input("Por quantos dias deseja lucrar 1%?: "))
montante = float(input("Qual o montante?: "))

print("Juros:")
while dia_inicial <= dias_finais:
  print("{:.2f} - {}".format(montante, dia_inicial))
  if dia_inicial == dias_finais:
    break
  else:
    dia_inicial += 1
    montante = montante * 1.01

print("Ao final voce tera um total de: {:.2f} reais".format(montante))
