"""
Funções para avaliação de modelos de Machine Learning
Tech Challenge Fase 4 - POSTECH Data Analytics
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    classification_report, confusion_matrix, roc_auc_score
)
from sklearn.model_selection import cross_val_score
import plotly.graph_objects as go
import plotly.express as px


def evaluate_model(model, X_test, y_test, class_names=None):
    """
    Avaliar modelo de classificação com múltiplas métricas
    
    Args:
        model: Modelo treinado
        X_test: Features de teste
        y_test: Labels de teste
        class_names: Nomes das classes
        
    Returns:
        Dicionário com métricas
    """
    # Fazer predições
    y_pred = model.predict(X_test)
    
    # Calcular métricas
    metrics = {
        'accuracy': accuracy_score(y_test, y_pred),
        'precision': precision_score(y_test, y_pred, average='weighted'),
        'recall': recall_score(y_test, y_pred, average='weighted'),
        'f1_score': f1_score(y_test, y_pred, average='weighted')
    }
    
    # Relatório de classificação
    report = classification_report(y_test, y_pred, 
                                   target_names=class_names,
                                   output_dict=True)
    
    # Matriz de confusão
    cm = confusion_matrix(y_test, y_pred)
    
    metrics['classification_report'] = report
    metrics['confusion_matrix'] = cm
    metrics['predictions'] = y_pred
    
    return metrics


def compare_models(models_dict, X_train, X_test, y_train, y_test, cv=5):
    """
    Comparar múltiplos modelos
    
    Args:
        models_dict: Dicionário {nome: modelo}
        X_train: Features de treino
        X_test: Features de teste
        y_train: Labels de treino
        y_test: Labels de teste
        cv: Número de folds para cross-validation
        
    Returns:
        DataFrame com comparação
    """
    results = []
    
    for name, model in models_dict.items():
        # Treinar modelo
        model.fit(X_train, y_train)
        
        # Avaliar
        metrics = evaluate_model(model, X_test, y_test)
        
        # Cross-validation
        cv_scores = cross_val_score(model, X_train, y_train, cv=cv)
        
        results.append({
            'Modelo': name,
            'Acurácia': metrics['accuracy'],
            'Precisão': metrics['precision'],
            'Recall': metrics['recall'],
            'F1-Score': metrics['f1_score'],
            'CV Score': cv_scores.mean(),
            'CV Std': cv_scores.std()
        })
    
    df_results = pd.DataFrame(results)
    df_results = df_results.sort_values('Acurácia', ascending=False)
    
    return df_results


def plot_confusion_matrix(cm, class_names, title='Confusion Matrix'):
    """
    Plotar matriz de confusão
    
    Args:
        cm: Matriz de confusão
        class_names: Nomes das classes
        title: Título do gráfico
    """
    plt.figure(figsize=(10, 8))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
                xticklabels=class_names,
                yticklabels=class_names,
                square=True, linewidths=0.5)
    plt.title(title, fontsize=14, fontweight='bold', pad=20)
    plt.ylabel('Classe Real', fontsize=12)
    plt.xlabel('Classe Prevista', fontsize=12)
    plt.xticks(rotation=45, ha='right')
    plt.yticks(rotation=0)
    plt.tight_layout()
    plt.show()


def plot_feature_importance(model, feature_names, top_n=15):
    """
    Plotar importância das features
    
    Args:
        model: Modelo treinado (deve ter feature_importances_)
        feature_names: Nomes das features
        top_n: Número de features para mostrar
    """
    if not hasattr(model, 'feature_importances_'):
        print("Modelo não possui feature_importances_")
        return
    
    importance_df = pd.DataFrame({
        'Feature': feature_names,
        'Importance': model.feature_importances_
    }).sort_values('Importance', ascending=False).head(top_n)
    
    plt.figure(figsize=(10, 6))
    plt.barh(importance_df['Feature'], importance_df['Importance'],
             color='steelblue', edgecolor='black')
    plt.xlabel('Importância', fontsize=12)
    plt.title(f'Top {top_n} Features Mais Importantes', 
              fontsize=14, fontweight='bold')
    plt.gca().invert_yaxis()
    plt.grid(axis='x', alpha=0.3)
    plt.tight_layout()
    plt.show()


def plot_model_comparison(results_df, metric='Acurácia'):
    """
    Plotar comparação de modelos
    
    Args:
        results_df: DataFrame com resultados
        metric: Métrica para plotar
    """
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        x=results_df['Modelo'],
        y=results_df[metric],
        text=results_df[metric].apply(lambda x: f'{x:.4f}'),
        textposition='auto',
        marker=dict(
            color=results_df[metric],
            colorscale='RdYlGn',
            showscale=True
        )
    ))
    
    fig.update_layout(
        title=f'Comparação de Modelos - {metric}',
        xaxis_title='Modelo',
        yaxis_title=metric,
        height=500
    )
    
    fig.show()


def calculate_class_metrics(y_test, y_pred, class_names):
    """
    Calcular métricas por classe
    
    Args:
        y_test: Labels verdadeiros
        y_pred: Predições
        class_names: Nomes das classes
        
    Returns:
        DataFrame com métricas por classe
    """
    report = classification_report(y_test, y_pred,
                                   target_names=class_names,
                                   output_dict=True)
    
    class_metrics = []
    for class_name in class_names:
        if class_name in report:
            class_metrics.append({
                'Classe': class_name,
                'Precisão': report[class_name]['precision'],
                'Recall': report[class_name]['recall'],
                'F1-Score': report[class_name]['f1-score'],
                'Support': report[class_name]['support']
            })
    
    return pd.DataFrame(class_metrics)


def print_model_summary(metrics, model_name):
    """
    Imprimir resumo das métricas do modelo
    
    Args:
        metrics: Dicionário com métricas
        model_name: Nome do modelo
    """
    print("=" * 80)
    print(f"RESUMO DO MODELO: {model_name}")
    print("=" * 80)
    print(f"\n📊 Métricas Globais:")
    print(f"  Acurácia:  {metrics['accuracy']:.4f} ({metrics['accuracy']*100:.2f}%)")
    print(f"  Precisão:  {metrics['precision']:.4f}")
    print(f"  Recall:    {metrics['recall']:.4f}")
    print(f"  F1-Score:  {metrics['f1_score']:.4f}")
    print("=" * 80)
