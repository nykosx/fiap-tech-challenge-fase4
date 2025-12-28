# Tech Challenge Fase 4: Predição de Níveis de Obesidade

## 🛠️ STATUS DO PROJETO
**✅ PROJETO COMPLETO - Pronto para uso e avaliação**

## 🎯 Objetivo Principal
Desenvolver um modelo de Machine Learning (Classificação Multiclasse) para prever os níveis de obesidade de pacientes. A solução deve atingir mais de **75% de acurácia** e ser entregue com uma aplicação preditiva em **Streamlit** e um **Dashboard Analítico** para a equipe médica.

## 📊 Dataset Utilizado
O projeto utiliza o dataset `Obesity.csv` (2111 registros), focado em dados de hábitos alimentares e histórico de saúde.

### Variáveis do Dataset:
- **Demográficas**: Gender, Age, Height, Weight
- **Histórico**: family_history (histórico familiar de obesidade)
- **Hábitos Alimentares**: FAVC, FCVC, NCP, CAEC
- **Estilo de Vida**: SMOKE, CH2O, SCC, FAF, TUE, CALC, MTRANS
- **Alvo**: Obesity (7 classes)

### Classes de Obesidade:
1. Insufficient_Weight (Peso Insuficiente)
2. Normal_Weight (Peso Normal)
3. Overweight_Level_I (Sobrepeso Nível I)
4. Overweight_Level_II (Sobrepeso Nível II)
5. Obesity_Type_I (Obesidade Tipo I)
6. Obesity_Type_II (Obesidade Tipo II)
7. Obesity_Type_III (Obesidade Tipo III - Mórbida)

## 🗂 Estrutura do Repositório

```
fiap-tech-challenge-fase4/
├── data/                          # Dados do projeto
│   ├── Obesity.csv               # Dataset original
│   └── Obesity_with_BMI.csv      # Dataset com IMC calculado (gerado)
│
├── notebooks/                     # Notebooks Jupyter
│   ├── 01_exploratory_data_analysis.ipynb    # Análise exploratória completa
│   └── 02_model_training.ipynb              # Treinamento e avaliação de modelos
│
├── src/                          # Código fonte reutilizável
│   └── translations.py          # Traduções e padronizações PT-BR
│
├── models/                       # Modelos treinados e artefatos
│   ├── best_model.pkl           # Melhor modelo treinado
│   ├── label_encoders.pkl       # Encoders para variáveis categóricas
│   ├── target_encoder.pkl       # Encoder para variável alvo
│   ├── scaler.pkl              # Scaler para normalização
│   ├── feature_names.pkl       # Nomes das features
│   └── model_metrics.pkl       # Métricas do modelo
│
├── app/                         # Aplicações Streamlit
│   ├── app_prediction.py       # App de predição individual
│   └── app_dashboard.py        # Dashboard analítico
│
├── tests/                       # Testes automatizados
│   └── test_model.py           # Testes do pipeline ML
│
├── docs/                        # Documentação técnica
│   └── DOCUMENTACAO_TECNICA.md # Detalhes de implementação
│
├── links_entrega.txt           # Links de entrega do projeto
├── requirements.txt             # Dependências do projeto
├── .gitignore                  # Arquivos ignorados pelo Git
└── README.md                   # Este arquivo
```

## 🚀 Como Executar o Projeto

### 1️⃣ Pré-requisitos
- Python 3.9+
- pip (gerenciador de pacotes Python)

### 2️⃣ Instalação

```bash
# Clone o repositório
git clone <url-do-repositorio>
cd fiap-tech-challenge-fase4

# Crie um ambiente virtual (recomendado)
python -m venv venv

# Ative o ambiente virtual
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Instale as dependências
pip install -r requirements.txt
```

### 3️⃣ Executar Análise Exploratória

```bash
# Abra o Jupyter Notebook
jupyter notebook

# Navegue até notebooks/01_exploratory_data_analysis.ipynb
# Execute todas as células
```

**O que você verá:**
- ✅ Análise detalhada do dataset
- ✅ Visualizações de distribuições
- ✅ Correlações entre variáveis
- ✅ Insights sobre padrões de obesidade
- ✅ Cálculo de IMC para todos os registros

### 4️⃣ Treinar Modelos

```bash
# No Jupyter Notebook, abra:
# notebooks/02_model_training.ipynb
# Execute todas as células
```

**O que acontece:**
- ✅ Preprocessamento automático dos dados
- ✅ Treinamento de 5 modelos diferentes:
  - Logistic Regression
  - Decision Tree
  - Random Forest
  - Gradient Boosting
  - XGBoost
- ✅ Comparação de modelos com múltiplas métricas
- ✅ **Análise de Feature Importance** (identifica variáveis mais impactantes)
- ✅ Otimização do melhor modelo (GridSearch)
- ✅ **Feature Importance do Modelo Otimizado** (análise crítica)
- ✅ **Teste Experimental: Modelo Comportamental** (sem Height/Weight/BMI)
- ✅ Comparação: Modelo Completo vs Comportamental
- ✅ Salvamento de artefatos em `models/`

