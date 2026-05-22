import pytesseract
from PIL import Image
import io
from domain.interfaces.ocr_gateway import OCRGateway

class TesseractOCRGateway(OCRGateway):
    def executar_ocr(self, arquivo_bytes: bytes) -> str:
        # Converte bytes em imagem para o Tesseract ler
        imagem = Image.open(io.BytesIO(arquivo_bytes))
        texto = pytesseract.image_to_string(imagem, lang='por')
        return texto