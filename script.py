import os

from PyPDF2 import PdfMerger, PdfReader
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

raiz_do_projeto = "C:/Users/gamer/Desktop/Programas/front-end/trabalho/"

def formatar_caminho(caminho_completo):
    length = len(raiz_do_projeto)
    return caminho_completo[length:]

def cortar_string(string, tamanho):
    pedacos = []
    for i in range(0, len(string), tamanho):
        pedaco = string[i:i + tamanho]
        pedacos.append(pedaco)
    return pedacos

def criar_pdf_arquivo(nome_arquivo_pdf, lista_de_arquivos):
    total_arquivos = len(lista_de_arquivos)
    count = 0

    merger = PdfMerger()
    c = canvas.Canvas(nome_arquivo_pdf, pagesize=letter)
    for arquivo in lista_de_arquivos:
        try:
            with open(arquivo, 'r', encoding='UTF-8', ) as file:
                conteudo = file.read()

            caminho_formatado = formatar_caminho(arquivo)
            c.drawString(50, 750, f"Arquivo: {caminho_formatado}")

            x, y = 50, 720  # Posição inicial
            largura_maxima = 550

            for linha in conteudo.split('\n'):
                largura_linha = c.stringWidth(linha)
                if x + largura_linha >= largura_maxima:
                    textos_cortados = cortar_string(linha, 80)
                    for texto_cortado in textos_cortados:
                        x = 50
                        c.drawString(x, y, texto_cortado)
                        y -= 15
                        if(y <= 10):
                            c.showPage()
                            y = 750
                        
                    continue

                c.drawString(x, y, linha)
                y -= 15 
                
                if (y <= 10):
                    c.showPage()
                    y = 750  
            c.showPage()   
        except Exception as e:
            print("Erro ao ler o arquivo: " + arquivo) 
            print (e)
        count += 1
        print(f"Arquivo {count} de {total_arquivos} processados!")
    c.save()
    merger.append(nome_arquivo_pdf)
    merger.write(nome_arquivo_pdf)
    merger.close()
    print("PDF criado com sucesso!")

def criar_pdf_pasta(nome_pasta, nome_arquivo_pdf):
    lista_de_arquivos = []
    count = 0
    for pasta_raiz, _, arquivos in os.walk(nome_pasta):
        for arquivo in arquivos:
            caminho_completo = os.path.join(pasta_raiz, arquivo)
            lista_de_arquivos.append(caminho_completo)
            count += 1
    if(count == 0):
        print("Nenhum arquivo encontrado ou pasta vazia!")
        return        

    criar_pdf_arquivo(nome_arquivo_pdf, lista_de_arquivos)


def combinar_pdfs(lista_de_pdfs, nome_arquivo_final):
    total_arquivos = len(lista_de_pdfs)
    count = 0
    merger = PdfMerger()
    
    for pdf in lista_de_pdfs:
        merger.append(pdf)
        count += 1
        print(f"PDF {count} de {total_arquivos} compactados, para o PDF final!")

    merger.write(nome_arquivo_final)
    merger.close()    

pasta_do_projeto = "C:\\Users\\gamer\\Desktop\\Programas\\front-end\\trabalho\\fretex\\backend"
nome_do_arquivo = 'projetoBack.pdf'


criar_pdf_pasta(pasta_do_projeto, nome_do_arquivo)

#combinar_pdfs(['projetoBack.pdf', 'projetoFront.pdf'], 'projeto_final.pdf') - função para combinar os pdfs que estão na lista e na mesma pasta do script.py
