"""
Testes básicos para validação do modelo e pipeline
Tech Challenge Fase 4 - POSTECH Data Analytics

Execute este arquivo do diretório raiz do projeto:
    python tests/test_model.py
"""

import os
import sys
import joblib  # Changed from pickle to joblib
import pandas as pd
import numpy as np
from pathlib import Path

# Determinar diretório raiz do projeto
if os.path.basename(os.getcwd()) == 'tests':
    # Se estiver executando de dentro da pasta tests
    ROOT_DIR = os.path.dirname(os.getcwd())
else:
    # Se estiver executando do diretório raiz
    ROOT_DIR = os.getcwd()

# Mudar para diretório raiz
os.chdir(ROOT_DIR)
sys.path.insert(0, ROOT_DIR)

print(f"📁 Diretório de trabalho: {ROOT_DIR}")
print()


def get_model_path(filename):
    """Retornar caminho absoluto para arquivo do modelo"""
    return os.path.join(ROOT_DIR, 'models', filename)


def test_model_files_exist():
    """Verificar se todos os arquivos do modelo existem"""
    required_files = [
        'best_model.pkl',
        'label_encoders.pkl',
        'target_encoder.pkl',
        'scaler.pkl',
        'feature_names.pkl'
    ]
    
    missing_files = []
    for filename in required_files:
        file_path = get_model_path(filename)
        if not os.path.exists(file_path):
            missing_files.append(filename)
    
    assert len(missing_files) == 0, f"Arquivos faltando: {missing_files}"
    print("✅ Todos os arquivos do modelo existem")


def test_load_model():
    """Testar carregamento do modelo"""
    try:
        model_path = get_model_path('best_model.pkl')
        model = joblib.load(model_path)
        
        assert model is not None, "Modelo não carregado"
        assert hasattr(model, 'predict'), "Modelo não tem método predict"
        print("✅ Modelo carregado com sucesso")
        return model
    except Exception as e:
        assert False, f"Erro ao carregar modelo: {e}"


def test_load_artifacts():
    """Testar carregamento de artefatos"""
    artifacts = {}
    
    try:
        artifacts['encoders'] = joblib.load(get_model_path('label_encoders.pkl'))
        artifacts['scaler'] = joblib.load(get_model_path('scaler.pkl'))
        artifacts['features'] = joblib.load(get_model_path('feature_names.pkl'))
        artifacts['target_encoder'] = joblib.load(get_model_path('target_encoder.pkl'))
        
        assert len(artifacts) == 4, "Não carregou todos os artefatos"
        print("✅ Todos os artefatos carregados")
        return artifacts
        
    except Exception as e:
        assert False, f"Erro ao carregar artefatos: {e}"


def test_prediction_pipeline():
    """Testar pipeline completo de predição"""
    
    # Carregar modelo e artefatos
    model = joblib.load(get_model_path('best_model.pkl'))
    encoders = joblib.load(get_model_path('label_encoders.pkl'))
    scaler = joblib.load(get_model_path('scaler.pkl'))
    feature_names = joblib.load(get_model_path('feature_names.pkl'))
    
    # Dados de teste (paciente típico)
    test_data = {
        'Gender': 'Male',
        'Age': 30,
        'Height': 1.75,
        'Weight': 80,
        'family_history': 'yes',
        'FAVC': 'yes',
        'FCVC': 2.0,
        'NCP': 3.0,
        'CAEC': 'Sometimes',
        'SMOKE': 'no',
        'CH2O': 2.0,
        'SCC': 'no',
        'FAF': 1.0,
        'TUE': 1.0,
        'CALC': 'Sometimes',
        'MTRANS': 'Public_Transportation',
        'BMI': 26.12
    }
    
    try:
        # Criar DataFrame
        df = pd.DataFrame([test_data])
        
        # Encoding
        df_encoded = df.copy()
        for col, encoder in encoders.items():
            if col in df_encoded.columns:
                df_encoded[col] = encoder.transform(df_encoded[col])
        
        # Reordenar colunas
        df_encoded = df_encoded[feature_names]
        
        # Scaling (apenas colunas numéricas)
        numerical_cols = ['Age', 'Height', 'Weight', 'FCVC', 'NCP', 'CH2O', 'FAF', 'TUE', 'BMI']
        df_encoded[numerical_cols] = scaler.transform(df_encoded[numerical_cols])
        
        # Predição
        prediction = model.predict(df_encoded)
        proba = model.predict_proba(df_encoded)
        
        assert prediction is not None, "Predição falhou"
        assert len(proba[0]) == 7, "Probabilidades devem ter 7 classes"
        assert np.isclose(proba[0].sum(), 1.0), "Probabilidades devem somar 1"
        
        print(f"✅ Pipeline de predição funcionando")
        print(f"   Predição: {prediction[0]}")
        print(f"   Confiança: {proba[0].max():.2%}")
        
    except Exception as e:
        assert False, f"Erro no pipeline: {e}"


