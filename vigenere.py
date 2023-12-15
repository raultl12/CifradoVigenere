class Vigenere:

    def ExtenderClave(self, mensaje, clave):
        # Extender la clave para que tenga la misma longitud que el mensaje
        claveExtendida = clave
        for i in range(len(mensaje) - len(clave)):
            claveExtendida += clave[i % len(clave)]

        return claveExtendida

    def QuitarEspacios(self, mensaje):
        # Quitar espacios del mensaje
        mensaje = mensaje.replace(' ', '')
        return mensaje
    
    def Cifrar(self, mensaje, clave):
        # Cifrar usando solo el diccionario
        mensaje = self.QuitarEspacios(mensaje.upper())
        clave = self.QuitarEspacios(clave.upper())
        self.clave = self.ExtenderClave(mensaje, clave)
        cifrado = ''
        for i in range(len(mensaje)):
            num_letraTexto = self.dict[mensaje[i]]
            num_letraClave = self.dict[self.clave[i]]
            cifrado += self.numCh[(num_letraTexto + num_letraClave) % len(self.dict)]

        return cifrado
    
    def Descifrar(self, mensaje, clave):
        # Descifrar usando solo el diccionario
        mensaje = mensaje.upper()
        clave = clave.upper()
        descifrado = ''
        for i in range(len(mensaje)):
            letraTexto = self.dict[mensaje[i]]
            letraClave = self.dict[self.clave[i]]
            descifrado += self.numCh[(letraTexto - letraClave) % len(self.dict)]
        return descifrado

    def __init__(self):
        self.dict = {
            'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4,
            'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9,
            'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14,
            'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19,
            'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24,
            'Z': 25
        }

        
        self.numCh = {
            0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E',
            5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J',
            10: 'K', 11: 'L', 12: 'M', 13: 'N', 14: 'O',
            15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T',
            20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y',
            25: 'Z'
        }

        self.clave = None