**Meta:** Acurácia > 75%

**Insights Importantes:**
- 🔬 Feature Importance revela quais variáveis são mais importantes
- 📊 Modelo comportamental testa predição sem medições físicas
- 💡 Análise crítica sobre redundância matemática de BMI

### 5️⃣ Executar Aplicação de Predição

```bash
# Execute a aplicação Streamlit
streamlit run app/app_prediction.py
```

**Funcionalidades:**
- 🏥 Formulário interativo para entrada de dados do paciente
- 🎯 Predição do nível de obesidade
- 📊 Probabilidades para cada classe
- 💡 Recomendações personalizadas
- 📈 Cálculo automático de IMC

### 6️⃣ Executar Dashboard Analítico

```bash
# Execute o dashboard
streamlit run app/app_dashboard.py
```

**Funcionalidades:**
- 📊 KPIs principais do dataset
- 🤖 Métricas de performance do modelo
- 📈 Visualizações interativas:
  - Distribuições de variáveis
  - Matriz de correlação
  - Análise demográfica
  - Hábitos de vida
- 🔍 Filtros dinâmicos
- 💡 Insights e recomendações para equipe médica

## 💻 Tecnologias Utilizadas

### Core
- **Python 3.9+**: Linguagem principal
- **Pandas**: Manipulação de dados
- **NumPy**: Computação numérica
- **Scikit-learn**: Machine Learning

### Machine Learning
- **RandomForestClassifier**: Modelo ensemble
- **XGBoost**: Gradient boosting otimizado
- **GradientBoostingClassifier**: Boosting tradicional
- **LabelEncoder**: Codificação de variáveis categóricas
- **StandardScaler**: Normalização de features

### Visualização
- **Matplotlib**: Gráficos estáticos
- **Seaborn**: Visualizações estatísticas
- **Plotly**: Gráficos interativos

### Aplicação Web
- **Streamlit**: Framework para apps de ML
- **Joblib**: Serialização de modelos

## 📈 Resultados Esperados

### Métricas do Modelo
- 🎯 **Acurácia**: > 75% (meta do projeto)
- 📊 **Precisão**: Alta para todas as classes
- 🔄 **Recall**: Balanceado entre classes
- 📉 **F1-Score**: Métrica harmônica otimizada

### Entregáveis
1. ✅ Notebook de EDA completo com insights
2. ✅ Notebook de treinamento com múltiplos modelos
3. ✅ Modelo otimizado salvo e pronto para produção
4. ✅ Aplicação web de predição funcional
5. ✅ Dashboard analítico interativo
6. ✅ Documentação completa

## 🔄 Workflow do Projeto

```
1. Carregar Dados (data/Obesity.csv)
   ↓
2. Análise Exploratória (EDA)
   - Estatísticas descritivas
   - Visualizações
   - Detecção de padrões
   ↓
3. Preprocessamento
   - Codificação de categóricas
   - Normalização de numéricas
   - Cálculo de IMC
   ↓
4. Treinamento de Modelos
   - 5 algoritmos diferentes
   - Cross-validation
   - Comparação de métricas
   ↓
5. Otimização (GridSearch)
   - Busca de hiperparâmetros
   - Validação cruzada
   ↓
6. Salvamento de Artefatos
   - Modelo treinado
   - Encoders e Scaler
   - Métricas
   ↓
7. Deploy em Streamlit
   - App de Predição
   - Dashboard Analítico
```

## 🎓 Conceitos de ML Aplicados

- **Classificação Multiclasse**: 7 classes de obesidade
- **Feature Engineering**: Criação de IMC como feature derivada
- **Preprocessing**: Label Encoding + Standard Scaling
- **Ensemble Methods**: Random Forest, Gradient Boosting
- **Hyperparameter Tuning**: GridSearchCV
- **Cross-Validation**: Validação cruzada k-fold
- **Model Evaluation**: Múltiplas métricas (accuracy, precision, recall, F1)

## 📝 Observações Importantes

1. **Dados Balanceados**: Verificar balanceamento das classes no EDA
2. **Features Importantes**: Height, Weight, BMI são altamente correlacionadas com obesidade
3. **Histórico Familiar**: Feature relevante para predição
4. **Hábitos de Vida**: FAVC, FAF, MTRANS são bons preditores
5. **IMC**: Feature derivada crucial para classificação

## ⚠️ Limitações do Modelo

### Limitações Técnicas:
1. **Multicolinearidade**: Height, Weight e BMI são altamente correlacionados (VIF > 20), o que pode afetar a interpretabilidade dos coeficientes em modelos lineares
2. **Overfitting Potencial**: Acurácia de 99.05% pode indicar ajuste excessivo aos dados de treinamento
3. **Generalização**: Modelo treinado em dataset sintético/acadêmico - performance em dados reais pode variar
4. **Dados Sintéticos**: Dataset original possui padrões muito regulares que podem não refletir a complexidade do mundo real

