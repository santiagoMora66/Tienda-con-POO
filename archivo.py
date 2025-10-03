import os

if os.path.exists('productos.dat'):
    print("el archivo existe :D")
    print("mira los productos")
    with open('productos.dat', 'r') as archivo:
        contenido = archivo.read()
    print(contenido)

    print("vamos a añadirle algunos productos")
    productos = input("que productos vas a añadir: ")
    with open('productos.dat', 'a') as archivo:
        archivo.write(f"{productos}\n")
else:
    print("no existe :/")
    print("vamooo a crearlo")
    with open('productos.dat', 'a') as archivo:
        archivo.write("ok\n")
    print("archivo creado :3")
