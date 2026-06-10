import streamlit as st

st.title('Minha calculadora')
numero_1 = st.number_input(label='Digite o primeiro número', format='%0f')
numero_2 = st.number_input(label='Digite o segundo numero', format='%0f')
colunas = st.columns(4)

with colunas[0]:
    if st.button('Soma'):
        resultado = numero_1 + numero_2 
        st.write(f'O resultado é: {resultado}')  

with colunas[1]:
    if st.button('Subtração'):
        resultado = numero_1 - numero_2
        st.write(f'O resultado é: {resultado}')

with colunas[2]:
    if st.button('Multiplicação'):
        resultado = numero_1 * numero_2 
        st.write(f'O resultado é: {resultado}')

with colunas[3]:
    if st.button('Divisão'):
        resultado = numero_1 / numero_2
        st.write(f'O resultado é: {resultado}') 

