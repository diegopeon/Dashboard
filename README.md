# 🚗 Dashboard Interativo - Locadora de Veículos

[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)](https://streamlit.io/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)

Um dashboard completo desenvolvido em **Streamlit + Python** para análise e gestão de locadora de veículos, com visualizações interativas e relatórios automáticos.

## 📋 Índice

- [Visão Geral](#-visão-geral)
- [Funcionalidades](#-funcionalidades)
- [Pré-requisitos](#-pré-requisitos)
- [Instalação e Configuração](#-instalação-e-configuração)
- [Estrutura do Projeto](#-estrutura-do-projeto)
- [Execução](#-execução)
- [Módulos do Dashboard](#-módulos-do-dashboard)
- [Formatos de Arquivo Suportados](#-formatos-de-arquivo-suportados)
- [Suporte Técnico](#-suporte-técnico)

## 🎯 Visão Geral

Sistema inteligente que processa automaticamente dados de clientes, veículos e locações para fornecer insights estratégicos através de um dashboard interativo e fácil de usar.

## ✨ Funcionalidades

### 📊 **Módulo de Visão Geral**
- **KPIs Principais**: Total de clientes, veículos, locações e receita
- **Métricas em Tempo Real** com tendências e comparações
- **Visão consolidada** do negócio

### 🚙 **Módulo de Frota**
- **Análise por Categoria**: Distribuição de veículos por tipo
- **Status da Frota**: Disponibilidade e manutenção
- **Combustível**: Análise por tipo de motorização
- **Tabela Detalhada** com informações completas dos veículos

### 👥 **Módulo de Clientes**
- **Top Clientes**: Ranking por número de locações
- **Perfil de Clientes**: Análise comportamental
- **Base de Dados** completa de clientes

### 📅 **Módulo de Locações**
- **Filtros Avançados** por período e características
- **Receita por Mês**: Análise temporal e sazonalidade
- **Histórico Detalhado** de todas as locações

### 💰 **Módulo Financeiro**
- **Estatísticas de Valores**: Média, mediana e distribuição
- **Análise de Rentabilidade** por veículo e categoria
- **Relatórios Financeiros** consolidados

## 🛠 Pré-requisitos

- **Python 3.10+**
- **Streamlit**
- **Pandas**

## ⚙️ Instalação e Configuração

### 1. Clone ou baixe o projeto
```bash
git clone https://github.com/seu-usuario/dashboard-locadora.git
cd dashboard-locadora
```

### 2. Instale as dependências
```bash
pip install streamlit pandas
```

### 3. Download dos dados de exemplo
📥 **Baixe os arquivos CSV necessários:**
[Google Drive - Dados da Locadora](https://drive.google.com/file/d/1yyom-Kx305sgUGVB26D4BIuRxt4pWIac/view?usp=sharing)

**Após download, descompacte e posicione na pasta do projeto:**
- `client.csv`
- `client_0.csv` 
- `vehicle_0.csv`

## 📁 Estrutura do Projeto

```
dashboard-locadora/
│
├── app.py                          # Aplicação principal Streamlit
├── client.csv                      # Dados de clientes
├── client_0.csv                    # Dados adicionais de clientes
├── vehicle_0.csv                   # Dados da frota de veículos
├── requirements.txt                # Dependências do projeto
└── README.md                       # Documentação
```

## 🚀 Execução

### Método Recomendado (Streamlit)
```bash
streamlit run app.py
```

### ⚠️ Importante
**NÃO execute com:** `python app.py`  
**SEMPRE use:** `streamlit run app.py`

### Acesso ao Dashboard
Após executar o comando, o sistema automaticamente abrirá no navegador:
```
http://localhost:8501
```

**Se não abrir automaticamente:**
1. Copie o link acima
2. Cole manualmente no navegador
3. O dashboard estará pronto para uso!

## 🔧 Módulos do Dashboard

### 🔹 Visão Geral
- **KPIs Principais** em cards destacados
- **Métricas Financeiras** consolidadas
- **Visão 360°** do negócio

### 🔹 Frota 
- **Gráficos de Distribuição** por categoria e status
- **Análise de Combustível**
- **Tabela Interativa** com filtros

### 🔹 Clientes
- **Ranking de Melhores Clientes**
- **Análise de Fidelidade**
- **Base de Dados Completa**

### 🔹 Locações
- **Filtros por Período** (mensal, trimestral, anual)
- **Gráfico de Receita Temporal**
- **Tabela de Locações** com detalhes

### 🔹 Financeiro
- **Estatísticas Descritivas** dos valores
- **Distribuição de Preços**
- **Análise de Rentabilidade**

## 📄 Formatos de Arquivo Suportados

O sistema possui **inteligência automática** para detectar e processar diferentes formatos de CSV:

### ✅ Separadores Suportados
- Vírgula (`,`)
- Ponto e vírgula (`;`)

### ✅ Encodings Suportados
- UTF-8
- Latin-1 (ISO-8859-1)

### ✅ Tratamento de Erros
- **Linhas inconsistentes**: Ignoradas automaticamente
- **Dados faltantes**: Processados com resiliência
- **Formato variável**: Detectado automaticamente

## 🆘 Suporte Técnico

### Problemas Comuns e Soluções

**❌ Erro ao carregar arquivos CSV:**
- Verifique se os arquivos estão na pasta correta
- Confirme os nomes exatos dos arquivos
- Teste com os dados de exemplo do Google Drive

**❌ Dashboard não abre:**
- Execute `streamlit run app.py` (não `python app.py`)
- Verifique se a porta 8501 não está ocupada
- Confirme a instalação do Streamlit

**❌ Dados não aparecem:**
- Verifique o formato dos arquivos CSV
- Confirme o encoding (tente salvar como UTF-8)
- Teste com os dados de exemplo

### 📞 Contato para Suporte
Em caso de problemas persistentes, entre em contato com a equipe de desenvolvimento.

---

**Desenvolvido com ❤️ usando Streamlit + Python**  
*Sistema de Dashboard para Locadora de Veículos - Versão 1.0*
