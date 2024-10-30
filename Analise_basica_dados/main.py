import pandas as pd

#ler o arquivo CSV com os dados de vendas
df = pd.read_csv('vendas.csv')

# Calcular o total de vendas por produto
total_vendas = df.groupby('produto')['valor_venda'].sum().round(2)

# Caucular a media de vendas por produto
media_vendas = df.groupby('produto')['valor_venda'].mean().round(2)

# Exibir os resultados
print('O valor de vendas foi de:')
print(total_vendas)
print("\nMédia de vendas por produto:")
print(media_vendas)
