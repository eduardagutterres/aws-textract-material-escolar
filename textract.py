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
