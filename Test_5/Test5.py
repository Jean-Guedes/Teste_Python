# Função que inverte os caracteres de uma string, retorna a string invertida.
def inverter_string(texto):
    texto_invertido = ""
    for caractere in texto:
        texto_invertido = caractere + texto_invertido
    return texto_invertido

# MAIN:
string = input("Digite a String para se invertida:  ")
print(inverter_string(string))
