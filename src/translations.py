"""
Dicionário de Traduções e Padronização
Tech Challenge Fase 4 - POSTECH Data Analytics

Baseado no dicionário de dados oficial (dicionario_obesity_fiap.pdf)
"""

# ============================================================================
# CORES PADRÃO DO PROJETO
# ============================================================================

PRIMARY_COLOR = '#1a252f'      # Azul muito escuro (quase navy)
SECONDARY_COLOR = '#2c5f7c'    # Azul médio escurecido
ACCENT_COLOR = '#8b3a3a'       # Vermelho escuro/bordô

# ============================================================================
# TRADUÇÃO DE VARIÁVEIS
# ============================================================================

VARIABLE_NAMES = {
    # Informações demográficas
    'Gender': 'Gênero',
    'Age': 'Idade',
    
    # Medidas físicas
    'Height': 'Altura',
    'Weight': 'Peso',
    'BMI': 'IMC',
    
    # Histórico e genética
    'family_history': 'Histórico Familiar de Obesidade',
    
    # Hábitos alimentares
    'FAVC': 'Consumo de Alimentos Calóricos',
    'FCVC': 'Consumo de Vegetais',
    'NCP': 'Refeições Principais por Dia',
    'CAEC': 'Consumo Entre Refeições',
    
    # Hábitos de saúde
    'SMOKE': 'Fumante',
    'CH2O': 'Consumo de Água',
    'SCC': 'Monitora Calorias',
    
    # Atividade física
    'FAF': 'Atividade Física',
    'TUE': 'Tempo em Telas',
    
    # Outros hábitos
    'CALC': 'Consumo de Álcool',
    'MTRANS': 'Meio de Transporte',
    
    # Variável alvo
    'Obesity': 'Nível de Obesidade'
}

# Nomes completos (para textos mais detalhados)
VARIABLE_DESCRIPTIONS = {
    'Gender': 'Sexo biológico',
    'Age': 'Idade em anos',
    'Height': 'Altura em metros',
    'Weight': 'Peso em quilogramas',
    'BMI': 'Índice de Massa Corporal',
    'family_history': 'Histórico familiar de excesso de peso',
    'FAVC': 'Consumo frequente de alimentos muito calóricos',
    'FCVC': 'Frequência de consumo de vegetais nas refeições',
    'NCP': 'Número de refeições principais por dia',
    'CAEC': 'Consumo de lanches/comidas entre as refeições',
    'SMOKE': 'Hábito de fumar',
    'CH2O': 'Consumo diário de água',
    'SCC': 'Monitora a ingestão calórica diária',
    'FAF': 'Frequência semanal de atividade física',
    'TUE': 'Tempo diário usando dispositivos eletrônicos',
    'CALC': 'Consumo de bebidas alcoólicas',
    'MTRANS': 'Meio de transporte habitual',
    'Obesity': 'Classe de peso corporal / Nível de obesidade'
}

# ============================================================================
# TRADUÇÃO DOS NÍVEIS DE OBESIDADE
# ============================================================================

OBESITY_LABELS = {
    'Insufficient_Weight': 'Peso Insuficiente',
    'Normal_Weight': 'Peso Normal',
    'Overweight_Level_I': 'Sobrepeso I',
    'Overweight_Level_II': 'Sobrepeso II',
    'Obesity_Type_I': 'Obesidade I',
    'Obesity_Type_II': 'Obesidade II',
    'Obesity_Type_III': 'Obesidade III'
}

# Ordem lógica das classes de obesidade
OBESITY_ORDER = [
    'Insufficient_Weight',
    'Normal_Weight',
    'Overweight_Level_I',
    'Overweight_Level_II',
    'Obesity_Type_I',
    'Obesity_Type_II',
    'Obesity_Type_III'
]

# Descrições detalhadas dos níveis de obesidade (baseado em OMS)
OBESITY_DESCRIPTIONS = {
    'Insufficient_Weight': 'IMC < 18.5 - Risco de desnutrição',
    'Normal_Weight': 'IMC 18.5-24.9 - Peso saudável',
    'Overweight_Level_I': 'IMC 25-27.4 - Sobrepeso leve',
    'Overweight_Level_II': 'IMC 27.5-29.9 - Sobrepeso moderado',
    'Obesity_Type_I': 'IMC 30-34.9 - Obesidade grau I',
    'Obesity_Type_II': 'IMC 35-39.9 - Obesidade grau II (severa)',
    'Obesity_Type_III': 'IMC ≥ 40 - Obesidade grau III (mórbida)'
}

# ============================================================================
# TRADUÇÃO DE VALORES CATEGÓRICOS
# ============================================================================

VALUE_TRANSLATIONS = {
    # Gênero
    'Female': 'Feminino',
    'Male': 'Masculino',
    
    # Respostas sim/não
    'yes': 'Sim',
    'no': 'Não',
    
    # Frequências
    'Sometimes': 'Às vezes',
    'Frequently': 'Frequentemente',
    'Always': 'Sempre',
    
    # Meios de transporte
    'Public_Transportation': 'Transporte Público',
    'Automobile': 'Automóvel',
    'Motorbike': 'Motocicleta',
    'Bike': 'Bicicleta',
    'Walking': 'Caminhando'
}

# ============================================================================
# ESCALAS E CATEGORIAS DE VARIÁVEIS
# ============================================================================

