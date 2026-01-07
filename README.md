# Tech Challenge Fase 4: Predição de Níveis de Obesidade

## Status do projeto
**Projeto completo - pronto para uso e avaliação**

## Objetivo principal
Desenvolver um modelo de Machine Learning (Classificação Multiclasse) para prever os níveis de obesidade de pacientes. A solução deve atingir mais de **75% de acurácia** e ser entregue com uma aplicação preditiva em **Streamlit** e um **Dashboard Analítico** para a equipe médica.

## Dataset utilizado
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

## Estrutura do repositório

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

## Como executar o projeto

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
- Análise detalhada do dataset
- Visualizações de distribuições
- Correlações entre variáveis
- Insights sobre padrões de obesidade
- Cálculo de IMC para todos os registros

### 4️⃣ Treinar Modelos

```bash
# No Jupyter Notebook, abra:
# notebooks/02_model_training.ipynb
# Execute todas as células
```

**O que acontece:**
- Preprocessamento automático dos dados
- Treinamento de 5 modelos diferentes:
  - Logistic Regression
  - Decision Tree
  - Random Forest
  - Gradient Boosting
  - XGBoost
- Comparação de modelos com múltiplas métricas
- Análise de feature importance (variáveis mais impactantes)
- Otimização do melhor modelo (GridSearch)
- Teste experimental: modelo comportamental (sem Height/Weight/BMI)
- Comparação entre modelo completo e comportamental
- Salvamento de artefatos em `models/`

**Meta:** acurácia > 75%

**Insights importantes:**
- Feature importance mostra quais variáveis são mais importantes
- Modelo comportamental testa predição sem medições físicas
- Análise crítica sobre redundância matemática de BMI

### 5️⃣ Executar Aplicação de Predição

```bash
# Execute a aplicação Streamlit
streamlit run app/app_prediction.py
```

**Funcionalidades:**
- Formulário interativo para entrada de dados do paciente
- Predição do nível de obesidade
- Probabilidades para cada classe
- Recomendações personalizadas
- Cálculo automático de IMC

### 6️⃣ Executar Dashboard Analítico

```bash
# Execute o dashboard
streamlit run app/app_dashboard.py
```

**Funcionalidades:**
- KPIs principais do dataset
- Métricas de performance do modelo
- Visualizações interativas:
  - Distribuições de variáveis
  - Matriz de correlação
  - Análise demográfica
  - Hábitos de vida
- Filtros dinâmicos
- Insights e recomendações para equipe médica

## Tecnologias utilizadas

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

## Resultados alcançados

### Métricas do modelo completo (com variáveis antropométricas)
- **Acurácia no conjunto de teste**: aproximadamente 99% (acima da meta de 75%)
- **Cross-validation**: média próxima de 99%, consistente com o teste
- **F1-Score**: elevado para todas as classes
- **Observação conceitual**: grande parte da importância vem de Height/Weight/BMI (circularidade metodológica)

### Métricas do modelo comportamental (sem variáveis antropométricas)
- **Acurácia**: aproximadamente 87% (ainda acima da meta de 75%)
- **Features**: apenas variáveis comportamentais e demográficas (sem Weight, Height, BMI)
- **Aplicação**: viável para screening remoto sem medições físicas
- **Principais variáveis**: FAF (atividade física), FCVC (vegetais), Age, FAVC (alimentos calóricos), family_history

**Análise detalhada de métricas e feature importance**: ver [notebook de treinamento](notebooks/02_model_training.ipynb)

### Entregáveis
1. Notebook de EDA completo com insights
2. Notebook de treinamento com múltiplos modelos e avaliação de desempenho
3. Modelo otimizado salvo e pronto para uso
4. Aplicação web de predição funcional
5. Dashboard analítico interativo
6. Documentação completa

## Workflow do projeto

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

## Conceitos de ML aplicados

- **Classificação Multiclasse**: 7 classes de obesidade
- **Feature Engineering**: Criação de IMC como feature derivada
- **Preprocessing**: Label Encoding + Standard Scaling
- **Ensemble Methods**: Random Forest, Gradient Boosting
- **Hyperparameter Tuning**: GridSearchCV
- **Cross-Validation**: Validação cruzada k-fold
- **Model Evaluation**: Múltiplas métricas (accuracy, precision, recall, F1)

