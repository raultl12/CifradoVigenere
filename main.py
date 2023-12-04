import vigenere

txt = input("Texto: ")
clave = input("Clave: ")

vigenere = vigenere.Vigenere()

cifrado = vigenere.Cifrar(txt, clave)
print("Cifrado: " + cifrado)

descifrado = vigenere.Descifrar(cifrado, clave)
print("Descifrado: " + descifrado)