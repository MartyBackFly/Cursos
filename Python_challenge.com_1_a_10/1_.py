
# pasar caracteres dos lugares en el orden del abecedario .. a es c , b es d , etc 

#diccionario de remplazos 

# http://www.pythonchallenge.com/pc/def/map.html




def reemplazar_palabras(cadena, diccionario_reemplazos):
    nueva_cadena = ""
    for caracter in cadena:
        if caracter in diccionario_reemplazos:
            nueva_cadena += diccionario_reemplazos[caracter]
        else:
            nueva_cadena += caracter
    return nueva_cadena
# Ejemplo de uso
codigo_original = """
g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm 
jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj. http://www.pythonchallenge.com/pc/def/map.html """ 


codigo_original2 = """ feiauzroivgzbmpszazlutnwsdofbiwqidjbzshfrblqgsbydajygcbjcwggtdmfjeobhcmdlzxajvitekcgpkcf
wqbvkoixetpiiljanvqjjgtcpadjkgcbluaidgumcdskunujfcjhfmbzpkzsasdxsqqdqlaeisjezfjfdaoljapywxjthqjknnednxnsahxqedoeq
sdcmltcsnwakjxdtytfaalhlgabekfmyimwrkffydghiunlriwgkuzqljjbsxguytfsatejmdwkbfbzifdknpcqimvehxujkszbuyutmsompijjojsp
bwlroefiwmqrsjstdjhfwxhcnthsoosmjoqtufoxvpvpjkgiaqgofrhyufxxdnjiwtfqusbkdeakunjgkfnpibuklgjougnivhgixsnekxgrirbs
llpuaouvhzbilbjirmqqxtktgcnkdljoasnexwtgvwjegurngksokjtroovpcmykzgeolwynsyfideomflmkwmj """

diccionario_reemplazos = {
    "a":"c",
    "b":"d",
    "c":"e",
    "d":"f",
    "e": "g",
    "f": "h",
    "g": "i",
    "h": "j",
    "i": "k",
    "j": "l",
    "k": "m",
    "l": "n",
    "m": "o",
    "n": "p",
    "o": "q",
    "p": "r",
    "q": "s",
    "r": "t",
    "s": "u",
    "t": "v",
    "u": "w",
    "v": "x",
    "w": "y",
    "x": "z",
    "y": "a",
    "z": "b",
    
    
}

codigo_modificado = reemplazar_palabras(codigo_original, diccionario_reemplazos)
print(codigo_modificado)
