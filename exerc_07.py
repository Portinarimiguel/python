materia = input("digite o nome da materia: ")

nota = []
for i in range(1, 5):
  notas = float(input("digite a nota {}: ".format(i)))
  nota.append(notas)
  media = sum(nota) / len(nota)
  if media >= 7:
    print("aprovado")
  else:
    print("reprovado")

print(f"a media da materia {materia} é: {media}")