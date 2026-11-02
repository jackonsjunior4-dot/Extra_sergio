import pandas as pd
import streamlit as st
from lista import ListaDividida

st.set_page_config(page_title="Lista Dividida", layout="wide")

if "lista" not in st.session_state:
    st.session_state.lista = ListaDividida()

lista = st.session_state.lista

st.title("Lista Ordenada e Cauda Não Ordenada")
st.write("Busca binária, busca sequencial e intercalação.")

col1, col2 = st.columns(2)

with col1:
    st.metric("Números na região ordenada", len(lista.regiao_ordenada))

with col2:
    st.metric("Números na cauda", f"{len(lista.cauda)} / 10")

st.divider()

st.subheader("Inserir número")

with st.form("inserir"):
    novo_numero = st.number_input(
        "Digite um número inteiro",
        value=150000,
        step=1
    )
    inserir = st.form_submit_button("Inserir")

if inserir:
    sucesso, mensagem = lista.inserir(int(novo_numero))

    if sucesso:
        st.success(mensagem)
        if len(lista.cauda) == 0:
            st.info("A cauda foi ordenada e intercalada à região principal.")
    else:
        st.error(mensagem)

st.divider()

st.subheader("Buscar número")

with st.form("buscar"):
    numero_busca = st.number_input(
        "Qual número deseja procurar?",
        value=150000,
        step=1,
        key="numero_busca"
    )
    pesquisar = st.form_submit_button("Buscar")

if pesquisar:
    resultado = lista.buscar(int(numero_busca))

    if resultado["encontrou"]:
        st.success(f"Encontrado em: {resultado['local']}")
    else:
        st.warning("Número não encontrado.")

    c1, c2, c3 = st.columns(3)

    c1.metric("Iterações binárias", resultado["binaria"])
    c2.metric("Iterações sequenciais", resultado["sequencial"])
    c3.metric("Total de iterações", resultado["total"])

st.divider()

st.subheader("Visualizar as listas")

with st.expander("Mostrar região ordenada"):
    tabela = pd.DataFrame({
        "Posição": range(len(lista.regiao_ordenada)),
        "Valor": lista.regiao_ordenada
    })
    st.dataframe(tabela, hide_index=True)

st.write("**Cauda não ordenada:**")
st.write(lista.cauda if lista.cauda else "Cauda vazia.")

st.divider()

st.subheader("Componentes Streamlit utilizados")

st.write("Cada componente abaixo é usado neste aplicativo, com o trecho de código correspondente.")

componentes = [
    (
        "st.set_page_config()",
        "Define o título da aba e o layout da página.",
        'st.set_page_config(page_title="Lista Dividida", layout="wide")'
    ),
    (
        "st.session_state",
        "Guarda a lista entre as interações, pois o Streamlit reexecuta o script a cada clique.",
        '''if "lista" not in st.session_state:
    st.session_state.lista = ListaDividida()'''
    ),
    (
        "st.title()",
        "Título principal da aplicação.",
        'st.title("Lista Ordenada e Cauda Não Ordenada")'
    ),
    (
        "st.write()",
        "Exibe textos e listas.",
        'st.write("Busca binária, busca sequencial e intercalação.")'
    ),
    (
        "st.subheader()",
        "Títulos das seções.",
        'st.subheader("Inserir número")'
    ),
    (
        "st.divider()",
        "Linha que separa as seções.",
        'st.divider()'
    ),
    (
        "st.columns()",
        "Organiza informações lado a lado.",
        'col1, col2 = st.columns(2)'
    ),
    (
        "st.metric()",
        "Mostra quantidades e iterações em destaque.",
        'st.metric("Total de iterações", resultado["total"])'
    ),
    (
        "st.form()",
        "Agrupa campos e botão, enviando tudo de uma vez.",
        'with st.form("inserir"):\n    ...'
    ),
    (
        "st.number_input()",
        "Campo para digitar números inteiros.",
        'st.number_input("Digite um número inteiro", value=150000, step=1)'
    ),
    (
        "st.form_submit_button()",
        "Botão que executa a inserção ou a busca.",
        'inserir = st.form_submit_button("Inserir")'
    ),
    (
        "st.success()",
        "Mensagem verde de sucesso.",
        'st.success(mensagem)'
    ),
    (
        "st.error()",
        "Mensagem vermelha de erro (chave repetida ou inválida).",
        'st.error(mensagem)'
    ),
    (
        "st.warning()",
        "Mensagem amarela quando a chave não é encontrada.",
        'st.warning("Número não encontrado.")'
    ),
    (
        "st.info()",
        "Mensagem azul avisando que a intercalação aconteceu.",
        'st.info("A cauda foi ordenada e intercalada à região principal.")'
    ),
    (
        "st.expander()",
        "Área que abre e fecha para mostrar a região ordenada.",
        'with st.expander("Mostrar região ordenada"):\n    ...'
    ),
    (
        "st.dataframe()",
        "Tabela com a posição e o valor de cada número da região ordenada.",
        '''tabela = pd.DataFrame({
    "Posição": range(len(lista.regiao_ordenada)),
    "Valor": lista.regiao_ordenada
})
st.dataframe(tabela, hide_index=True)'''
    ),
    (
        "st.code()",
        "Exibe os trechos de código desta seção.",
        'st.code(\'st.title("Lista Ordenada e Cauda Não Ordenada")\', language="python")'
    ),
    (
        "st.button() e st.rerun()",
        "Reinicia a aplicação com uma nova lista e recarrega a página.",
        '''if st.button("Reiniciar aplicação"):
    st.session_state.lista = ListaDividida()
    st.rerun()'''
    ),
]

for nome, descricao, trecho in componentes:
    st.markdown(f"**`{nome}`**: {descricao}")
    st.code(trecho, language="python")

if st.button("Reiniciar aplicação"):
    st.session_state.lista = ListaDividida()
    st.rerun()
