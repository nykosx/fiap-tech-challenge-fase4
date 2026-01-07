"""
Dashboard Analítico de Obesidade
Tech Challenge Fase 4 - POSTECH Data Analytics
Dashboard para equipe médica com insights e análises
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import joblib
import sys
import os

# Adicionar o diretório raiz ao path para imports
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT_DIR)

# Importar traduções e cores padronizadas
from src.translations import (
    VARIABLE_NAMES, OBESITY_LABELS, OBESITY_ORDER, VALUE_TRANSLATIONS,
    PRIMARY_COLOR, SECONDARY_COLOR, ACCENT_COLOR,
    translate_variable, translate_value, get_obesity_label, get_color_palette
)

# Configuração da página
st.set_page_config(
    page_title="Dashboard Analítico - Obesidade",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Carregar dados
@st.cache_data
def load_data():
    """Carregar dataset"""
    try:
        data_path = os.path.join(ROOT_DIR, 'data', 'Obesity.csv')
        df = pd.read_csv(data_path)
        df['BMI'] = df['Weight'] / (df['Height'] ** 2)
        return df
    except Exception as e:
        st.error(f"Erro ao carregar dados: {e}")
        return None

# Carregar métricas do modelo
@st.cache_resource
def load_metrics():
    """Carregar métricas do modelo"""
    try:
        metrics_path = os.path.join(ROOT_DIR, 'models', 'model_metrics.pkl')
        metrics = joblib.load(metrics_path)
        return metrics
    except:
        return None

# Título
st.title("Dashboard Analítico de Obesidade")
st.markdown("### Análises e insights para equipe médica")
st.markdown("---")

# Carregar dados
df = load_data()
metrics = load_metrics()

if df is None:
    st.error("❌ Dados não encontrados!")
    st.stop()

# Sidebar - Filtros
st.sidebar.header("Filtros")

# Filtro de gênero (com tradução)
gender_options = df['Gender'].unique()
gender_filter = st.sidebar.multiselect(
    translate_variable("Gender"),
    options=gender_options,
    default=gender_options,
    format_func=lambda x: translate_value(x)
)

# Filtro de idade
age_range = st.sidebar.slider(
    translate_variable("Age"),
    int(df['Age'].min()),
    int(df['Age'].max()),
    (int(df['Age'].min()), int(df['Age'].max()))
)

# Filtro de obesidade (com tradução)
obesity_options = sorted(df['Obesity'].unique(), key=lambda x: OBESITY_ORDER.index(x) if x in OBESITY_ORDER else 999)
obesity_filter = st.sidebar.multiselect(
    translate_variable("Obesity"),
    options=obesity_options,
    default=obesity_options,
    format_func=lambda x: get_obesity_label(x)
)

# Aplicar filtros
df_filtered = df[
    (df['Gender'].isin(gender_filter)) &
    (df['Age'] >= age_range[0]) &
    (df['Age'] <= age_range[1]) &
    (df['Obesity'].isin(obesity_filter))
]

st.sidebar.markdown("---")
st.sidebar.markdown(f"**Total de Registros:** {len(df_filtered)}")

# KPIs principais
st.header("Indicadores principais")
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.metric("Total de pacientes", f"{len(df_filtered):,}")

with col2:
    avg_age = df_filtered['Age'].mean()
    st.metric("Idade média", f"{avg_age:.1f} anos")

with col3:
    avg_bmi = df_filtered['BMI'].mean()
    st.metric("IMC médio", f"{avg_bmi:.2f}")

with col4:
    obesity_rate = (df_filtered['Obesity'].str.contains('Obesity').sum() / len(df_filtered)) * 100
    st.metric("Taxa de obesidade", f"{obesity_rate:.1f}%")

with col5:
    normal_weight = (df_filtered['Obesity'] == 'Normal_Weight').sum()
    normal_pct = (normal_weight / len(df_filtered)) * 100
    st.metric("Peso normal", f"{normal_pct:.1f}%")

st.markdown("---")

# Visualizações
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "Distribuições",
    "Correlações",
    "Demografia",
    "Hábitos de vida",
    "Modelo de ML"
])

with tab1:
    st.header("Distribuições de variáveis")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Distribuição de obesidade (ordenada e traduzida)
        obesity_counts = df_filtered['Obesity'].value_counts()
        obesity_counts = obesity_counts.reindex([x for x in OBESITY_ORDER if x in obesity_counts.index])
        obesity_counts_df = obesity_counts.reset_index()
        obesity_counts_df.columns = ['Obesidade', 'Quantidade']
        obesity_counts_df['Obesidade_PT'] = obesity_counts_df['Obesidade'].apply(get_obesity_label)
        
        # Usar gradiente de azul padronizado
        colors_grad = get_color_palette(len(obesity_counts_df))
        
        fig1 = px.bar(
            obesity_counts_df,
            x='Obesidade_PT',
            y='Quantidade',
            title='Distribuição dos Níveis de Obesidade',
            color='Quantidade',
            color_continuous_scale='Blues',
            text='Quantidade'
        )
        fig1.update_traces(textposition='outside', marker_line_color='black', marker_line_width=1.2)
        fig1.update_layout(showlegend=False, height=400, xaxis_title=translate_variable('Obesity'), yaxis_title='Frequência')
        st.plotly_chart(fig1, use_container_width=True)
    
    with col2:
        # Distribuição de IMC com cores padronizadas
        fig2 = px.histogram(
            df_filtered,
            x='BMI',
            nbins=40,
            title=f'Distribuição do {translate_variable("BMI")}',
            color_discrete_sequence=[SECONDARY_COLOR]
        )
        fig2.add_vline(x=18.5, line_dash="dash", line_color="#95a5a6", 
                      annotation_text="< 18.5", annotation_position="top")
        fig2.add_vline(x=25, line_dash="dash", line_color="#7f8c8d",
                      annotation_text="25", annotation_position="top")
        fig2.add_vline(x=30, line_dash="dash", line_color=PRIMARY_COLOR,
                      annotation_text="30", annotation_position="top")
        fig2.update_layout(height=400, xaxis_title=translate_variable('BMI'), yaxis_title='Frequência')
        fig2.update_traces(marker_line_color='black', marker_line_width=1.2, opacity=0.85)
        st.plotly_chart(fig2, use_container_width=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Distribuição de idade
        fig3 = px.histogram(
            df_filtered,
            x='Age',
            nbins=30,
            title='Distribuição por idade',
            color_discrete_sequence=[SECONDARY_COLOR],
            labels={'Age': 'Idade', 'count': 'Frequência'}
        )
        fig3.update_layout(height=400, xaxis_title='Idade', yaxis_title='Frequência')
        st.plotly_chart(fig3, use_container_width=True)
    
    with col2:
        # Boxplot de peso por obesidade (ordenado)
        df_ordered = df_filtered.copy()
        df_ordered['Obesidade_PT'] = df_ordered['Obesity'].apply(get_obesity_label)
        df_ordered['Obesity_Order'] = df_ordered['Obesity'].apply(lambda x: OBESITY_ORDER.index(x) if x in OBESITY_ORDER else 999)
        df_ordered = df_ordered.sort_values('Obesity_Order')
        
        fig4 = px.box(
            df_ordered,
            x='Obesidade_PT',
            y='Weight',
            title='Distribuição de peso por nível de obesidade',
            color='Obesidade_PT',
            color_discrete_sequence=get_color_palette(df_ordered['Obesidade_PT'].nunique())
        )
        fig4.update_layout(showlegend=False, height=400, xaxis_title='Nível de Obesidade', yaxis_title='Peso (kg)')
        fig4.update_xaxes(tickangle=45)
        st.plotly_chart(fig4, use_container_width=True)

with tab2:
    st.header("Análise de correlações")
    
    # Matriz de correlação
    numeric_cols = df_filtered.select_dtypes(include=[np.number]).columns
    corr_matrix = df_filtered[numeric_cols].corr()
    
    # Rename columns and index to Portuguese
    corr_matrix_pt = corr_matrix.rename(columns=translate_variable, index=translate_variable)
    
    fig5 = px.imshow(
        corr_matrix_pt,
        title='Matriz de Correlação - Variáveis Numéricas',
        color_continuous_scale='RdBu_r',
        aspect='auto',
        text_auto='.2f'
    )
    fig5.update_layout(height=600)
    st.plotly_chart(fig5, use_container_width=True)
    
    # Scatter plots
    col1, col2 = st.columns(2)
    
    with col1:
        df_scatter = df_filtered.copy()
        df_scatter['Obesidade'] = df_scatter['Obesity'].apply(get_obesity_label)
        
        fig6 = px.scatter(
            df_scatter,
            x='Height',
            y='Weight',
            color='Obesidade',
            title='Peso vs altura por nível de obesidade',
            color_discrete_sequence=get_color_palette(df_scatter['Obesidade'].nunique()),
            hover_data=['Age', 'BMI'],
            labels={'Height': 'Altura (m)', 'Weight': 'Peso (kg)', 'Age': 'Idade', 'BMI': 'IMC'}
        )
        fig6.update_layout(height=400)
        st.plotly_chart(fig6, use_container_width=True)
    
    with col2:
        df_scatter2 = df_filtered.copy()
        df_scatter2['Obesidade'] = df_scatter2['Obesity'].apply(get_obesity_label)
        
        fig7 = px.scatter(
            df_scatter2,
            x='Age',
            y='BMI',
            color='Obesidade',
            title='IMC vs idade por nível de obesidade',
            color_discrete_sequence=get_color_palette(df_scatter2['Obesidade'].nunique()),
            hover_data=['Weight', 'Height'],
            labels={'Age': 'Idade', 'BMI': 'IMC', 'Weight': 'Peso (kg)', 'Height': 'Altura (m)'}
        )
        fig7.update_layout(height=400)
        st.plotly_chart(fig7, use_container_width=True)

with tab3:
    st.header("Análise demográfica")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Obesidade por gênero
        df_gender = df_filtered.copy()
        df_gender['Gênero'] = df_gender['Gender'].apply(translate_value)
        df_gender['Obesidade'] = df_gender['Obesity'].apply(get_obesity_label)
        gender_obesity = pd.crosstab(df_gender['Gênero'], df_gender['Obesidade'], normalize='index') * 100
        
        fig8 = go.Figure()
        palette_gender = get_color_palette(len(gender_obesity.columns))
        for i, col in enumerate(gender_obesity.columns):
            fig8.add_trace(go.Bar(
                name=col,
                x=gender_obesity.index,
                y=gender_obesity[col],
                marker_color=palette_gender[i],
                text=gender_obesity[col].apply(lambda x: f'{x:.1f}%'),
                textposition='auto'
            ))
        
        fig8.update_layout(
            title='Distribuição de Obesidade por Gênero (%)',
            barmode='group',
            xaxis_title='Gênero',
            yaxis_title='Percentual (%)',
            height=400
        )
        st.plotly_chart(fig8, use_container_width=True)
    
    with col2:
        # Histórico familiar
        df_family = df_filtered.copy()
        df_family['Histórico Familiar'] = df_family['family_history'].apply(translate_value)
        df_family['Obesidade'] = df_family['Obesity'].apply(get_obesity_label)
        family_obesity = pd.crosstab(df_family['Histórico Familiar'], df_family['Obesidade'], normalize='index') * 100
        
        fig9 = go.Figure()
        palette_family = get_color_palette(len(family_obesity.columns))
        for i, col in enumerate(family_obesity.columns):
            fig9.add_trace(go.Bar(
                name=col,
                x=family_obesity.index,
                y=family_obesity[col],
                marker_color=palette_family[i],
                text=family_obesity[col].apply(lambda x: f'{x:.1f}%'),
                textposition='auto'
            ))
        
        fig9.update_layout(
            title='Obesidade por Histórico Familiar (%)',
            barmode='group',
            xaxis_title='Histórico Familiar',
            yaxis_title='Percentual (%)',
            height=400
        )
        st.plotly_chart(fig9, use_container_width=True)
    
    # Faixas etárias
    df_filtered['Faixa Etária'] = pd.cut(
        df_filtered['Age'],
        bins=[0, 20, 30, 40, 50, 100],
        labels=['<20', '20-30', '30-40', '40-50', '50+']
    )
    
    age_obesity = pd.crosstab(df_filtered['Faixa Etária'], df_filtered['Obesity'], normalize='index') * 100
    # Translate obesity types to Portuguese
    age_obesity.columns = [get_obesity_label(col) for col in age_obesity.columns]
    
    fig10 = px.bar(
        age_obesity,
        title='Distribuição de obesidade por faixa etária (%)',
        barmode='stack',
        color_discrete_sequence=get_color_palette(age_obesity.shape[1]),
        labels={'value': 'Percentual (%)', 'variable': 'Nível de Obesidade', 'Faixa Etária': 'Faixa Etária'}
    )
    fig10.update_layout(height=400)
    st.plotly_chart(fig10, use_container_width=True)

with tab4:
    st.header("Hábitos de vida e comportamento")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Atividade física
        faf_obesity = df_filtered.groupby('Obesity')['FAF'].mean().reset_index()
        faf_obesity.columns = ['Obesidade_Cod', 'Frequência Média']
        faf_obesity['Obesidade'] = faf_obesity['Obesidade_Cod'].apply(get_obesity_label)
        faf_obesity['Obesity_Order'] = faf_obesity['Obesidade_Cod'].apply(
            lambda x: OBESITY_ORDER.index(x) if x in OBESITY_ORDER else 999
        )
        faf_obesity = faf_obesity.sort_values('Obesity_Order')

        fig11 = px.bar(
            faf_obesity,
            x='Obesidade',
            y='Frequência Média',
            title='Frequência Média de Atividade Física por Nível de Obesidade',
            color='Frequência Média',
            color_continuous_scale='Greens',
            text='Frequência Média'
        )
        fig11.update_traces(texttemplate='%{text:.2f}', textposition='outside')
        fig11.update_layout(showlegend=False, height=450, margin=dict(t=80, b=80))
        fig11.update_xaxes(tickangle=45)
        fig11.update_yaxes(range=[0, faf_obesity['Frequência Média'].max() * 1.15])
        st.plotly_chart(fig11, use_container_width=True)
    
    with col2:
        # Consumo de água
        ch2o_obesity = df_filtered.groupby('Obesity')['CH2O'].mean().reset_index()
        ch2o_obesity.columns = ['Obesidade_Cod', 'Consumo Médio']
        ch2o_obesity['Obesidade'] = ch2o_obesity['Obesidade_Cod'].apply(get_obesity_label)
        ch2o_obesity['Obesity_Order'] = ch2o_obesity['Obesidade_Cod'].apply(
            lambda x: OBESITY_ORDER.index(x) if x in OBESITY_ORDER else 999
        )
        ch2o_obesity = ch2o_obesity.sort_values('Obesity_Order')

        fig12 = px.bar(
            ch2o_obesity,
            x='Obesidade',
            y='Consumo Médio',
            title='Consumo Médio de Água por Nível de Obesidade',
            color='Consumo Médio',
            color_continuous_scale='Blues',
            text='Consumo Médio'
        )
        fig12.update_traces(texttemplate='%{text:.2f}L', textposition='outside')
        fig12.update_layout(showlegend=False, height=450, margin=dict(t=80, b=80))
        fig12.update_xaxes(tickangle=45)
        fig12.update_yaxes(range=[0, ch2o_obesity['Consumo Médio'].max() * 1.15])
        st.plotly_chart(fig12, use_container_width=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Alimentos calóricos
        df_favc = df_filtered.copy()
        df_favc['Alimentos Calóricos'] = df_favc['FAVC'].apply(translate_value)
        df_favc['Obesidade'] = df_favc['Obesity'].apply(get_obesity_label)
        favc_obesity = pd.crosstab(df_favc['Alimentos Calóricos'], df_favc['Obesity'], normalize='index') * 100

        # Ordenar colunas de obesidade conforme OBESITY_ORDER e garantir rótulos em português
        obesity_cols_ordered = [get_obesity_label(x) for x in OBESITY_ORDER if get_obesity_label(x) in favc_obesity.columns]
        favc_obesity = favc_obesity[obesity_cols_ordered]
        
        fig13 = go.Figure()
        palette_favc = get_color_palette(len(favc_obesity.columns))
        for i, col in enumerate(favc_obesity.columns):
            fig13.add_trace(go.Bar(
                name=col,
                x=favc_obesity.index,
                y=favc_obesity[col],
                marker_color=palette_favc[i],
                text=favc_obesity[col].apply(lambda x: f'{x:.1f}%'),
                textposition='auto'
            ))
        
        fig13.update_layout(
            title='Consumo de Alimentos Calóricos vs Obesidade (%)',
            barmode='group',
            xaxis_title='Consome Alimentos Calóricos',
            yaxis_title='Percentual (%)',
            height=400
        )
        st.plotly_chart(fig13, use_container_width=True)
    
    with col2:
        # Meio de transporte
        df_mtrans = df_filtered.copy()
        df_mtrans['Transporte'] = df_mtrans['MTRANS'].apply(translate_value)
        df_mtrans['Obesidade'] = df_mtrans['Obesity'].apply(get_obesity_label)
        mtrans_counts = df_mtrans.groupby(['Transporte', 'Obesidade']).size().reset_index(name='Quantidade')
        
        fig14 = px.sunburst(
            mtrans_counts,
            path=['Transporte', 'Obesidade'],
            values='Quantidade',
            title='Meio de Transporte por Nível de Obesidade',
            color_discrete_sequence=get_color_palette(mtrans_counts['Transporte'].nunique())
        )
        fig14.update_layout(height=400)
        st.plotly_chart(fig14, use_container_width=True)

with tab5:
    st.header("Desempenho do modelo de ML")

    if metrics:
        col1, col2 = st.columns(2)

        with col1:
            st.metric("Modelo utilizado", metrics['model_name'])
        with col2:
            accuracy = metrics['accuracy'] * 100
            st.metric("Acurácia", f"{accuracy:.2f}%")

        if 'results_df' in metrics:
            with st.expander("Ver comparação detalhada de modelos"):
                st.dataframe(metrics['results_df'], use_container_width=True)
    else:
        st.info("Métricas do modelo não disponíveis nesta sessão.")

    st.markdown("---")
    st.subheader("Risco de obesidade por nível de atividade física")

    # Análise adicional: taxa de obesidade por faixa de FAF
    faf_risk_df = df_filtered.copy()
    faf_risk_df['Faixa_FAF'] = pd.cut(
        faf_risk_df['FAF'],
        bins=[-0.1, 0, 1, 2, faf_risk_df['FAF'].max() + 0.1],
        labels=['0 dias/sem', '0-1 dia/sem', '1-2 dias/sem', '≥2 dias/sem']
    )

    obesity_by_faf = (
        faf_risk_df
        .assign(Obeso=faf_risk_df['Obesity'].str.contains('Obesity'))
        .groupby('Faixa_FAF')['Obeso']
        .mean()
        .reset_index()
    )
    obesity_by_faf['Taxa_Obesidade_%'] = obesity_by_faf['Obeso'] * 100

    fig_faf = px.bar(
        obesity_by_faf,
        x='Faixa_FAF',
        y='Taxa_Obesidade_%',
        title='Taxa de obesidade por frequência de atividade física',
        color='Taxa_Obesidade_%',
        color_continuous_scale='Reds',
        labels={
            'Faixa_FAF': 'Frequência de atividade física (FAF)',
            'Taxa_Obesidade_%': 'Taxa de obesidade (%)'
        },
        text='Taxa_Obesidade_%'
    )
    fig_faf.update_traces(texttemplate='%{text:.1f}%', textposition='outside')
    fig_faf.update_layout(showlegend=False, height=420, margin=dict(t=80, b=80))
    st.plotly_chart(fig_faf, use_container_width=True)

    # Texto interpretativo simples
    try:
        low_activity_rate = obesity_by_faf.loc[obesity_by_faf['Faixa_FAF'] == '0 dias/sem', 'Taxa_Obesidade_%'].iloc[0]
    except IndexError:
        low_activity_rate = np.nan

    try:
        high_activity_rate = obesity_by_faf.loc[obesity_by_faf['Faixa_FAF'] == '≥2 dias/sem', 'Taxa_Obesidade_%'].iloc[0]
    except IndexError:
        high_activity_rate = np.nan

    if not np.isnan(low_activity_rate) and not np.isnan(high_activity_rate):
        diff_rate = low_activity_rate - high_activity_rate
        st.markdown(
            f"Em média, pacientes sem atividade física apresentam taxa de obesidade de **{low_activity_rate:.1f}%**, "
            f"enquanto aqueles com **2 ou mais dias de atividade física por semana** têm cerca de **{high_activity_rate:.1f}%**. "
            f"Isso representa uma diferença aproximada de **{diff_rate:.1f} pontos percentuais** na taxa de obesidade entre os grupos."
        )
    else:
        st.markdown(
            "As faixas de atividade física atuais não permitem comparar claramente as taxas de obesidade entre grupos. "
            "Ajuste os filtros à esquerda para visualizar melhor esse efeito."
        )

# Insights e Recomendações
st.markdown("---")
st.header("💡 Insights e Recomendações")

col1, col2 = st.columns(2)

with col1:
    st.subheader("📊 Principais Descobertas")
    
    insights = [
        f"• **Taxa de Obesidade:** {obesity_rate:.1f}% dos pacientes apresentam algum tipo de obesidade",
        f"• **IMC Médio:** {avg_bmi:.2f} - {'Normal' if 18.5 <= avg_bmi < 25 else 'Acima do normal' if avg_bmi >= 25 else 'Abaixo do normal'}",
        f"• **Idade Média:** {avg_age:.1f} anos",
        f"• **Gênero Predominante:** {translate_value(df_filtered['Gender'].mode()[0])}"
    ]
    
    for insight in insights:
        st.markdown(insight)
    
    # Fatores de risco
    st.markdown("**Fatores de Risco Identificados:**")
    risk_factors = []
    
    if df_filtered['family_history'].value_counts().get('yes', 0) > len(df_filtered) * 0.5:
        risk_factors.append("• Alta prevalência de histórico familiar")
    
    if df_filtered['FAF'].mean() < 1.5:
        risk_factors.append("• Baixa frequência de atividade física")
    
    if df_filtered['FAVC'].value_counts().get('yes', 0) > len(df_filtered) * 0.5:
        risk_factors.append("• Alto consumo de alimentos calóricos")
    
    for risk in risk_factors:
        st.warning(risk)

with col2:
    st.subheader("🎯 Recomendações para Intervenção")
    
    recommendations = [
        "**1. Programas de Atividade Física**\n   - Implementar programas de exercícios regulares\n   - Incentivar atividades aeróbicas e de fortalecimento",
        
        "**2. Educação Nutricional**\n   - Workshops sobre alimentação saudável\n   - Orientação sobre escolhas alimentares",
        
        "**3. Acompanhamento Regular**\n   - Monitoramento periódico de peso e IMC\n   - Consultas de acompanhamento",
        
        "**4. Intervenção Comportamental**\n   - Grupos de apoio\n   - Técnicas de mudança de comportamento"
    ]
    
    for rec in recommendations:
        st.info(rec)

# Rodapé
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #888;">
    <p>Tech Challenge Fase 4 - POSTECH Data Analytics - 9DTAT</p>
    <p>Dashboard Analítico de Obesidade | Desenvolvido usando Streamlit</p>
</div>
""", unsafe_allow_html=True)
