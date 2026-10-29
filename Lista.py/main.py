
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
    st.write(lista.regiao_ordenada)

st.write("**Cauda não ordenada:**")
st.write(lista.cauda if lista.cauda else "Cauda vazia.")

st.divider()

st.subheader("Componentes Streamlit utilizados")

st.write("""
- `st.title()`: título da aplicação.
- `st.write()`: exibe textos e listas.
- `st.columns()`: organiza informações em colunas.
- `st.metric()`: mostra quantidades.
- `st.form()`: agrupa campos e botões.
- `st.number_input()`: recebe números.
- `st.form_submit_button()`: executa inserções e buscas.
- `st.success()` e `st.error()`: exibem mensagens.
- `st.expander()`: permite expandir a região ordenada.
""")

st.subheader("Trechos de código dos componentes")

st.code('st.title("Lista Ordenada e Cauda Não Ordenada")', language="python")
st.code('st.number_input("Digite um número inteiro", value=150000, step=1)', language="python")
st.code('st.metric("Total de iterações", resultado["total"])', language="python")

if st.button("Reiniciar aplicação"):
    st.session_state.lista = ListaDividida()
    st.rerun()
