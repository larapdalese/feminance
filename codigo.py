import streamlit as st
import yfinance as yf
import datetime
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
    def exibir_grafico_cotacao(ticker, moeda):
        today = datetime.datetime.today().strftime('%Y-%m-%d')  # Data atual
        dados = yf.download(ticker, start='2023-01-01', end=today)
        if not dados.empty:
            st.markdown(f"**{moeda}**")
            st.line_chart(dados['Close'])
        else:
            st.error(f'Não foi possível obter os dados da cotação do {moeda}.')
    exibir_grafico_cotacao('USDBRL=X', 'Dólar')
    exibir_grafico_cotacao('EURBRL=X', 'Euro')
st.set_page_config(layout="wide", page_title="Buscar Símbolos de Ações")
st.markdown("<h1 style='text-align: center;'>Busca de Símbolos no Yahoo Finance</h1>", unsafe_allow_html=True)
empresa = st.text_input("Digite o nome da empresa:", "")
if empresa:
    url = f"https://query2.finance.yahoo.com/v1/finance/search?q={empresa}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        resultados = data.get("quotes", [])
        if resultados:
            st.subheader(f"Resultados encontrados para '{empresa}':")
            for item in resultados:
                nome_empresa = item.get("shortname", "Nome não disponível")
                symbol = item.get("symbol", "Símbolo não disponível")
                st.markdown(f"**Empresa:** {nome_empresa} | **Símbolo:** `{symbol}`")
        else:
            st.error("Nenhum símbolo encontrado para a empresa digitada.")
    else:
        st.error("Erro ao buscar os dados. Tente novamente mais tarde.")
