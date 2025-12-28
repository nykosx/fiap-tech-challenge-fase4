@echo off
REM Script de Limpeza do Projeto - Tech Challenge Fase 4
REM Execute este script para preparar o projeto para entrega

echo ============================================
echo LIMPEZA DO PROJETO TECH CHALLENGE FASE 4
echo ============================================
echo.

REM Remover arquivos de desenvolvimento
echo [1/6] Removendo arquivos de desenvolvimento...
if exist PROMPT_NOVA_SESSAO.md del /Q PROMPT_NOVA_SESSAO.md
if exist test_padronizacao.py del /Q test_padronizacao.py
if exist check_project.py del /Q check_project.py
if exist run_pipeline.py del /Q run_pipeline.py
if exist CONTEXTO_PROJETO.md del /Q CONTEXTO_PROJETO.md
if exist ALTERACOES_REALIZADAS.md del /Q ALTERACOES_REALIZADAS.md
if exist AVALIACAO_PROJETO.md del /Q AVALIACAO_PROJETO.md
if exist PROXIMOS_PASSOS.md del /Q PROXIMOS_PASSOS.md
if exist MELHORIAS_APLICADAS.md del /Q MELHORIAS_APLICADAS.md
if exist GUIA_RAPIDO.md del /Q GUIA_RAPIDO.md
if exist TESTES_CORRIGIDOS.md del /Q TESTES_CORRIGIDOS.md
if exist run_tests.py del /Q run_tests.py
if exist run_tests_debug.py del /Q run_tests_debug.py
if exist quick_test.py del /Q quick_test.py
if exist inspect_models.py del /Q inspect_models.py
if exist test_output.log del /Q test_output.log
echo    OK - Arquivos removidos

REM Remover arquivos Python não utilizados
echo [2/6] Removendo arquivos Python nao utilizados...
if exist src\preprocessing.py del /Q src\preprocessing.py
if exist src\model_utils.py del /Q src\model_utils.py
if exist tests\test_model_simple.py del /Q tests\test_model_simple.py
echo    OK - Arquivos Python removidos

REM Criar pasta docs e mover PDFs
echo [3/6] Organizando documentacao...
if not exist docs mkdir docs
if exist "POSTECH - Tech Challenge - Fase 4 -  Data Analytics_.pdf" move /Y "POSTECH - Tech Challenge - Fase 4 -  Data Analytics_.pdf" docs\ >nul
if exist dicionario_obesity_fiap.pdf move /Y dicionario_obesity_fiap.pdf docs\ >nul
if exist DOCUMENTACAO_TECNICA.md move /Y DOCUMENTACAO_TECNICA.md docs\ >nul
echo    OK - Documentos organizados em /docs/

REM Limpar cache Python
echo [4/6] Removendo cache Python...
if exist __pycache__ rmdir /s /q __pycache__
if exist src\__pycache__ rmdir /s /q src\__pycache__
if exist app\__pycache__ rmdir /s /q app\__pycache__
del /s /q *.pyc 2>nul
echo    OK - Cache removido

REM Limpar checkpoints Jupyter
echo [5/6] Removendo checkpoints Jupyter...
if exist notebooks\.ipynb_checkpoints rmdir /s /q notebooks\.ipynb_checkpoints
if exist .ipynb_checkpoints rmdir /s /q .ipynb_checkpoints
echo    OK - Checkpoints removidos

REM Limpar artifacts temporários
echo [6/6] Removendo artifacts temporarios...
if exist artifacts rmdir /s /q artifacts
echo    OK - Artifacts removidos

echo.
echo ============================================
echo LIMPEZA CONCLUIDA COM SUCESSO!
echo ============================================
echo.
echo Proximos passos:
echo 1. Revisar README.md
echo 2. Testar aplicacoes Streamlit
echo 3. Validar notebooks
echo 4. Gerar arquivo ZIP para entrega
echo.
echo Pressione qualquer tecla para sair...
pause >nul