def test_feature_count():
    """Verificar número correto de features"""
    feature_names = joblib.load(get_model_path('feature_names.pkl'))
    
    expected_count = 17  # Número de features no dataset
    assert len(feature_names) == expected_count, \
        f"Esperado {expected_count} features, encontrado {len(feature_names)}"
    
    print(f"✅ Número correto de features: {len(feature_names)}")


def test_encoders_completeness():
    """Verificar se encoders cobrem todas as variáveis categóricas"""
    encoders = joblib.load(get_model_path('label_encoders.pkl'))
    
    expected_categorical = ['Gender', 'family_history', 'FAVC', 'CAEC', 
                           'SMOKE', 'SCC', 'CALC', 'MTRANS']
    
    for col in expected_categorical:
        assert col in encoders, f"Encoder faltando para {col}"
    
    print(f"✅ Todos os encoders presentes: {len(encoders)} variáveis")


def test_model_accuracy():
    """Verificar se modelo atinge meta de acurácia"""
    try:
        metrics = joblib.load(get_model_path('model_metrics.pkl'))
        
        # Metrics pode ser dict ou outra estrutura
        if isinstance(metrics, dict):
            accuracy = metrics.get('accuracy', 0)
        else:
            accuracy = getattr(metrics, 'accuracy', 0) if hasattr(metrics, 'accuracy') else 0
        
        target_accuracy = 0.75
        
        assert accuracy >= target_accuracy, \
            f"Acurácia {accuracy:.2%} abaixo da meta {target_accuracy:.2%}"
        
        print(f"✅ Acurácia {accuracy:.2%} atinge meta (>{target_accuracy:.2%})")
        
    except FileNotFoundError:
        print("⚠️ Arquivo de métricas não encontrado - pulando teste")


def run_all_tests():
    """Executar todos os testes"""
    print("\n" + "="*60)
    print("🧪 EXECUTANDO TESTES DE VALIDAÇÃO")
    print("="*60 + "\n")
    
    tests = [
        ("Arquivos do Modelo", test_model_files_exist),
        ("Carregamento do Modelo", test_load_model),
        ("Carregamento de Artefatos", test_load_artifacts),
        ("Número de Features", test_feature_count),
        ("Completude dos Encoders", test_encoders_completeness),
        ("Pipeline de Predição", test_prediction_pipeline),
        ("Acurácia do Modelo", test_model_accuracy)
    ]
    
    passed = 0
    failed = 0
    
    for name, test_func in tests:
        try:
            print(f"\n📋 Teste: {name}")
            print("-" * 60)
            test_func()
            passed += 1
        except AssertionError as e:
            print(f"❌ FALHOU: {e}")
            failed += 1
        except Exception as e:
            print(f"❌ ERRO: {e}")
            failed += 1
    
    print("\n" + "="*60)
    print(f"📊 RESULTADO: {passed} passou, {failed} falhou")
    print("="*60 + "\n")
    
    return failed == 0


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
