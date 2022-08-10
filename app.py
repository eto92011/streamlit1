import streamlit as st


#Importando as bibliotecas necessárias
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st



#Função para selecionar a quantiodade de linhas do dataframe

def mostra_qntd_linhas(dataframe):
    qntd_linhas=st.sidebar.slider("Seleciopne a quantidade de linhas que deseja mostrar na tabela", min_value=1, max_value=len(dataframe),step=1)
    st.write(dataframe.head(qntd_linhas).style.format(subset=['TTEseg'], formatter="{:.2f}"))


#Função que cria o gráfico

def plot_estoque(dataframe,categoria):
    dados_plot=dataframe.query("grupo==@categoria")
    
    fig, ax= plt.subplots(figsize=(8,6))
    ax=sns.barplot(x='grupo', y='TTLseg', data=dados_plot)
    ax.set_title(f'Quantidade em estoque dos produtos de {categoria} ',fontsize=16)
    ax.set_xlabel('Produtos', fontsize = 12)
    ax.tick_params(rotation = 20, axis = 'x')
    ax.set_ylabel('Quantidade', fontsize = 12)

    return fig



#importando os dados

dados=pd.read_excel("base/BaseAGF.xlsx", sheet_name="BaseAGF")


#escrevendo um título na página

st.title('Minha Primeira Aplicação')


st.write("Nesse projeto vamos analisar a quantidade de produtos em estoque, por categoria, \
de uma base de dados de produtos de supermercado")


#Filtros para a Tabela

checkbox_mostrar_tabela=st.sidebar.checkbox("Mostrar Tabela")

if checkbox_mostrar_tabela:
    st.sidebar.markdown("## Filtro para a Tabela")

    categorias=list(dados["grupo"].unique())
    categorias.append("Todas")
    categoria=st.sidebar.selectbox('Selecione a categoria para apresentar na tabela',options=categorias)


    if categoria!="Todas":
        df_categoria=dados.query('grupo == @categoria')
        mostra_qntd_linhas(df_categoria)
    else:
        mostra_qntd_linhas(dados)



# filtro para o gráfico
st.sidebar.markdown('## Filtro para o gráfico')

categoria_grafico = st.sidebar.selectbox('Selecione a categoria para apresentar no gráfico', options = dados['grupo'].unique())
figura = plot_estoque(dados, categoria_grafico)
st.pyplot(figura)

