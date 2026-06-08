## IMPORTAR O STREAMLIT

import streamlit as st

# Titulo principal da página
st.title('Minha primeira aplicação streamlit')

# Cabeçalho
st.header('Bem-vindo ao mundo Streamlit')

# Sub Cabeçalho
st.subheader('Vamos explorar essa ferramenta incrível')

# Texto genérico
st.write('Este é um texto simples usando o st.write')

# Texto formatado com markdadown
st.markdown('''
Este é um exemplo de **Markdown** no Streamlit.
Podemos usar o **negrito**, *italico* e até mesmo **listas**:
* Item 1
* Item 2
''')