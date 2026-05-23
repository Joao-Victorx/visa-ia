import pytesseract
from PIL import Image
import io
from pdf2image import convert_from_bytes
from domain.interfaces.ocr_gateway import OCRGateway

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


class TesseractOCRGateway(OCRGateway):
    def executar_ocr(self, arquivo_bytes: bytes, nome_arquivo: str) -> str:
        texto_completo = ""

        # Verifica se o arquivo é PDF
        if nome_arquivo.lower().endswith(".pdf"):
            # Converte as páginas do PDF em imagens (Precisa do Poppler instalado no Windows)
            paginas = convert_from_bytes(arquivo_bytes)
            for pagina in paginas:
                texto_completo += pytesseract.image_to_string(
                    pagina, lang='por') + "\n"
        else:
            # Se for imagem comum (PNG/JPG)
            imagem = Image.open(io.BytesIO(arquivo_bytes))
            texto_completo = pytesseract.image_to_string(imagem, lang='por')

        return texto_completo