# Escalas das variáveis ordinais
VARIABLE_SCALES = {
    'FCVC': {
        1: 'Raramente (1)',
        2: 'Às vezes (2)',
        3: 'Sempre (3)'
    },
    'NCP': {
        1: '1 refeição',
        2: '2 refeições',
        3: '3 refeições',
        4: '4+ refeições'
    },
    'CH2O': {
        1: '< 1 litro',
        2: '1-2 litros',
        3: '> 2 litros'
    },
    'FAF': {
        0: 'Sedentário',
        1: '1x/semana',
        2: '2x/semana',
        3: '3x/semana',
        4: '4x/semana',
        5: '5+ x/semana'
    },
    'TUE': {
        0: 'Não usa',
        1: '0-2h/dia',
        2: '3-5h/dia',
        3: '> 5h/dia'
    }
}

# ============================================================================
# FUNÇÕES AUXILIARES
# ============================================================================

def translate_variable(var_name: str, full_description: bool = False) -> str:
    """
    Traduz nome de variável para português.
    
    Args:
        var_name: Nome da variável em inglês
        full_description: Se True, retorna descrição completa
        
    Returns:
        Nome traduzido da variável
    """
    if full_description:
        return VARIABLE_DESCRIPTIONS.get(var_name, var_name)
    return VARIABLE_NAMES.get(var_name, var_name)


def translate_value(value: str, variable: str = None) -> str:
    """
    Traduz valor categórico para português.
    
    Args:
        value: Valor a ser traduzido
        variable: Nome da variável (para traduções específicas)
        
    Returns:
        Valor traduzido
    """
    # Tradução específica por escala
    if variable and variable in VARIABLE_SCALES:
        try:
            numeric_val = int(float(value))
            if numeric_val in VARIABLE_SCALES[variable]:
                return VARIABLE_SCALES[variable][numeric_val]
        except (ValueError, TypeError):
            pass
    
    # Tradução de obesidade
    if str(value) in OBESITY_LABELS:
        return OBESITY_LABELS[str(value)]
    
    # Tradução genérica
    return VALUE_TRANSLATIONS.get(str(value), str(value))


def get_obesity_label(obesity_class: str, with_description: bool = False) -> str:
    """
    Retorna label de obesidade em português.
    
    Args:
        obesity_class: Classe de obesidade em inglês
        with_description: Se True, inclui descrição do IMC
        
    Returns:
        Label traduzido
    """
    label = OBESITY_LABELS.get(obesity_class, obesity_class)
    
    if with_description:
        desc = OBESITY_DESCRIPTIONS.get(obesity_class, '')
        return f"{label} ({desc})"
    
    return label


def get_color_palette(n_colors: int = 7, reverse: bool = False) -> list:
    """
    Retorna paleta de cores padronizada do projeto.
    
    Args:
        n_colors: Número de cores desejadas
        reverse: Se True, inverte a ordem (escuro -> claro)
        
    Returns:
        Lista de cores em hexadecimal
    """
    import matplotlib.cm as cm
    import numpy as np
    
    blues = cm.get_cmap('Blues', 256)
    
    if reverse:
        color_indices = np.linspace(0.95, 0.35, n_colors)
    else:
        color_indices = np.linspace(0.35, 0.95, n_colors)
    
    colors = [blues(idx) for idx in color_indices]
    
    # Converter RGBA para hex
    import matplotlib.colors as mcolors
    return [mcolors.rgb2hex(color[:3]) for color in colors]


# ============================================================================
# INSIGHTS ACADÊMICOS (para uso em textos e dashboards)
# ============================================================================

ACADEMIC_INSIGHTS = {
    'family_history': {
        'finding': 'Histórico familiar é o fator de risco mais forte para obesidade',
        'evidence': '40-70% da variação do IMC é atribuível a fatores genéticos',
        'genes': 'Genes FTO, MC4R e POMC influenciam apetite e metabolismo',
        'reference': 'Locke et al., Nature 2015'
    },
    'FAF': {
        'finding': 'Atividade física regular reduz risco de obesidade em 20-30%',
        'recommendation': 'OMS recomenda ≥150 min/semana de atividade moderada',
        'reference': 'WHO, 2020; Donnelly et al., 2009'
    },
    'FAVC': {
        'finding': 'Alimentos ultraprocessados aumentam ingestão calórica',
        'evidence': 'Consumo de ultraprocessados eleva ingestão em ~500 kcal/dia',
        'reference': 'Harvard T.H. Chan School, 2023'
    },
    'Gender': {
        'finding': 'Diferenças metabólicas e hormonais entre gêneros',
        'evidence': 'Homens e mulheres têm distribuição de gordura diferente',
        'reference': 'Kanter & Caballero, 2012'
    }
}


if __name__ == "__main__":
    # Teste das funções
    print("=== Teste do módulo de traduções ===\n")
    
    print("1. Tradução de variáveis:")
    for var in ['Gender', 'Age', 'BMI', 'FAVC', 'FAF']:
        print(f"  {var:15s} -> {translate_variable(var)}")
    
    print("\n2. Tradução de níveis de obesidade:")
    for obesity in OBESITY_ORDER:
        print(f"  {obesity:25s} -> {get_obesity_label(obesity)}")
    
    print("\n3. Paleta de cores:")
    colors = get_color_palette(7)
    print(f"  {colors}")
    
    print("\n4. Cores do projeto:")
    print(f"  PRIMARY_COLOR   = {PRIMARY_COLOR}")
    print(f"  SECONDARY_COLOR = {SECONDARY_COLOR}")
    print(f"  ACCENT_COLOR    = {ACCENT_COLOR}")
