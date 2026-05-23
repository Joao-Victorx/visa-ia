from fastapi import FastAPI, UploadFile, File
from adapters.gateways.tesseract_ocr_gateway import TesseractOCRGateway
from use_cases.analisar_documento import AnalisarDocumentoUseCase
from frameworks.ia.bert_ia_service import BertIAService  # Import novo

app = FastAPI(title="VISA Londrina IA")

# Inicializa a IA uma vez só (fora da rota) para não lentificar o upload
ia_service = BertIAService()


@app.post("/documentos/analisar")
async def analisar_doc(file: UploadFile = File(...)):
    ocr_gtw = TesseractOCRGateway()

    # Agora passamos o serviço de IA real!
    use_case = AnalisarDocumentoUseCase(ocr_gtw, ia_service=ia_service)

    conteudo_arquivo = await file.read()
    resultado = use_case.executar(conteudo_arquivo, file.filename)

    return resultado
