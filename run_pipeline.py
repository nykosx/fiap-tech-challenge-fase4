"""
Script para executar o pipeline completo do projeto
Tech Challenge Fase 4 - POSTECH Data Analytics
"""

import subprocess
import sys
import os
from pathlib import Path


def print_header(text):
    """Imprimir cabeçalho formatado"""
    print("\n" + "="*80)
    print(f"  {text}")
    print("="*80 + "\n")


def run_command(command, description):
    """Executar comando shell"""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, 
                              capture_output=True, text=True)
        print(f"✅ {description} - Concluído!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Erro: {e}")
        print(f"   Output: {e.stdout}")
        print(f"   Error: {e.stderr}")
        return False


def main():
    """Função principal"""
    print_header("🚀 PIPELINE AUTOMÁTICO - Tech Challenge Fase 4")
    
    print("""
    Este script irá:
    1. Verificar dependências
    2. Executar análise exploratória
    3. Treinar modelos de ML
    4. Gerar relatórios
    
    ⚠️ NOTA: Este processo pode levar 30-40 minutos
    
    """)
    
    response = input("Deseja continuar? (s/n): ")
    if response.lower() not in ['s', 'sim', 'y', 'yes']:
        print("❌ Operação cancelada pelo usuário")
        return
    
    # Passo 1: Verificar instalação
    print_header("📦 PASSO 1: Verificando Instalação")
    
    if not run_command("python check_project.py", 
                      "Verificação de estrutura e dependências"):
        print("\n⚠️ Problemas encontrados. Resolva-os antes de continuar.")
        return
    
    # Passo 2: Executar EDA (se possível via nbconvert)
    print_header("📊 PASSO 2: Análise Exploratória de Dados")
    
    eda_notebook = "notebooks/01_exploratory_data_analysis.ipynb"
    
    print(f"""
    ⚠️ AÇÃO MANUAL NECESSÁRIA:
    
    1. Abra o Jupyter Notebook:
       jupyter notebook
    
    2. Execute o notebook: {eda_notebook}
       (Cell > Run All)
    
    3. Revise as visualizações e insights
    
    Pressione ENTER quando terminar...
    """)
    input()
    
    # Passo 3: Treinar modelos
    print_header("🤖 PASSO 3: Treinamento de Modelos")
    
    training_notebook = "notebooks/02_model_training.ipynb"
    
    print(f"""
    ⚠️ AÇÃO MANUAL NECESSÁRIA:
    
    1. No Jupyter Notebook, execute: {training_notebook}
       (Cell > Run All)
    
    2. Aguarde o treinamento completo (~15-20 min)
    
    3. Verifique se a acurácia > 75% foi atingida
    
    Pressione ENTER quando terminar...
    """)
    input()
    
    # Passo 4: Verificar modelos
    print_header("✅ PASSO 4: Verificação Final")
    
    models_path = Path("models")
    required_models = [
        "best_model.pkl",
        "label_encoders.pkl",
        "target_encoder.pkl",
        "scaler.pkl",
        "feature_names.pkl"
    ]
    
    missing_models = []
    for model_file in required_models:
        if not (models_path / model_file).exists():
            missing_models.append(model_file)
    
    if missing_models:
        print(f"❌ Modelos faltando: {', '.join(missing_models)}")
        print("⚠️ Certifique-se de executar o notebook de treinamento completamente")
        return
    
    print("✅ Todos os modelos foram salvos com sucesso!")
    
    # Passo 5: Instruções finais
    print_header("🎉 PROJETO CONCLUÍDO!")
    
    print("""
    ✅ Pipeline executado com sucesso!
    
    📋 PRÓXIMOS PASSOS:
    
    1. Testar Aplicação de Predição:
       streamlit run app/app_prediction.py
    
    2. Visualizar Dashboard Analítico:
       streamlit run app/app_dashboard.py
    
    3. Revisar documentação:
       - README.md (documentação completa)
       - QUICKSTART.md (guia rápido)
    
    📊 ENTREGÁVEIS:
    ✅ Notebooks executados com análises
    ✅ Modelos treinados (>75% acurácia esperada)
    ✅ Aplicação de predição funcional
    ✅ Dashboard analítico funcional
    ✅ Documentação completa
    
    🏆 Parabéns! Projeto pronto para apresentação!
    """)
    
    print("="*80)


if __name__ == "__main__":
    main()
