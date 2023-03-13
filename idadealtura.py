idades = []
alturas = []

for i in range(5):
    idade = int(input("Digite a idade da pessoa {}: ".format(i+1)))
    altura = float(input("Digite a altura da pessoa {} (em metros): ".format(i+1)))
    idades.append(idade)
    alturas.append(altura)

print("Idades em ordem inversa:")
for idade in reversed(idades):
    print(idade)

print("\nAlturas em ordem inversa:")
for altura in reversed(alturas):
    print("{:.2f}m".format(altura))
