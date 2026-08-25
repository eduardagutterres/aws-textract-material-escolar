## AWS Textract - Lista de Material Escolar

Projeto desenvolvido durante o curso da Nublify na DIO para praticar a extração de texto de imagens utilizando o Amazon Textract.

## Objetivo

O objetivo foi utilizar uma imagem com uma lista de material escolar e extrair automaticamente o texto dela com o Amazon Textract.

## Como foi feito

Primeiro, testei a imagem diretamente no console da AWS para verificar se o Textract reconhecia corretamente os textos.

Depois, configurei a AWS CLI e utilizei Python com a biblioteca boto3 para enviar a imagem ao Textract e retornar as linhas de texto identificadas.

## Código utilizado

```python
import boto3

client = boto3.client("textract", region_name="us-east-1")

with open("lista-material-escolar.jpeg", "rb") as arquivo:
    imagem = arquivo.read()

resposta = client.detect_document_text(
    Document={
        "Bytes": imagem
    }
)

for bloco in resposta["Blocks"]:
    if bloco["BlockType"] == "LINE":
        print(bloco["Text"])

```
## Resultado

O Textract conseguiu reconhecer os itens e as quantidades presentes na lista de material escolar.

## Aprendizados

Com este projeto, pratiquei:

* uso do Amazon Textract;
* configuração da AWS CLI;
* uso da biblioteca boto3;
* integração entre Python e AWS;
* extração de texto a partir de imagens.

## Possibilidades

Esse mesmo processo pode ser utilizado para outros tipos de documentos, como listas, recibos, formulários e outros arquivos que contenham texto.

## Prints do projeto

### Teste no Amazon Textract
<img width="1131" height="634" alt="Captura de Tela 2026-08-24 às 22 40 00" src="https://github.com/user-attachments/assets/5a26bb6d-1448-42e5-a053-7c34fd6ed655" />

### Resultado no Terminal
<img width="493" height="225" alt="Captura de Tela 2026-08-24 às 22 47 48" src="https://github.com/user-attachments/assets/55f7a295-ddc4-4836-9a62-45b3d44b0ec2" />



