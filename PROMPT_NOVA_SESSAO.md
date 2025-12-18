# 🤖 PROMPT PARA CONTINUAR SESSÃO NO GITHUB COPILOT

> **Copie e cole este texto no início da nova sessão do Copilot**

---

## Prompt Completo:

```
Estou trabalhando no Tech Challenge Fase 4 da POSTECH (pós-graduação em Data Analytics).

OBJETIVO: 
Sistema de ML para predição de níveis de obesidade (7 classes) com >75% de acurácia 
+ aplicações Streamlit (predição individual + dashboard analítico).

ESTADO ATUAL:
✅ Projeto completo estruturado (data/, notebooks/, src/, app/, models/)
✅ Módulo centralizado de traduções criado (src/translations.py)
✅ EDA notebook completo com visualizações profissionais em PT-BR
✅ Model training notebook atualizado com traduções
✅ 2 apps Streamlit prontos (predição + dashboard)
✅ Padronização completa: cores azuis profissionais + traduções PT-BR
✅ Documentação técnica completa

PENDENTE:
⏳ Executar notebooks para treinar modelos
⏳ Testar aplicações Streamlit
⏳ Ajustar dashboard se necessário

PADRÕES TÉCNICOS:
- Cores: PRIMARY=#2c3e50, SECONDARY=#3498db, ACCENT=#e74c3c
- Gradiente azul: Blues colormap, range 0.35-0.95
- Traduções: Centralizadas em src/translations.py
- Dataset: Obesity.csv (2111 registros, 17 features, 7 classes)

ARQUIVOS DE REFERÊNCIA:
- CONTEXTO_PROJETO.md (estado completo do projeto)
- DOCUMENTACAO_TECNICA.md (detalhes técnicos)
- notebooks/00_GUIA_ANALISE.ipynb (contexto analítico e metodologia)
- README.md (setup e instalação)

Leia CONTEXTO_PROJETO.md para detalhes completos antes de começar.
```

---

## Próximos Passos Prioritários:

1. **Treinar Modelos** (30 min)
   - Abrir `notebooks/02_model_training.ipynb`
   - Executar todas as células
   - Verificar se acurácia > 75%

2. **Testar Apps Streamlit** (15 min)
   - `streamlit run app/app_prediction.py`
   - `streamlit run app/app_dashboard.py`
   - Confirmar traduções e cores

3. **Validação Final** (10 min)
   - Rodar `py test_padronizacao.py`
   - Verificar tudo funcionando

---

## Comandos Úteis:

```bash
# Iniciar Jupyter Notebook
jupyter notebook

# Testar App de Predição
streamlit run app/app_prediction.py

# Testar Dashboard
streamlit run app/app_dashboard.py

# Validar padronizações
py test_padronizacao.py
```

---

**Tempo Estimado para Conclusão:** 1 hora
