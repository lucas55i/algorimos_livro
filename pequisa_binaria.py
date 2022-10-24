def pesquisa_binaria(lista, item):
    baixo = 0  # baixo  e alto acompanham a parte da lista que voce está proucurando
    # baixo  e alto acompanham a parte da lista que voce está proucurando
    alto = len(lista) - 1

    while baixo <= alto:  # Entquanto ainda não conseguiu chegar a um único elemento
        meio = (baixo + alto) / 2  # ...Verifica o elemento central.
        chute = lista[meio]
        if chute == item:  # Acha o item.
            return meio
        if chute > item:  # O chute foi muito alto
            alto = meio - 1
        else:  # O chute foi muito baixo
            baixo = meio + 1
    return None  # O item não existe


minha_lista = [1, 3, 5, 7, 9]  # vamos testá-lo
# Lembre-se, as listas começam no 0. O  próximo endereço tem índice 1
print(pesquisa_binaria(minha_lista, 3))
# "None" significa nulo em python. Ele indica que o item não foi encontrado.
print(pesquisa_binaria(minha_lista, -1))
