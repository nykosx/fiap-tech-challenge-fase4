# Documentação técnica

Este documento resume as principais decisões técnicas de padronização e organização do projeto.

## Módulo de traduções e cores

O arquivo [src/translations.py](../src/translations.py) centraliza:

- nomes das variáveis em português (curtos e descritivos);
- descrições mais completas para uso em textos e tooltips;
- rótulos dos níveis de obesidade (em português) e sua ordem lógica;
- traduções de valores categóricos (por exemplo, `yes`/`no`, meios de transporte);
- escalas legíveis para variáveis ordinais (FAF, TUE, CH2O etc.);
- cores padrão do projeto e uma função utilitária `get_color_palette` para gerar paletas coerentes.

As cores base utilizadas nas aplicações são importadas desse módulo (PRIMARY_COLOR, SECONDARY_COLOR, ACCENT_COLOR), garantindo consistência visual entre notebooks e apps.

## Padrão visual

Nos notebooks e no dashboard foram adotados alguns princípios simples de visualização:

- uso de uma paleta de azuis para a maior parte dos gráficos, evitando “rainbow” e combinações muito chamativas;
- títulos e eixos em português, com fonte legível e tamanhos consistentes;
- grades discretas, destaque para médias/limiares quando relevante e rótulos de eixos claros;
- organização dos gráficos por tema (distribuições, correlações, demografia, hábitos de vida) para facilitar leitura.

O objetivo foi manter as visualizações informativas e agradáveis sem exagero de efeitos visuais.

## Integração com notebooks e apps

- O notebook de EDA ([01_exploratory_data_analysis.ipynb](../notebooks/01_exploratory_data_analysis.ipynb)) utiliza as traduções e cores padronizadas para exibir gráficos com rótulos em português e paleta consistente.
- O notebook de modelagem ([02_model_training.ipynb](../notebooks/02_model_training.ipynb)) se beneficia das mesmas convenções quando apresenta gráficos de importância de variáveis e demais visualizações.
- As aplicações Streamlit ([app/app_prediction.py](../app/app_prediction.py) e [app/app_dashboard.py](../app/app_dashboard.py)) importam `translate_variable`, `translate_value`, `get_obesity_label` e `get_color_palette` para:
  - traduzir variáveis e valores diretamente na interface;
  - padronizar as cores dos gráficos interativos;
  - garantir que os nomes e rótulos exibidos ao usuário final sejam os mesmos usados na análise.

## Evolução do dashboard

Durante o desenvolvimento foram levantadas ideias adicionais para o dashboard (como destacar mais os fatores modificáveis, simular intervenções e separar melhor grupos de risco). Diante dos prazos e do escopo do desafio, optou‑se por implementar uma versão mais enxuta, focada em:

- indicadores principais do dataset (total de registros, IMC médio, taxas por classe);
- visualizações de distribuições, correlações, demografia e hábitos;
- exibição resumida das métricas do modelo treinado.

As ideias de evolução futura do dashboard ficaram documentadas apenas em alto nível (por exemplo, criar abas dedicadas a fatores modificáveis ou a perfis de risco) e podem ser retomadas em trabalhos posteriores, caso o projeto avance além do contexto do Tech Challenge.

## Referências

As mesmas referências listadas em METODOLOGIA_E_INSIGHTS.md servem como base para as escolhas de visualização e comunicação dos resultados (organização Mundial da Saúde, literatura sobre obesidade e atividade física, documentação das bibliotecas utilizadas).
