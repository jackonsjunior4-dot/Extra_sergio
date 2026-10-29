
from lista import ListaDividida


def criar_lista():
    lista = ListaDividida(tamanho_inicial=20)
    return lista


def test_lista_inicial():
    lista = criar_lista()

    assert len(lista.regiao_ordenada) == 20
    assert lista.regiao_ordenada == sorted(lista.regiao_ordenada)
    assert len(set(lista.regiao_ordenada)) == 20


def test_semente_reproduzivel():
    primeira = ListaDividida(tamanho_inicial=20, semente=42)
    segunda = ListaDividida(tamanho_inicial=20, semente=42)

    assert primeira.regiao_ordenada == segunda.regiao_ordenada


def test_inserir_numero():
    lista = criar_lista()

    sucesso, mensagem = lista.inserir(2000)

    assert sucesso
    assert 2000 in lista.cauda


def test_rejeitar_repetido():
    lista = criar_lista()
    lista.inserir(2000)

    sucesso, mensagem = lista.inserir(2000)

    assert not sucesso
    assert lista.cauda == [2000]


def test_busca_binaria():
    lista = criar_lista()
    numero = lista.regiao_ordenada[5]

    resultado = lista.buscar(numero)

    assert resultado["encontrou"]
    assert resultado["local"] == "Região ordenada"


def test_busca_sequencial():
    lista = criar_lista()
    lista.inserir(2000)

    resultado = lista.buscar(2000)

    assert resultado["encontrou"]
    assert resultado["local"] == "Cauda"


def test_numero_inexistente():
    lista = criar_lista()

    resultado = lista.buscar(2000)

    assert not resultado["encontrou"]
    assert resultado["total"] == (
        resultado["binaria"] + resultado["sequencial"]
    )


def test_decima_insercao():
    lista = criar_lista()

    for numero in range(2000, 2010):
        lista.inserir(numero)

    assert lista.cauda == []
    assert len(lista.regiao_ordenada) == 30
    assert lista.regiao_ordenada == sorted(lista.regiao_ordenada)


def test_inserir_apos_intercalacao():
    lista = criar_lista()

    for numero in range(2000, 2010):
        lista.inserir(numero)

    sucesso, mensagem = lista.inserir(3000)

    assert sucesso
    assert lista.cauda == [3000]
