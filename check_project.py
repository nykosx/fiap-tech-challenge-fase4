"""
Script para inicialização rápida do projeto
Executa verificações e prepara o ambiente
"""

import os
import sys
from pathlib import Path

def check_structure():
    """Verificar estrutura de diretórios"""
    print("🔍 Verificando estrutura do projeto...")
    
    required_dirs = ['data', 'notebooks', 'src', 'models', 'app']
    missing_dirs = []
    
    for dir_name in required_dirs:
        if not os.path.exists(dir_name):
            missing_dirs.append(dir_name)
    
    if missing_dirs:
        print(f"❌ Diretórios faltando: {', '.join(missing_dirs)}")
        return False
    
    print("✅ Estrutura de diretórios OK!")
    return True


def check_data():
    """Verificar se os dados existem"""
    print("\n🔍 Verificando dados...")
    
    data_file = Path('data/Obesity.csv')
    
    if not data_file.exists():
        print("❌ Arquivo Obesity.csv não encontrado em data/")
        return False
    
    print(f"✅ Dataset encontrado: {data_file}")
    
    # Contar linhas
    try:
        with open(data_file, 'r') as f:
            lines = len(f.readlines()) - 1  # -1 para header
        print(f"   📊 {lines} registros encontrados")
    except Exception as e:
        print(f"⚠️ Erro ao ler arquivo: {e}")
    
    return True


def check_dependencies():
    """Verificar dependências instaladas"""
    print("\n🔍 Verificando dependências...")
    
    required_packages = [
        'pandas', 'numpy', 'sklearn', 'matplotlib', 
        'seaborn', 'streamlit', 'plotly', 'xgboost', 'joblib'
    ]
    
    missing_packages = []
    
    for package in required_packages:
        try:
            __import__(package)
        except ImportError:
            missing_packages.append(package)
    
    if missing_packages:
        print(f"❌ Pacotes faltando: {', '.join(missing_packages)}")
        print("\n💡 Execute: pip install -r requirements.txt")
        return False
    
    print("✅ Todas as dependências instaladas!")
    return True


def check_models():
    """Verificar se modelos existem"""
    print("\n🔍 Verificando modelos treinados...")
    
    model_files = [
        'models/best_model.pkl',
        'models/label_encoders.pkl',
        'models/target_encoder.pkl',
        'models/scaler.pkl',
        'models/feature_names.pkl'
    ]
    
    existing = []
    missing = []
    
    for model_file in model_files:
        if os.path.exists(model_file):
            existing.append(model_file)
        else:
            missing.append(model_file)
    
    if missing:
        print(f"⚠️ Modelos não encontrados: {len(missing)}/{len(model_files)}")
        print("💡 Execute o notebook 02_model_training.ipynb para treinar os modelos")
        return False
    
    print(f"✅ Todos os modelos encontrados ({len(existing)} arquivos)")
    return True


def main():
    """Função principal"""
    print("="*80)
    print("🚀 VERIFICAÇÃO DO PROJETO - Tech Challenge Fase 4")
    print("="*80)
    
    checks = [
        check_structure(),
        check_data(),
        check_dependencies(),
        check_models()
    ]
    
    print("\n" + "="*80)
    
    if all(checks):
        print("✅ PROJETO PRONTO PARA USO!")
        print("\n📋 Próximos passos:")
        print("   1. Execute: jupyter notebook (para EDA e treinamento)")
        print("   2. Execute: streamlit run app/app_prediction.py (predição)")
        print("   3. Execute: streamlit run app/app_dashboard.py (dashboard)")
    else:
        print("⚠️ PROJETO COM PENDÊNCIAS")
        print("\n📋 Siga as instruções acima para resolver os problemas")
    
    print("="*80)


if __name__ == "__main__":
    main()
