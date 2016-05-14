Name="Luis"
def Fun1(Name):
	if Name == "ola":
		print("Hey ola")
	elif Name == "Andrea":
		print("Hey Andrea")
	elif Name == "Luis":
		print("Hey Luis")
	else:
		print("Hey you")
Fun1(Name)
print("fuera")
Fun1("Andrea")
Fun1("ola")
Fun1("no")

Nombres=["Ana", "Luis", "Andrea", "Carlos"]
def Lista(Nombre):
	print (Nombre)
for Nombre in Nombres:
	Lista(Nombre)

Máximo=5
for Actual in range(1,Máximo):
	print(Actual)
	