def cryptage(chaine,cle):
    alpha ="abcdefghijklmnopqrstuvwxyz0123456789"
    liste = ''
    for caractere in chaine:
        try:
            index=alpha.index(caractere)
            numero=index + cle
            cle= cle + cle
            if cle > 35:
                cle=cle-35
            if numero > 35:
                numero=numero-35
            liste+=alpha[numero]
        except:
            liste+=caractere
    return liste     
def decryptage (chaine,cle):
    alpha = "abcdefghijklmnopqrstuvwxyz0123456789"
    liste = ''
    for caractere in chaine:
        try:
            index=alpha.index(caractere)
            numero=index - cle
            cle= cle + cle
            if cle > 35:
                cle= cle - 35
            if numero < 0:
                numero = numero+35
            liste+=alpha[numero]
        except:
            liste+=caractere
    return liste

