# Trabalhando com arquivos binários
with open('dados/imagem.png', 'rb') as f:
    dados = f.read()  # Lê todo o conteúdo binário
print(dados)