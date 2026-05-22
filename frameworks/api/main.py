from fastapi import FastAPI, UploadFile, File
# Ajuste as importações para o local correto das suas pastas na raiz:
from adapters.gateways.tesseract_ocr_gateway import TesseractOCRGateway
from use_cases.analisar_documento import AnalisarDocumentoUseCase

app = FastAPI(title="VISA Londrina IA")


@app.post("/documentos/analisar")
async def analisar_doc(file: UploadFile = File(...)):
    # Inicializa o motor de OCR
    ocr_gtw = TesseractOCRGateway()

    # Inicializa o caso de uso (Passando None na IA por enquanto)
    use_case = AnalisarDocumentoUseCase(ocr_gtw, ia_service=None)

    conteudo_arquivo = await file.read()
    resultado = use_case.executar(conteudo_arquivo, file.filename)

    return resultado
