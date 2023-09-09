# gerador-de-pdf-de-projetos

Nesse projeto você poderá tanto gerar quanto combinar PDFs

- Você poderá gerar PDFs dos seus projetos com a função (criar_pdf_pasta), mas caso haja arquivos que a padrão UTF-8 não possa decodificar o script irá apenas ignorar eles
- Você também poderá combinar PDFs com a função (combinar_pdfs), basta que os PDFs estejam na mesma pasta que o script e sejam passados no parâmetro da função

Requisitos para rodar e passo a passo:
- Você deve possuir python na sua máquina ou na máquina virtual (venv)
- Deve rodar o comando "pip install -r requirements.txt" para instalar as dependências
- Preencher as variáveis "pasta_do_projeto", "nome_do_arquivo", "raiz_do_projeto" e executar
