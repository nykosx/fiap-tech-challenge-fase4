"""
Funções utilitárias para preprocessamento de dados
Tech Challenge Fase 4 - POSTECH Data Analytics
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler


def calculate_bmi(height: float, weight: float) -> float:
    """
    Calcular IMC (Índice de Massa Corporal)
    
    Args:
        height: Altura em metros
        weight: Peso em kg
        
    Returns:
        IMC calculado
    """
    return weight / (height ** 2)


def encode_categorical_features(df: pd.DataFrame, columns: list = None, 
                                encoders: dict = None) -> tuple:
    """
    Codificar variáveis categóricas usando LabelEncoder
    
    Args:
        df: DataFrame com os dados
        columns: Lista de colunas para codificar (None = todas categóricas)
        encoders: Dicionário com encoders já treinados (para predição)
        
    Returns:
        Tuple (DataFrame codificado, dicionário de encoders)
    """
    df_encoded = df.copy()
    
    if columns is None:
        columns = df.select_dtypes(include=['object']).columns.tolist()
    
    if encoders is None:
        encoders = {}
        for col in columns:
            le = LabelEncoder()
            df_encoded[col] = le.fit_transform(df[col])
            encoders[col] = le
    else:
        for col in columns:
            if col in encoders:
                df_encoded[col] = encoders[col].transform(df[col])
    
    return df_encoded, encoders


def scale_numerical_features(df: pd.DataFrame, columns: list = None,
                            scaler: StandardScaler = None) -> tuple:
    """
    Normalizar variáveis numéricas usando StandardScaler
    
    Args:
        df: DataFrame com os dados
        columns: Lista de colunas para normalizar (None = todas numéricas)
        scaler: Scaler já treinado (para predição)
        
    Returns:
        Tuple (DataFrame normalizado, scaler)
    """
    df_scaled = df.copy()
    
    if columns is None:
        columns = df.select_dtypes(include=[np.number]).columns.tolist()
    
    if scaler is None:
        scaler = StandardScaler()
        df_scaled[columns] = scaler.fit_transform(df[columns])
    else:
        df_scaled[columns] = scaler.transform(df[columns])
    
    return df_scaled, scaler


def prepare_data_for_training(df: pd.DataFrame, target_column: str = 'Obesity',
                              add_bmi: bool = True) -> tuple:
    """
    Preparar dados completos para treinamento
    
    Args:
        df: DataFrame original
        target_column: Nome da coluna alvo
        add_bmi: Se deve calcular e adicionar coluna de IMC
        
    Returns:
        Tuple (X_scaled, y_encoded, label_encoders, target_encoder, scaler, feature_names)
    """
    # Copiar dataframe
    df_prep = df.copy()
    
    # Calcular IMC se necessário
    if add_bmi and 'BMI' not in df_prep.columns:
        df_prep['BMI'] = df_prep.apply(
            lambda row: calculate_bmi(row['Height'], row['Weight']), 
            axis=1
        )
    
    # Separar features e target
    X = df_prep.drop(target_column, axis=1)
    y = df_prep[target_column]
    
    # Identificar colunas categóricas e numéricas
    categorical_cols = X.select_dtypes(include=['object']).columns.tolist()
    numerical_cols = X.select_dtypes(include=[np.number]).columns.tolist()
    
    # Codificar variáveis categóricas
    X_encoded, label_encoders = encode_categorical_features(X, categorical_cols)
    
    # Codificar target
    target_encoder = LabelEncoder()
    y_encoded = target_encoder.fit_transform(y)
    
    # Normalizar features numéricas
    X_scaled, scaler = scale_numerical_features(X_encoded, numerical_cols)
    
    # Salvar nomes das features
    feature_names = X_scaled.columns.tolist()
    
    return X_scaled, y_encoded, label_encoders, target_encoder, scaler, feature_names


def prepare_data_for_prediction(input_data: pd.DataFrame, 
                                label_encoders: dict,
                                scaler: StandardScaler,
                                feature_names: list,
                                add_bmi: bool = True) -> pd.DataFrame:
    """
    Preparar novos dados para predição
    
    Args:
        input_data: DataFrame com dados novos
        label_encoders: Dicionário com encoders treinados
        scaler: Scaler treinado
        feature_names: Lista com nomes das features na ordem correta
        add_bmi: Se deve calcular e adicionar coluna de IMC
        
    Returns:
        DataFrame preparado para predição
    """
    # Copiar dados
    df_pred = input_data.copy()
    
    # Calcular IMC se necessário
    if add_bmi and 'BMI' not in df_pred.columns:
        df_pred['BMI'] = df_pred.apply(
            lambda row: calculate_bmi(row['Height'], row['Weight']),
            axis=1
        )
    
    # Codificar variáveis categóricas
    categorical_cols = df_pred.select_dtypes(include=['object']).columns.tolist()
    df_encoded, _ = encode_categorical_features(df_pred, categorical_cols, label_encoders)
    
    # Normalizar features numéricas
    numerical_cols = df_encoded.select_dtypes(include=[np.number]).columns.tolist()
    df_scaled, _ = scale_numerical_features(df_encoded, numerical_cols, scaler)
    
    # Reordenar colunas
    df_scaled = df_scaled[feature_names]
    
    return df_scaled


def get_obesity_interpretation(obesity_class: str) -> dict:
    """
    Obter interpretação e recomendações para classe de obesidade
    
    Args:
        obesity_class: Nome da classe de obesidade
        
    Returns:
        Dicionário com interpretação e recomendações
    """
    interpretations = {
        'Insufficient_Weight': {
            'description': 'Peso Abaixo do Normal',
            'severity': 'low',
            'color': '#3498db',
            'recommendations': [
                'Consulte um nutricionista para plano alimentar adequado',
                'Considere exercícios de fortalecimento muscular',
                'Realize exames para verificar causas subjacentes'
            ]
        },
        'Normal_Weight': {
            'description': 'Peso Normal',
            'severity': 'normal',
            'color': '#2ecc71',
            'recommendations': [
                'Mantenha hábitos alimentares saudáveis',
                'Continue com atividades físicas regulares',
                'Mantenha dieta balanceada e variada'
            ]
        },
        'Overweight_Level_I': {
            'description': 'Sobrepeso Nível I',
            'severity': 'medium',
            'color': '#f39c12',
            'recommendations': [
                'Aumente frequência de atividades físicas',
                'Reduza consumo de alimentos processados',
                'Aumente consumo de água',
                'Considere consultar nutricionista'
            ]
        },
        'Overweight_Level_II': {
            'description': 'Sobrepeso Nível II',
            'severity': 'medium-high',
            'color': '#e67e22',
            'recommendations': [
                'Consulte profissional de saúde',
                'Inicie programa de atividades físicas regulares',
                'Revise hábitos alimentares',
                'Monitore regularmente peso e IMC'
            ]
        },
        'Obesity_Type_I': {
            'description': 'Obesidade Tipo I',
            'severity': 'high',
            'color': '#e74c3c',
            'recommendations': [
                'Consulta médica altamente recomendada',
                'Avalie riscos de comorbidades',
                'Inicie exercícios sob supervisão',
                'Plano nutricional profissional essencial'
            ]
        },
        'Obesity_Type_II': {
            'description': 'Obesidade Tipo II',
            'severity': 'very-high',
            'color': '#c0392b',
            'recommendations': [
                'Consulta médica urgente recomendada',
                'Avaliação completa de saúde necessária',
                'Acompanhamento multidisciplinar',
                'Monitoramento regular crucial'
            ]
        },
        'Obesity_Type_III': {
            'description': 'Obesidade Tipo III (Mórbida)',
            'severity': 'critical',
            'color': '#8e44ad',
            'recommendations': [
                'Procure assistência médica imediatamente',
                'Avaliação médica completa essencial',
                'Tratamento multidisciplinar intensivo',
                'Considere opções de tratamento especializado'
            ]
        }
    }
    
    return interpretations.get(obesity_class, {
        'description': 'Classificação Desconhecida',
        'severity': 'unknown',
        'color': '#95a5a6',
        'recommendations': ['Consulte um profissional de saúde']
    })


def get_bmi_category(bmi: float) -> str:
    """
    Classificar IMC em categorias
    
    Args:
        bmi: Valor do IMC
        
    Returns:
        Categoria do IMC
    """
    if bmi < 18.5:
        return 'Abaixo do Peso'
    elif bmi < 25:
        return 'Peso Normal'
    elif bmi < 30:
        return 'Sobrepeso'
    elif bmi < 35:
        return 'Obesidade Grau I'
    elif bmi < 40:
        return 'Obesidade Grau II'
    else:
        return 'Obesidade Grau III (Mórbida)'
