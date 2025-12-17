# 🚀 Guia Rápido de Início

## ⚡ Início Rápido (5 minutos)

### 1. Instalar Dependências
```bash
pip install -r requirements.txt
```

### 2. Verificar Projeto
```bash
python check_project.py
```

### 3. Executar Notebooks na Ordem

**a) Análise Exploratória (10-15 min)**
```bash
jupyter notebook notebooks/01_exploratory_data_analysis.ipynb
```
- Execute todas as células (Cell > Run All)
- Revise visualizações e insights

**b) Treinamento de Modelos (15-20 min)**
```bash
jupyter notebook notebooks/02_model_training.ipynb
```
- Execute todas as células (Cell > Run All)
- Aguarde treinamento e otimização
- Modelos serão salvos automaticamente em `models/`

### 4. Executar Aplicações Streamlit

**Aplicação de Predição:**
```bash
streamlit run app/app_prediction.py
```
Acesse: http://localhost:8501

**Dashboard Analítico:**
```bash
streamlit run app/app_dashboard.py
```
Acesse: http://localhost:8501

## 📊 O Que Cada Componente Faz

### 📓 Notebook 1 - EDA
- ✅ Carrega e analisa o dataset
- ✅ Cria visualizações (distribuições, correlações, boxplots)
- ✅ Calcula IMC para todos os registros
- ✅ Identifica padrões e insights
- ✅ Salva dataset processado com BMI

### 🤖 Notebook 2 - Treinamento
- ✅ Preprocessa dados (encoding + normalização)
- ✅ Treina 5 modelos diferentes
- ✅ Compara performance
- ✅ Otimiza melhor modelo (GridSearch)
- ✅ Salva todos os artefatos necessários
- ✅ Gera relatórios e visualizações

### 🏥 App de Predição
- ✅ Interface web intuitiva
- ✅ Formulário para entrada de dados
- ✅ Predição em tempo real
- ✅ Probabilidades por classe
- ✅ Recomendações personalizadas
- ✅ Cálculo automático de IMC

### 📈 Dashboard Analítico
- ✅ KPIs do dataset
- ✅ Performance do modelo
- ✅ Visualizações interativas
- ✅ Filtros dinâmicos
- ✅ Insights para equipe médica

## ⏱️ Tempo Estimado

| Etapa | Tempo |
|-------|-------|
| Instalação | 2-3 min |
| EDA | 10-15 min |
| Treinamento | 15-20 min |
| Teste das Apps | 5-10 min |
| **TOTAL** | **~40 min** |

## 🎯 Checklist de Conclusão

- [ ] Dependências instaladas
- [ ] Notebook 1 (EDA) executado
- [ ] Notebook 2 (Treinamento) executado
- [ ] Modelos salvos em `models/`
- [ ] App de predição funcionando
- [ ] Dashboard funcionando
- [ ] Acurácia > 75% alcançada

## 🆘 Problemas Comuns

### ImportError
```bash
pip install -r requirements.txt --upgrade
```

### Modelo não encontrado
- Execute o notebook `02_model_training.ipynb` completo
- Verifique pasta `models/`

### Streamlit não abre
```bash
# Certifique-se de estar na pasta raiz do projeto
cd fiap-tech-challenge-fase4
streamlit run app/app_prediction.py
```

## 💡 Dicas

1. **Execute os notebooks na ordem** (01 → 02)
2. **Aguarde o treinamento completo** antes de usar as apps
3. **Use ambiente virtual** para evitar conflitos
4. **Revise as visualizações** para entender os dados
5. **Teste a predição** com diferentes perfis de pacientes

## 📞 Suporte

- 📖 Leia o [README.md](README.md) completo
- 🔍 Execute `python check_project.py` para diagnóstico
- 📝 Verifique logs de erro no terminal

---

**Boa sorte com o Tech Challenge! 🚀**
