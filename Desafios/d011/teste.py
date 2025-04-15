import pandas as pd

# Dados
parcelamentos = [6, 12, 18, 24, 36]
custos_totais = [5090.40, 5242.32, 5396.16, 5555.04, 5876.16]
acrescimo_percentual = [3.53, 6.62, 9.75, 12.98, 19.50]

# Cálculos de acréscimo entre as opções
acrescimo_entre_opcoes = [0, 2.98, 2.93, 2.95, 5.77]  # O acréscimo entre a 1ª opção e a 2ª é 2.98%, etc.

# Criando o DataFrame
df = pd.DataFrame({
    'Parcelamento (meses)': parcelamentos,
    'Custo Total (R$)': custos_totais,
    'Acréscimo Total (%)': acrescimo_percentual,
    'Acréscimo Entre Opções (%)': acrescimo_entre_opcoes
})

# Salvando a planilha
file_path = 'C:/Users/p001557/Desktop/Gustavo/parcelamento_comparacao.xlsx'
df.to_excel(file_path, index=False)

file_path
