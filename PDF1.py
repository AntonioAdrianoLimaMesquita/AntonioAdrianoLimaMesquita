# importar a biblioteca PyPDF2
import PyPDF2 as pdf

# importar a biblioteca tkinter
from tkinter import filedialog, Tk, simpledialog, messagebox

# importar a biblioteca os
import os

 

# inicializar o marger
mesclar = pdf.PdfMerger(strict=False)

# Criar uma janela de aplicativo vazia
diretorio =Tk()

diretorio.withdraw()

messagebox.showinfo("Mescla de PDF do Antonio", "Certifique-se que na pasta de origem há arquivos no formato PDF."
                    "\n 1 - Selecione a pasta de origem."
                    "\n 2 - Selecione a pasta de destino."
                    "\n 3 - Informe o nome do novo arquivo.")

pasta_origem = filedialog.askdirectory(title=f'Selecione a pasta com os arquivos PDFs')

#arquivos = os.listdir('C:/Users/antomes/Documents/BAT/Mescla_PDF')

nova_pasta = filedialog.askdirectory(title=f'Selecione onde será salvo o novo Arquivo PDF')

nova_pasta +="/"

 

if not pasta_origem:

    messagebox.showerror("Erro", "Nenhum diretório selecionado. Encerrando o programa.")

else:

     # Listar arquivos na pasta de origem

    arquivos = os.listdir(pasta_origem)

    #faz o for dentro da pasta

    #selecionado somente os arquivos que são em formato PDF

    for arquivo in arquivos:

        if arquivo.lower().endswith('.pdf'):

            # incrementa os PDF´s em um unico dicionario

            mesclar.append(os.path.join(pasta_origem, arquivo))

            #mesclar.append(f'C:/Users/antomes/Documents/BAT/Mescla_PDF/{arquivo}')

 

    # Carrega o nome do novo arquivo gerado

    nome_arquivo_mesclado = simpledialog.askstring("Nome do Arquivo", "Digite o nome do arquivo PDF mesclado:")

 

    # Acrescenta a extensão ".pdf" ao nome do arquivo

    if nome_arquivo_mesclado:

        nome_arquivo_mesclado += ".pdf"

 

        #Gera o arquivo final do PDF Mesclado

        mesclar.write(nova_pasta + nome_arquivo_mesclado)

        #mesclar.write('C:/Users/antomes/Documents/BAT/Mescla_PDF/PDF_Mesclado_final.pdf')

 

        messagebox.showinfo("Sucesso!", f'Arquivos mesclados com sucesso! O arquivo {nome_arquivo_mesclado} foi criado.')

 

        mesclar.close()

    else:

        messagebox.showerror("Erro", f'Nenhum nome de arquivo fornecido. Encerrando o programa.')

       

        mesclar.close()