## Observações importantes

1. **Dados Balanceados**: Verificar balanceamento das classes no EDA
2. **Features Importantes**: Height, Weight, BMI são altamente correlacionadas com obesidade
3. **Histórico Familiar**: Feature relevante para predição
4. **Hábitos de Vida**: FAVC, FAF, MTRANS são bons preditores
5. **IMC**: Feature derivada crucial para classificação

## Limitações do modelo

### Limitações Técnicas:

1. **Circularidade Metodológica** ⚠️ **[CRÍTICO]**:
   - Height, Weight e BMI representam **67.17%** da importância total do modelo
   - Classes de obesidade SÃO DEFINIDAS por faixas de IMC (calculado como `Weight/Height²`)
   - Modelo "aprende" essa fórmula matemática ao invés de descobrir padrões comportamentais
   - Acurácia muito alta é esperada (não surpreendente) devido a essa circularidade
   - Análise detalhada disponível no [notebook de treinamento](notebooks/02_model_training.ipynb)

2. **Análise de overfitting**:
   - Avaliação de desempenho indica boa generalização no conjunto de teste
   - O principal ponto de atenção é conceitual (circularidade), não técnico (sobreajuste)

3. **Multicolinearidade**: 
   - Height, Weight e BMI são altamente correlacionados (VIF > 20)
   - Afeta interpretabilidade em modelos lineares, mas não em Random Forest
   - Distribuição de importância: BMI (41%), Weight (21%), Height (5%)

4. **Generalização**: 
   - Modelo treinado em dataset sintético/acadêmico
   - Performance em dados reais pode variar
   - Dataset possui padrões muito regulares (não reflete complexidade real)

### Limitações Práticas:

1. **Dependência de Medições**: 
   - Requer dados antropométricos (altura, peso) que nem sempre estão disponíveis
   - **Solução**: Modelo comportamental (sem Weight/Height/BMI) atinge **87.47%** de acurácia
   - Viabiliza screening remoto/online sem balança ou fita métrica

2. **Auto-reporte**: 
   - Variáveis comportamentais dependem de respostas honestas do paciente
   - Risco de viés de desejabilidade social (subestimar consumo calórico, superestimar exercício)

3. **Contexto Cultural**: 
   - Hábitos alimentares e de transporte podem variar entre culturas/regiões
   - Dataset pode não representar padrões brasileiros adequadamente

4. **Temporal**: 
   - Não considera mudanças ao longo do tempo (snapshot único)
   - Não prevê progressão ou evolução futura

### Limitações de Aplicação:
1. **Não é Diagnóstico Médico**: Ferramenta de apoio, não substitui avaliação médica profissional
2. **Faixa Etária**: Não validado para crianças, adolescentes ou idosos
3. **Condições Especiais**: Não considera gestação, condições médicas especiais, atletas
4. **Viés de Amostra**: Dataset pode não representar adequadamente todas as populações

## Troubleshooting

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

## Possíveis melhorias futuras

- **Validação com Dados Reais**: Testar modelo com dados clínicos reais de hospitais/clínicas
- **Comparação Temporal**: Acompanhar evolução do paciente ao longo do tempo com gráficos de tendência
- **Exportar Relatórios**: Gerar PDFs com resultados, recomendações e histórico para compartilhamento
- **API REST**: Criar API com FastAPI para integração com sistemas externos

## Grupo

**POSTECH Data Analytics - 9DTAT**  
Tech Challenge - Fase 4

**Integrantes:**
- Thiago Cesar Silva
- Vitor da Silva Ammari
- João Marcos Marques Messias
- João Pedro de Jesus
- Nykolas Vieira Albino dos Santos

## Licença

Este projeto foi desenvolvido para fins educacionais como parte do Tech Challenge da POSTECH.

---

Desenvolvido para o Tech Challenge Fase 4 - POSTECH Data Analytics - 9DTAT
