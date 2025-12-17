"""
Aplicação Streamlit para Predição de Níveis de Obesidade
Tech Challenge Fase 4 - POSTECH Data Analytics
"""

import streamlit as st
import pandas as pd
import numpy as np
import joblib
import plotly.graph_objects as go
import plotly.express as px
from pathlib import Path
import sys
sys.path.append('../src')

# Importar traduções e cores padronizadas
from translations import (
    VARIABLE_NAMES, OBESITY_LABELS, VALUE_TRANSLATIONS,
    PRIMARY_COLOR, SECONDARY_COLOR, ACCENT_COLOR,
    translate_variable, translate_value, get_obesity_label, get_color_palette
)

# Configuração da página
st.set_page_config(
    page_title="Preditor de Obesidade",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Carregar artefatos do modelo
@st.cache_resource
def load_model_artifacts():
    """Carregar modelo e artefatos necessários"""
    try:
        model = joblib.load('../models/best_model.pkl')
        label_encoders = joblib.load('../models/label_encoders.pkl')
        target_encoder = joblib.load('../models/target_encoder.pkl')
        scaler = joblib.load('../models/scaler.pkl')
        feature_names = joblib.load('../models/feature_names.pkl')
        metrics = joblib.load('../models/model_metrics.pkl')
        
        return model, label_encoders, target_encoder, scaler, feature_names, metrics
    except Exception as e:
        st.error(f"Erro ao carregar modelo: {e}")
        return None, None, None, None, None, None

# Carregar modelo
model, label_encoders, target_encoder, scaler, feature_names, metrics = load_model_artifacts()

# Título e descrição
st.title("🏥 Preditor de Níveis de Obesidade")
st.markdown("### Sistema de Classificação de Obesidade baseado em Machine Learning")
st.markdown("---")

# Verificar se o modelo foi carregado
if model is None:
    st.error("❌ Modelo não encontrado! Por favor, execute o notebook de treinamento primeiro.")
    st.stop()

# Exibir métricas do modelo
if metrics:
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("🎯 Modelo", metrics['model_name'])
    with col2:
        st.metric("📊 Acurácia", f"{metrics['accuracy']*100:.2f}%")
    with col3:
        status = "✅ Meta Atingida" if metrics['accuracy'] >= 0.75 else "⚠️ Abaixo da Meta"
        st.metric("🏆 Status", status)

st.markdown("---")

# Sidebar para entrada de dados
st.sidebar.header("📝 Dados do Paciente")
st.sidebar.markdown("Preencha as informações abaixo:")

# Criar formulário de entrada
with st.sidebar.form("patient_form"):
    st.subheader("Informações Pessoais")
    
    gender = st.selectbox(translate_variable("Gender"), ["Female", "Male"], 
                         format_func=lambda x: translate_value(x))
    age = st.number_input(translate_variable("Age"), min_value=10, max_value=100, value=25)
    height = st.number_input(translate_variable("Height"), min_value=1.0, max_value=2.5, value=1.70, step=0.01)
    weight = st.number_input(translate_variable("Weight"), min_value=30.0, max_value=200.0, value=70.0, step=0.5)
    
    st.subheader("Histórico e Hábitos")
    
    family_history = st.selectbox(translate_variable("family_history"), ["yes", "no"],
                                 format_func=lambda x: translate_value(x))
    favc = st.selectbox(translate_variable("FAVC"), ["yes", "no"],
                       format_func=lambda x: translate_value(x))
    fcvc = st.slider(translate_variable("FCVC"), 0.0, 3.0, 2.0, 0.1)
    ncp = st.slider(translate_variable("NCP"), 1.0, 4.0, 3.0, 0.1)
    
    caec = st.selectbox(translate_variable("CAEC"), 
                       ["no", "Sometimes", "Frequently", "Always"],
                       format_func=lambda x: translate_value(x))
    smoke = st.selectbox(translate_variable("SMOKE"), ["yes", "no"],
                        format_func=lambda x: translate_value(x))
    ch2o = st.slider(translate_variable("CH2O"), 0.0, 3.0, 2.0, 0.1)
    scc = st.selectbox(translate_variable("SCC"), ["yes", "no"],
                      format_func=lambda x: translate_value(x))
    
    st.subheader("Atividade Física")
    
    faf = st.slider(translate_variable("FAF"), 0.0, 3.0, 1.0, 0.1)
    tue = st.slider(translate_variable("TUE"), 0.0, 2.0, 1.0, 0.1)
    
    st.subheader("Outros")
    
    calc = st.selectbox(translate_variable("CALC"), 
                       ["no", "Sometimes", "Frequently", "Always"],
                       format_func=lambda x: translate_value(x))
    mtrans = st.selectbox(translate_variable("MTRANS"), 
                         ["Automobile", "Bike", "Motorbike", "Public_Transportation", "Walking"])
    
    submit_button = st.form_submit_button("🔍 Fazer Predição")

# Processar predição quando o botão for clicado
if submit_button:
    try:
        # Calcular BMI
        bmi = weight / (height ** 2)
        
        # Criar DataFrame com os dados de entrada
        input_data = pd.DataFrame({
            'Gender': [gender],
            'Age': [age],
            'Height': [height],
            'Weight': [weight],
            'family_history': [family_history],
            'FAVC': [favc],
            'FCVC': [fcvc],
            'NCP': [ncp],
            'CAEC': [caec],
            'SMOKE': [smoke],
            'CH2O': [ch2o],
            'SCC': [scc],
            'FAF': [faf],
            'TUE': [tue],
            'CALC': [calc],
            'MTRANS': [mtrans],
            'BMI': [bmi]
        })
        
        # Codificar variáveis categóricas
        categorical_cols = input_data.select_dtypes(include=['object']).columns
        for col in categorical_cols:
            if col in label_encoders:
                input_data[col] = label_encoders[col].transform(input_data[col])
        
        # Normalizar features numéricas
        numerical_cols = input_data.select_dtypes(include=[np.number]).columns
        input_data[numerical_cols] = scaler.transform(input_data[numerical_cols])
        
        # Reordenar colunas para corresponder ao treinamento
        input_data = input_data[feature_names]
        
        # Fazer predição
        prediction = model.predict(input_data)[0]
        prediction_proba = model.predict_proba(input_data)[0]
        
        # Decodificar predição
        predicted_class = target_encoder.inverse_transform([prediction])[0]
        predicted_label = get_obesity_label(predicted_class)
        
        # Exibir resultados
        st.markdown("---")
        st.header("📊 Resultado da Predição")
        
        col1, col2 = st.columns([1, 2])
        
        with col1:
            st.subheader("🎯 Classificação")
            
            # Definir cor baseada na classificação (cores padronizadas)
            colors_gradient = get_color_palette(7)
            color_map = dict(zip(target_encoder.classes_, colors_gradient))
            
            color = color_map.get(predicted_class, PRIMARY_COLOR)
            
            st.markdown(f"""
            <div style="background-color: {color}; padding: 20px; border-radius: 10px; text-align: center;">
                <h2 style="color: white; margin: 0;">{predicted_label}</h2>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown(f"**IMC Calculado:** {bmi:.2f}")
            
            # Interpretação do IMC
            st.markdown("**Interpretação:**")
            if bmi < 18.5:
                st.info("IMC indica peso abaixo do normal")
            elif bmi < 25:
                st.success("IMC dentro da faixa normal")
            elif bmi < 30:
                st.warning("IMC indica sobrepeso")
            else:
                st.error("IMC indica obesidade")
        
        with col2:
            st.subheader("📈 Probabilidades por Classe")
            
            # Criar DataFrame de probabilidades (com tradução)
            classes = target_encoder.classes_
            classes_pt = [get_obesity_label(cls) for cls in classes]
            proba_df = pd.DataFrame({
                'Classe': classes_pt,
                'Probabilidade': prediction_proba * 100
            }).sort_values('Probabilidade', ascending=True)
            
            # Gráfico de barras horizontais com cores padronizadas
            colors_gradient = get_color_palette(len(proba_df), reverse=True)
            
            fig = go.Figure(go.Bar(
                x=proba_df['Probabilidade'],
                y=proba_df['Classe'],
                orientation='h',
                marker=dict(
                    color=proba_df['Probabilidade'],
                    colorscale='Blues',
                    showscale=False
                ),
                text=proba_df['Probabilidade'].apply(lambda x: f'{x:.1f}%'),
                textposition='auto',
            ))
            
            fig.update_layout(
                title="Distribuição de Probabilidades",
                xaxis_title="Probabilidade (%)",
                yaxis_title="Classe",
                height=400,
                showlegend=False
            )
            
            st.plotly_chart(fig, use_container_width=True)
        
        # Recomendações
        st.markdown("---")
        st.header("💡 Recomendações")
        
        recommendations = {
            'Insufficient_Weight': [
                "🍽️ Consulte um nutricionista para desenvolver um plano alimentar adequado",
                "💪 Considere exercícios de fortalecimento muscular",
                "🏥 Realize exames médicos para verificar possíveis causas subjacentes"
            ],
            'Normal_Weight': [
                "✅ Mantenha hábitos alimentares saudáveis",
                "🏃 Continue com atividades físicas regulares",
                "🥗 Mantenha dieta balanceada e variada"
            ],
            'Overweight_Level_I': [
                "⚠️ Aumente a frequência de atividades físicas",
                "🥗 Reduza o consumo de alimentos processados e açúcares",
                "💧 Aumente o consumo de água",
                "👨‍⚕️ Considere consultar um nutricionista"
            ],
            'Overweight_Level_II': [
                "⚠️ Importante: consulte um profissional de saúde",
                "🏃 Inicie programa de atividades físicas regulares",
                "🥗 Revise completamente seus hábitos alimentares",
                "📊 Monitore regularmente seu peso e IMC"
            ],
            'Obesity_Type_I': [
                "🚨 Consulta médica é altamente recomendada",
                "🏥 Avalie riscos de comorbidades (diabetes, hipertensão, etc.)",
                "💪 Inicie programa de exercícios sob supervisão",
                "🍽️ Plano nutricional profissional é essencial"
            ],
            'Obesity_Type_II': [
                "🚨 Atenção: consulta médica urgente recomendada",
                "🏥 Avaliação completa de saúde necessária",
                "👨‍⚕️ Acompanhamento multidisciplinar (médico, nutricionista, educador físico)",
                "📊 Monitoramento regular de saúde é crucial"
            ],
            'Obesity_Type_III': [
                "🚨 URGENTE: procure assistência médica imediatamente",
                "🏥 Avaliação médica completa é essencial",
                "👥 Tratamento multidisciplinar intensivo necessário",
                "⚕️ Considere opções de tratamento especializado"
            ]
        }
        
        if predicted_class in recommendations:
            for rec in recommendations[predicted_class]:
                st.markdown(f"- {rec}")
        
        # Informações adicionais
        st.markdown("---")
        st.info("ℹ️ **Nota:** Este sistema é uma ferramenta de apoio à decisão. Sempre consulte profissionais de saúde qualificados para diagnóstico e tratamento adequados.")
        
    except Exception as e:
        st.error(f"❌ Erro ao processar predição: {e}")
        st.exception(e)

# Rodapé
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #888;">
    <p>Tech Challenge Fase 4 - POSTECH Data Analytics</p>
    <p>Sistema de Predição de Obesidade | Desenvolvido com ❤️ usando Streamlit</p>
</div>
""", unsafe_allow_html=True)
