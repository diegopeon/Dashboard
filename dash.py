# app.py
# Dashboard para Locadora de Carros lendo:
# - client.csv
# - vehicle_0.csv
# - client_0.csv
#
# Para rodar:
# 1) Coloque este arquivo (app.py) na mesma pasta dos CSVs
# 2) No terminal:  streamlit run app.py

import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Dashboard Locadora de Veículos",
    layout="wide"
)

@st.cache_data
def load_csv(path: str) -> pd.DataFrame:
    """
    Tenta ler o CSV em vários formatos comuns no Brasil.
    - Testa UTF-8 e Latin1
    - Testa separador ',' e ';'
    - Ignora linhas quebradas (on_bad_lines='skip')
    """
    tentativas = [
        {"sep": ",", "encoding": "utf-8"},
        {"sep": ";", "encoding": "utf-8"},
        {"sep": ";", "encoding": "latin1"},
        {"sep": ",", "encoding": "latin1"},
    ]

    for cfg in tentativas:
        try:
            df = pd.read_csv(
                path,
                sep=cfg["sep"],
                encoding=cfg["encoding"],
                engine="python",          # mais tolerante
                on_bad_lines="skip"       # ignora linhas zoada
            )
            st.sidebar.success(
                f"{path} lido com sucesso "
                f"({df.shape[0]} linhas, {df.shape[1]} colunas, "
                f"sep='{cfg['sep']}', encoding='{cfg['encoding']}')"
            )
            return df
        except Exception as e:
            st.sidebar.warning(f"Falha ao ler {path} com {cfg}: {e}")

    st.sidebar.error(f"❌ Não foi possível ler {path} em nenhum formato testado.")
    return pd.DataFrame()


# ==== CARREGAMENTO DOS DADOS ====
clients_df  = load_csv("client.csv")
vehicles_df = load_csv("vehicle_0.csv")
rentals_df  = load_csv("client_0.csv")  # aqui estamos assumindo que é o histórico de locações

st.title("📊 Dashboard – Locadora de Veículos")

st.sidebar.header("⚙️ Configurações dos dados")

st.sidebar.subheader("Arquivos carregados")
st.sidebar.write(f"client.csv: **{clients_df.shape[0]}** linhas, **{clients_df.shape[1]}** colunas")
st.sidebar.write(f"vehicle_0.csv: **{vehicles_df.shape[0]}** linhas, **{vehicles_df.shape[1]}** colunas")
st.sidebar.write(f"client_0.csv: **{rentals_df.shape[0]}** linhas, **{rentals_df.shape[1]}** colunas")

if clients_df.empty or vehicles_df.empty or rentals_df.empty:
    st.error("Verifique se os arquivos client.csv, vehicle_0.csv e client_0.csv estão na mesma pasta do app.py e no formato CSV válido.")
    st.stop()

# ==== MAPEAMENTO FLEXÍVEL DAS COLUNAS ====
st.sidebar.subheader("🔑 Mapeamento de colunas")

# CLIENTES
st.sidebar.markdown("**Clientes (client.csv)**")
client_id_col = st.sidebar.selectbox(
    "Coluna de ID do cliente",
    options=clients_df.columns,
    index=0
)
client_name_col = st.sidebar.selectbox(
    "Coluna de nome do cliente",
    options=clients_df.columns,
    index=min(1, len(clients_df.columns)-1)
)

# VEÍCULOS
st.sidebar.markdown("**Veículos (vehicle_0.csv)**")
vehicle_id_col = st.sidebar.selectbox(
    "Coluna de ID/identificador do veículo",
    options=vehicles_df.columns,
    index=0
)
vehicle_category_col = st.sidebar.selectbox(
    "Coluna de categoria do veículo (econômico, SUV, etc.)",
    options=vehicles_df.columns,
    index=min(1, len(vehicles_df.columns)-1)
)
vehicle_status_col = st.sidebar.selectbox(
    "Coluna de status do veículo (disponível, alugado, manutenção)",
    options=vehicles_df.columns,
    index=min(2, len(vehicles_df.columns)-1)
)
vehicle_fuel_col = st.sidebar.selectbox(
    "Coluna de tipo de combustível",
    options=vehicles_df.columns,
    index=min(3, len(vehicles_df.columns)-1)
)

# LOCAÇÕES
st.sidebar.markdown("**Lotações / Contratos (client_0.csv)**")
rental_client_fk_col = st.sidebar.selectbox(
    "Coluna que referencia o cliente",
    options=rentals_df.columns,
    index=0
)
rental_vehicle_fk_col = st.sidebar.selectbox(
    "Coluna que referencia o veículo",
    options=rentals_df.columns,
    index=min(1, len(rentals_df.columns)-1)
)

date_cols = list(rentals_df.columns)
rental_start_col = st.sidebar.selectbox(
    "Coluna de data de início da locação",
    options=date_cols,
    index=min(2, len(date_cols)-1)
)
rental_end_col = st.sidebar.selectbox(
    "Coluna de data de fim/devolução da locação",
    options=date_cols,
    index=min(3, len(date_cols)-1)
)

value_col = st.sidebar.selectbox(
    "Coluna de valor da locação (R$)",
    options=rentals_df.columns,
    index=min(4, len(rentals_df.columns)-1)
)

# Tentativa de converter datas e valores
for col in [rental_start_col, rental_end_col]:
    try:
        rentals_df[col] = pd.to_datetime(rentals_df[col])
    except:
        pass

try:
    rentals_df[value_col] = pd.to_numeric(rentals_df[value_col], errors="coerce")
except:
    pass

st.markdown("---")

