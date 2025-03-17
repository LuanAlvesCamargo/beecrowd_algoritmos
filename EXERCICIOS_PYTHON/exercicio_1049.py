# Neste problema, você deverá ler 3 palavras que definem o tipo de animal possível segundo o esquema abaixo, 
# da esquerda para a direita.  Em seguida conclua qual dos animais seguintes foi escolhido, 
# através das três palavras fornecidas.

# Entrada
# A entrada contém 3 palavras, uma em cada linha, necessárias para identificar o animal segundo a figura acima, 
# com todas as letras minúsculas.
# Saída
# Imprima o nome do animal correspondente à entrada fornecida.

word1 = input().strip()
word2 = input().strip()
word3 = input().strip()

if word1 == "vertebrado":
    if word2 == "ave":
        if word3 == "carnivoro":
            animal = "aguia"
        elif word3 == "onivoro":
            animal = "pomba"
    elif word2 == "mamifero":
        if word3 == "onivoro":
            animal = "homem"
        elif word3 == "herbivoro":
            animal = "vaca"
elif word1 == "invertebrado":
    if word2 == "inseto":
        if word3 == "hematofago":
            animal = "pulga"
        elif word3 == "herbivoro":
            animal = "lagarta"
    elif word2 == "anelideo":
        if word3 == "hematofago":
            animal = "sanguessuga"
        elif word3 == "onivoro":
            animal = "minhoca"

print(animal)