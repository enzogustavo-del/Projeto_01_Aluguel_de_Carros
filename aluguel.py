import streamlit as st
st.title("Nitro Drive - aluguem de carros")
st.sidebar.title("Escolha o seu Modelo")
st.sidebar.image("logo.png")

carros = ['BMW M4', "Dodge Charger R/T 1970", "Uno com escada", "Camaro", "Pagani"]


opcao = st.sidebar.selectbox('Escolha o carro que foi alugado', carros)

st.image(f'{opcao}.png')
st.markdown(f'## Você alugou o modelo: {opcao}')
st.markdown('---')

dias = st.text_input(f'Por quantos dias o {opcao} foi alugado?')
km = st.text_input(f'Quantos km você rodou com o {opcao}')

if opcao == 'BMW M4':
    diaria = 850

elif opcao == 'Dodge Charger R/T 1970':
    diaria = 1250

elif opcao == 'Uno com escada':
    diaria = 200

elif opcao == 'Camaro':
    diaria = 975

elif opcao == 'Pagani':
    diaria = 3000


if st.button('Calcular'):
    dias = int(dias)    
    km = float(km)

    total_dias = dias * diaria
    total_km = km * 0.15
    aluguel_total = total_dias + total_km

    st.warning(f'Você alugou o {opcao} por {dias} dias e rodou {km}km. O valor a pagar é R${aluguel_total:.2f}')