# ======================= VISÃO GERAL =======================
st.header("📌 Visão Geral")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total de Clientes", f"{clients_df[client_id_col].nunique():,}".replace(",", "."))
with col2:
    st.metric("Total de Veículos", f"{vehicles_df[vehicle_id_col].nunique():,}".replace(",", "."))
with col3:
    st.metric("Total de Locações", f"{rentals_df.shape[0]:,}".replace(",", "."))
with col4:
    total_receita = rentals_df[value_col].sum(skipna=True)
    st.metric("Receita Total (R$)", f"{total_receita:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))

st.markdown("")

tab1, tab2, tab3, tab4 = st.tabs(["🚘 Frota", "👤 Clientes", "📄 Locações", "📈 Financeiro"])

# ======================= TAB FROTA =======================
with tab1:
    st.subheader("Frota de Veículos")

    c1, c2 = st.columns(2)

    with c1:
        st.markdown("**Veículos por Categoria**")
        cat_counts = vehicles_df[vehicle_category_col].value_counts().reset_index()
        cat_counts.columns = ["Categoria", "Quantidade"]
        st.bar_chart(cat_counts.set_index("Categoria"))

    with c2:
        st.markdown("**Veículos por Status**")
        status_counts = vehicles_df[vehicle_status_col].value_counts().reset_index()
        status_counts.columns = ["Status", "Quantidade"]
        st.bar_chart(status_counts.set_index("Status"))

    c3, c4 = st.columns(2)

    with c3:
        st.markdown("**Veículos por Tipo de Combustível**")
        fuel_counts = vehicles_df[vehicle_fuel_col].value_counts().reset_index()
        fuel_counts.columns = ["Combustível", "Quantidade"]
        st.bar_chart(fuel_counts.set_index("Combustível"))

    with c4:
        st.markdown("**Tabela de Veículos (amostra)**")
        st.dataframe(vehicles_df[[vehicle_id_col, vehicle_category_col, vehicle_status_col, vehicle_fuel_col]].head(50))

# ======================= TAB CLIENTES =======================
with tab2:
    st.subheader("Clientes")

    c1, c2 = st.columns(2)
    with c1:
        st.markdown("**Top clientes por número de locações**")
        top_clients = (
            rentals_df.groupby(rental_client_fk_col)
            .size()
            .reset_index(name="qtde_locações")
            .sort_values("qtde_locações", ascending=False)
            .head(10)
        )

        # juntar com nome do cliente, se existir relacionamento
        if client_id_col in clients_df.columns:
            top_clients = top_clients.merge(
                clients_df[[client_id_col, client_name_col]],
                left_on=rental_client_fk_col,
                right_on=client_id_col,
                how="left"
            )
            top_clients["Cliente"] = top_clients[client_name_col].fillna(top_clients[rental_client_fk_col].astype(str))
        else:
            top_clients["Cliente"] = top_clients[rental_client_fk_col].astype(str)

        st.bar_chart(top_clients.set_index("Cliente")["qtde_locações"])

    with c2:
        st.markdown("**Tabela de Clientes (amostra)**")
        st.dataframe(clients_df[[client_id_col, client_name_col]].head(50))

# ======================= TAB LOCAÇÕES =======================
with tab3:
    st.subheader("Locações")

    # Filtro de período
    if pd.api.types.is_datetime64_any_dtype(rentals_df[rental_start_col]):
        min_date = rentals_df[rental_start_col].min()
        max_date = rentals_df[rental_start_col].max()
        start_filter, end_filter = st.date_input(
            "Filtrar por período de início da locação",
            value=(min_date.date(), max_date.date())
        )

        mask = (rentals_df[rental_start_col].dt.date >= start_filter) & (rentals_df[rental_start_col].dt.date <= end_filter)
        rentals_filtered = rentals_df.loc[mask].copy()
    else:
        rentals_filtered = rentals_df.copy()

    c1, c2, c3 = st.columns(3)
    with c1:
        st.metric("Locações no período", f"{rentals_filtered.shape[0]:,}".replace(",", "."))
    with c2:
        st.metric("Clientes distintos no período", f"{rentals_filtered[rental_client_fk_col].nunique():,}".replace(",", "."))
    with c3:
        st.metric("Receita do período (R$)", f"{rentals_filtered[value_col].sum():,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))

    # Locações por mês
    if pd.api.types.is_datetime64_any_dtype(rentals_df[rental_start_col]):
        rentals_filtered["ano_mes"] = rentals_filtered[rental_start_col].dt.to_period("M").astype(str)
        by_month = rentals_filtered.groupby("ano_mes")[value_col].sum().reset_index()
        by_month = by_month.sort_values("ano_mes")

        st.markdown("**Receita por mês (com base na data de início)**")
        st.line_chart(by_month.set_index("ano_mes")[value_col])

    st.markdown("**Tabela de Locações (amostra)**")
    cols_to_show = [rental_client_fk_col, rental_vehicle_fk_col, rental_start_col, rental_end_col, value_col]
    cols_to_show = [c for c in cols_to_show if c in rentals_df.columns]
    st.dataframe(rentals_filtered[cols_to_show].head(100))

# ======================= TAB FINANCEIRO =======================
with tab4:
    st.subheader("Financeiro Básico")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Distribuição dos valores de locação**")
        st.bar_chart(rentals_df[value_col])

    with col2:
        st.markdown("**Estatísticas descritivas dos valores (R$)**")
        st.write(rentals_df[value_col].describe().to_frame("Valor").style.format("{:,.2f}".format))

    st.markdown("**Tabela completa de lançamentos de locação (amostra)**")
    st.dataframe(rentals_df[[rental_client_fk_col, rental_vehicle_fk_col, rental_start_col, rental_end_col, value_col]].head(100))
