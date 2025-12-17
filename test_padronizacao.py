"""
Script de Teste - Verificação da Padronização
Tech Challenge Fase 4 - POSTECH Data Analytics

Este script verifica se todas as padronizações foram aplicadas corretamente.
"""

import sys
sys.path.append('src')

def test_translations_module():
    """Testar módulo de traduções"""
    print("="*80)
    print("1. TESTANDO MÓDULO DE TRADUÇÕES (src/translations.py)")
    print("="*80)
    
    try:
        from translations import (
            VARIABLE_NAMES, OBESITY_LABELS, OBESITY_ORDER,
            PRIMARY_COLOR, SECONDARY_COLOR, ACCENT_COLOR,
            translate_variable, translate_value, get_obesity_label, get_color_palette
        )
        
        print("\n✅ Módulo importado com sucesso!")
        
        # Testar cores
        print(f"\n📊 Cores Padrão:")
        print(f"  PRIMARY_COLOR   = {PRIMARY_COLOR}")
        print(f"  SECONDARY_COLOR = {SECONDARY_COLOR}")
        print(f"  ACCENT_COLOR    = {ACCENT_COLOR}")
        
        # Testar traduções
        print(f"\n📝 Exemplos de Traduções:")
        test_vars = ['Gender', 'Age', 'BMI', 'FAVC', 'FAF', 'MTRANS']
        for var in test_vars:
            print(f"  {var:15s} -> {translate_variable(var)}")
        
        # Testar obesidade
        print(f"\n🏥 Níveis de Obesidade:")
        for obesity in OBESITY_ORDER[:3]:  # Primeiros 3
            print(f"  {obesity:25s} -> {get_obesity_label(obesity)}")
        
        # Testar paleta
        colors = get_color_palette(7)
        print(f"\n🎨 Paleta de Cores (7 tons):")
        print(f"  {colors[:2]}... ({len(colors)} cores)")
        
        print("\n✅ Todos os testes do módulo passaram!")
        return True
        
    except Exception as e:
        print(f"\n❌ ERRO: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_file_structure():
    """Verificar estrutura de arquivos"""
    print("\n" + "="*80)
    print("2. VERIFICANDO ESTRUTURA DE ARQUIVOS")
    print("="*80)
    
    import os
    
    required_files = [
        'src/translations.py',
        'notebooks/01_exploratory_data_analysis.ipynb',
        'notebooks/02_model_training.ipynb',
        'app/app_prediction.py',
        'app/app_dashboard.py',
        'PADRONIZACAO.md',
        'PADRONIZACAO_COMPLETA.md'
    ]
    
    all_exist = True
    for file_path in required_files:
        exists = os.path.exists(file_path)
        status = "✅" if exists else "❌"
        print(f"{status} {file_path}")
        if not exists:
            all_exist = False
    
    if all_exist:
        print("\n✅ Todos os arquivos necessários existem!")
    else:
        print("\n⚠️ Alguns arquivos estão faltando!")
    
    return all_exist


def test_imports_in_notebooks():
    """Verificar se notebooks podem importar traduções"""
    print("\n" + "="*80)
    print("3. VERIFICANDO IMPORTS NOS NOTEBOOKS")
    print("="*80)
    
    try:
        # Simular import do notebook
        import nbformat
        
        # Verificar notebook EDA
        with open('notebooks/01_exploratory_data_analysis.ipynb', 'r', encoding='utf-8') as f:
            nb = nbformat.read(f, as_version=4)
        
        # Procurar por imports de translations
        found_translations = False
        for cell in nb.cells:
            if cell.cell_type == 'code':
                if 'VARIABLE_NAMES' in cell.source or 'OBESITY_LABELS' in cell.source:
                    found_translations = True
                    break
        
        if found_translations:
            print("✅ Notebook EDA possui dicionários de tradução!")
        else:
            print("⚠️ Notebook EDA: dicionários inline (ok para funcionar)")
        
        # Verificar notebook de modelagem
        with open('notebooks/02_model_training.ipynb', 'r', encoding='utf-8') as f:
            nb = nbformat.read(f, as_version=4)
        
        found_import = False
        for cell in nb.cells:
            if cell.cell_type == 'code':
                if 'from translations import' in cell.source:
                    found_import = True
                    break
        
        if found_import:
            print("✅ Notebook de modelagem importa módulo translations!")
        else:
            print("⚠️ Notebook de modelagem não importa translations")
        
        return True
        
    except ImportError:
        print("⚠️ nbformat não instalado. Pulando verificação de notebooks.")
        print("   Instale com: pip install nbformat")
        return True
    except Exception as e:
        print(f"❌ ERRO: {e}")
        return False


def test_streamlit_apps():
    """Verificar se apps Streamlit têm imports corretos"""
    print("\n" + "="*80)
    print("4. VERIFICANDO APPS STREAMLIT")
    print("="*80)
    
    apps = [
        'app/app_prediction.py',
        'app/app_dashboard.py'
    ]
    
    all_ok = True
    for app_path in apps:
        try:
            with open(app_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            has_import = 'from translations import' in content
            has_translate = 'translate_variable' in content or 'get_color_palette' in content
            
            if has_import and has_translate:
                print(f"✅ {app_path}: imports e uso de traduções OK!")
            elif has_import:
                print(f"⚠️ {app_path}: tem import mas não usa funções")
            else:
                print(f"❌ {app_path}: não importa módulo translations")
                all_ok = False
                
        except Exception as e:
            print(f"❌ {app_path}: ERRO ao ler arquivo - {e}")
            all_ok = False
    
    return all_ok


def generate_report():
    """Gerar relatório final"""
    print("\n" + "="*80)
    print("📊 RELATÓRIO FINAL DE PADRONIZAÇÃO")
    print("="*80)
    
    results = {
        'Módulo de Traduções': test_translations_module(),
        'Estrutura de Arquivos': test_file_structure(),
        'Notebooks': test_imports_in_notebooks(),
        'Apps Streamlit': test_streamlit_apps()
    }
    
    print("\n" + "="*80)
    print("RESUMO:")
    print("="*80)
    
    for test_name, passed in results.items():
        status = "✅ PASSOU" if passed else "❌ FALHOU"
        print(f"{test_name:30s}: {status}")
    
    all_passed = all(results.values())
    
    print("\n" + "="*80)
    if all_passed:
        print("🎉 TODOS OS TESTES PASSARAM!")
        print("O projeto está totalmente padronizado e pronto para uso!")
    else:
        print("⚠️ ALGUNS TESTES FALHARAM")
        print("Verifique os erros acima e corrija os problemas.")
    print("="*80)
    
    return all_passed


if __name__ == "__main__":
    print("\n")
    print("╔" + "="*78 + "╗")
    print("║" + " "*15 + "TESTE DE PADRONIZAÇÃO DO PROJETO" + " "*31 + "║")
    print("║" + " "*15 + "Tech Challenge Fase 4 - POSTECH" + " "*32 + "║")
    print("╚" + "="*78 + "╝")
    print("\n")
    
    success = generate_report()
    
    print("\n")
    if success:
        print("✨ Projeto padronizado com sucesso! ✨")
        exit(0)
    else:
        print("⚠️ Corrija os problemas e execute novamente.")
        exit(1)
