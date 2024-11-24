import streamlit as st
import yfinance as yf
import datetime
import altair as alt
st.set_page_config(layout="wide", page_title="Investimentos")
def apply_custom_css():
    st.markdown("""
        <style>
        .main .block-container {
            padding-top: 1rem;
            padding-bottom: 1rem;
            padding-left: 0.5rem;
            padding-right: 0.5rem;
            max-width: 100%;
        }
        </style>
    """, unsafe_allow_html=True)
apply_custom_css()
st.markdown("""
    <style>
    .centered-title {
        text-align: center;
        font-size: 36px;
        font-weight: bold;
    }
    .centered-subtitle {
        text-align: center;
        font-size: 18px;
    }
    </style>
    <h1 class="centered-title">Investimentos</h1>
    """, unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    st.subheader("Tipos de investimento")
    st.markdown("Saiba um pouco mais sobre investimentos e as alternativas para o dinheiro que está sobrando na conta e que você não deseja gastar com mimos, clique nas palavras azuis sublinhadas para ser direcionada a páginas que te trarão mais informações sobre os tipos de investimentos.")
    st.markdown("""
    <style>
    .custom-subsubtitle {
        font-size: 20px; 
        font-weight: bold; 
        margin-bottom: 10px; 
    }
    </style>
    <p class="custom-subsubtitle">Investimentos de baixo risco</p>
""", unsafe_allow_html=True)
    st.markdown("Rendem menos & são mais seguros!")
    st.markdown("""
        - **Tesouro Direto**: 
        [Um dos investimentos mais seguros do Brasil, ideal para quem busca estabilidade.](https://www.tesourodireto.com.br/)
    """)
    st.markdown("""
        - **CDB**: 
        [Certificados de Depósito Bancário que oferecem segurança e rendimento superior à poupança, cada banco possui o seu.](https://www.b3.com.br/pt_br/produtos-e-servicos/registro/renda-fixa-e-valores-mobiliarios/certificado-de-deposito-bancario.htm)
    """)
    st.markdown("""
        - **Poupança**: 
        [Apesar de menos rentável, ainda é uma opção segura para reservas de emergência.](https://www.gov.br/pt-br/servicos-estaduais/conta-poupanca)
    """)
    st.markdown("""
    <style>
    .custom-subsubtitle {
        font-size: 20px; 
        font-weight: bold; 
        margin-bottom: 10px; 
    }
    </style>
    <p class="custom-subsubtitle">Investimentos de médio risco</p>
""", unsafe_allow_html=True)
with col2:
    st.subheader("Gráficos de Cotação")   
    def exibir_grafico_cotacao(ticker, ativo):
        today = datetime.datetime.today().strftime('%Y-%m-%d')
        dados = yf.download(ticker, start='2023-01-01', end=today)     
        if not dados.empty:
            if 'Close' in dados.columns:
                st.markdown(f"**{ativo}**")
                dados = dados.reset_index()  
                grafico = alt.Chart(dados).mark_line(color="#E85234").encode(
                    x='Date:T',
                    y='Close:Q',
                    tooltip=['Date:T', 'Close:Q']
                ).properties(
                    width=700,
                    height=400
                )
                st.altair_chart(grafico, use_container_width=True)
                ultimo_valor = dados['Close'].iloc[-1]
                st.write(f"Último valor do {ativo.lower()}: R$ {ultimo_valor:.2f}")
            else:
                st.error(f"A coluna 'Close' não foi encontrada nos dados do {ativo}.")
        else:
            st.error(f"Não foi possível obter os dados do {ativo}. O DataFrame está vazio.")
    exibir_grafico_cotacao('USDBRL=X', 'Dólar')
    st.write(
        """
        Saber o valor do dólar e o quanto o preço dele varia pode ser muito importante, vai além de motivos como viagens programadas. 
        Com a alta do dólar, empresas que exportam seus produtos (como carne, açúcar, grãos e outros produtos) optam estrategicamente 
        em atender o mercado de fora do Brasil, porque rende mais dinheiro. Dessa forma, a oferta de produtos ao mercado daqui é reduzida 
        e, por ter menos para vender, acontece o aumento de preços no supermercado.
        """
    )
    exibir_grafico_cotacao('^BVSP', 'IBOVESPA')
    st.markdown(
        """
        [Ok, mas o que é a Bolsa de Valores Brasileira/IBOVESPA?](https://g1.globo.com/economia/especial-publicitario/inteligencia-financeira/noticia/2022/06/23/voce-sabe-o-que-e-o-ibovespa-e-sua-importancia-no-mercado-de-capitais.ghtml)
        """
    )
