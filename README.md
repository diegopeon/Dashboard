📊 Dashboard de Locadora de Veículos

Sistema em Streamlit + Python que lê automaticamente três arquivos CSV (clientes, veículos e locações) e gera um dashboard interativo completo.

✅ 1. Visão Geral

Este projeto fornece um dashboard para análise de uma locadora de veículos, incluindo:

Frota

Clientes

Histórico de locações

Indicadores financeiros

Tendências por período

O sistema lê automaticamente três arquivos CSV e gera visualizações inteligentes com filtros, KPIs e tabelas agrupadas.

📁 2. Estrutura de Arquivos Necessários

Você deve baixar os três arquivos CSV nesta pasta do Google Drive:

📦 Download:
👉 https://drive.google.com/file/d/1yyom-Kx305sgUGVB26D4BIuRxt4pWIac/view?usp=sharing

Descompacte o .zip baixado e coloque estes arquivos na mesma pasta do projeto:

client.csv
client_0.csv
vehicle_0.csv

🛠 3. Requisitos

Python 3.10+

Streamlit

Pandas

Instale as dependências:

pip install streamlit pandas

📦 4. Estrutura Recomendada do Projeto
/dashboard-locadora
│
├── app.py
├── client.csv
├── client_0.csv
├── vehicle_0.csv
└── README.md

▶️ 5. Como Rodar o Projeto
1️⃣ Abra o terminal (CMD / PowerShell)
2️⃣ Navegue até a pasta do projeto:
cd caminho/para/dashboard-locadora

3️⃣ Execute o dashboard usando Streamlit:
streamlit run app.py


⚠️ Importante:
NÃO execute usando python app.py — Streamlit precisa rodar com o comando streamlit run.

4️⃣ O navegador abrirá automaticamente em:
http://localhost:8501


Se não abrir, copie e cole o link manualmente.

🔧 6. Suporte a Múltiplos Formatos de CSV

Os arquivos CSV do projeto podem vir com:

separador vírgula ( , )

separador ponto e vírgula ( ; )

encoding UTF-8

encoding Latin-1

linhas quebradas ou inconsistentes

A função load_csv() do sistema já tenta automaticamente todas as combinações e ajusta:

encoding

separator

engine

Ignora linhas inválidas (on_bad_lines='skip')

🧭 7. Como Usar o Dashboard

O dashboard contém abas e métricas:

🔹 Visão Geral

KPIs principais:

total de clientes

total de veículos

total de locações

receita total

🔹 Frota

veículos por categoria

veículos por status

tipo de combustível

tabela dos veículos

🔹 Clientes

top clientes por número de locações

tabela de clientes

🔹 Locações

filtro por período

receita por mês

tabela de locações detalhada

🔹 Financeiro

estatísticas dos valores

distribuição das locações
