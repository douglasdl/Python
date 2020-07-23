# Medir varias strings
palavras = ["gato", "janela", "programador"]
for p in palavras:
    print(p, len(p))


# Percorra a array para copia-la e adicionar um item no comeco
for p in palavras[:]:
    if len(p) > 6:
        palavras.insert(0, p)
print(palavras)
