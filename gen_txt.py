#!./marxgpt-env/bin/python

import os
import subprocess

os.system("rm -rf ./txtgen/*")

def converter_epub_para_txt(pasta_epub, pasta_txt):
    # Verifica se a pasta de destino existe, se não, a cria
    if not os.path.exists(pasta_txt):
        os.makedirs(pasta_txt)

    # Lista todos os arquivos na pasta_epub
    for arquivo in os.listdir(pasta_epub):
        if arquivo.endswith('.epub'):
            caminho_epub = os.path.join(pasta_epub, arquivo)
            nome_arquivo_txt = os.path.splitext(arquivo)[0] + '.txt'
            caminho_txt = os.path.join(pasta_txt, nome_arquivo_txt)

            # Chama o comando ebook-convert para converter o arquivo ePub em TXT
            subprocess.run(['ebook-convert', caminho_epub, caminho_txt])

def juntar_txt(pasta_txt, arquivo_saida):
    # Abre o arquivo de saída em modo de escrita
    with open(arquivo_saida, 'w') as outfile:
        # Lista todos os arquivos na pasta_txt
        for arquivo in os.listdir(pasta_txt):
            if arquivo.endswith('.txt'):
                caminho_txt = os.path.join(pasta_txt, arquivo)
                # Lê o conteúdo do arquivo .txt e escreve no arquivo de saída
                with open(caminho_txt, 'r') as infile:
                    outfile.write(infile.read())

# Pasta onde estão os arquivos ePub
pasta_epub = './original/epub/'
# Pasta onde os arquivos TXT serão salvos
pasta_txt = './txtgen/'
# Nome do arquivo de saída
arquivo_saida = './txtgen/all.txt'

converter_epub_para_txt(pasta_epub, pasta_txt)
juntar_txt(pasta_txt, arquivo_saida)