### Limitações Práticas:
1. **Dependência de Medições**: Requer dados antropométricos (altura, peso) que nem sempre estão disponíveis
2. **Auto-reporte**: Variáveis comportamentais dependem de respostas honestas do paciente
3. **Contexto Cultural**: Hábitos alimentares e de transporte podem variar entre culturas/regiões
4. **Temporal**: Não considera mudanças ao longo do tempo (snapshot único)

### Limitações de Aplicação:
1. **Não é Diagnóstico Médico**: Ferramenta de apoio, não substitui avaliação médica profissional
2. **Faixa Etária**: Não validado para crianças, adolescentes ou idosos
3. **Condições Especiais**: Não considera gestação, condições médicas especiais, atletas
4. **Viés de Amostra**: Dataset pode não representar adequadamente todas as populações

## 🐛 Troubleshooting

### Erro ao carregar modelo
```python
# Certifique-se de executar o notebook de treinamento primeiro
# Os modelos devem estar em models/
```

### Erro de importação
```bash
# Reinstale as dependências
pip install -r requirements.txt --upgrade
```

### Streamlit não abre
```bash
# Verifique se está na pasta correta
# Execute: streamlit run app/app_prediction.py
# Acesse: http://localhost:8501
```

## 📚 Próximos Passos (Melhorias Futuras)

### 🔬 Melhorias no Modelo:
- [ ] **Validação Cruzada Estratificada**: Implementar StratifiedKFold para garantir distribuição equilibrada
- [ ] **Feature Engineering Avançado**: Criar razões e interações entre features (ex: razão cintura-quadril)
- [ ] **Ensemble Learning**: Combinar múltiplos modelos (Voting/Stacking) para melhor generalização
- [ ] **Regularização**: Adicionar L1/L2 para reduzir overfitting
- [ ] **Análise de Viés**: Avaliar performance por gênero, idade, etnia

### 📊 Melhorias nos Dados:
- [ ] **Coleta de Dados Reais**: Validar modelo com dados clínicos reais
- [ ] **Aumento de Dataset**: Incorporar mais variáveis (glicemia, pressão arterial, colesterol)
- [ ] **Dados Temporais**: Coletar histórico longitudinal para prever progressão
- [ ] **SMOTE/ADASYN**: Balanceamento inteligente se houver desbalanceamento

### 💻 Melhorias Técnicas:
- [ ] **Testes Automatizados**: Implementar pytest para validação contínua
- [ ] **CI/CD Pipeline**: GitHub Actions para testes e deploy automático
- [ ] **API REST**: Criar FastAPI para integração com sistemas externos
- [ ] **Containerização**: Docker para facilitar deployment
- [ ] **Monitoramento**: MLflow para tracking de experimentos e métricas
- [ ] **Versionamento de Dados**: DVC para gerenciar datasets e modelos

### 🚀 Melhorias nas Aplicações:
- [ ] **Autenticação**: Sistema de login para controle de acesso
- [ ] **Histórico de Predições**: Armazenar e visualizar predições anteriores
- [ ] **Comparação Temporal**: Acompanhar evolução do paciente ao longo do tempo
- [ ] **Exportar Relatórios**: Gerar PDFs com resultados e recomendações
- [ ] **Mobile App**: Versão para smartphones (React Native/Flutter)
- [ ] **Chatbot**: Interface conversacional para coleta de dados

### 🧠 Melhorias em Interpretabilidade:
- [ ] **SHAP Values**: Explicabilidade detalhada das predições
- [ ] **LIME**: Explicações locais para casos individuais
- [ ] **Feature Importance Plots**: Visualizações interativas
- [ ] **Counterfactual Explanations**: "O que mudaria o resultado?"

### 🌐 Deployment e Escalabilidade:
- [ ] **Cloud Deployment**: AWS/GCP/Azure para escalabilidade
- [ ] **Load Balancing**: Suportar múltiplos usuários simultâneos
- [ ] **Edge Computing**: Executar modelo em dispositivos locais
- [ ] **Batch Processing**: Pipeline para processar múltiplos pacientes

### 📈 Extensões do Projeto:
- [ ] **Modelo de Séries Temporais**: Prever evolução futura da obesidade
- [ ] **Sistema de Recomendação**: Planos personalizados de dieta/exercício
- [ ] **Gamificação**: Sistema de pontos/badges para engajar usuários
- [ ] **Integração com Wearables**: Fitbit, Apple Watch, etc.

## 👥 Grupo

**POSTECH Data Analytics - 9DTAT**  
Tech Challenge - Fase 4

**Integrantes:**
- Thiago Cesar Silva
- Vitor da Silva Ammari
- João Marcos Marques Messias
- João Pedro de Jesus
- Nykolas Vieira Albino dos Santos

## 📄 Licença

Este projeto foi desenvolvido para fins educacionais como parte do Tech Challenge da POSTECH.

---

**Desenvolvido para o Tech Challenge Fase 4 - POSTECH Data Analytics - 9DTAT**
