import pytesseract
from PIL import Image
import io
import fitz  # Biblioteca PyMuPDF
from domain.interfaces.ocr_gateway import OCRGateway

# Caminho do motor Tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

class TesseractOCRGateway(OCRGateway):
    def executar_ocr(self, arquivo_bytes: bytes, nome_arquivo: str) -> str:
        texto_completo = ""

        # SE FOR PDF: Transforma cada página em imagem e lê o texto
        if nome_arquivo.lower().endswith(".pdf"):
            # Abre o PDF a partir dos bytes
            doc = fitz.open(stream=arquivo_bytes, filetype="pdf")
            for pagina in doc:
                # Transforma a página do PDF em uma imagem (pixmap)
                pix = pagina.get_pixmap()
                img = Image.frombytes(
                    "RGB", [pix.width, pix.height], pix.samples)

                # Roda o OCR na imagem da página
                texto_completo += pytesseract.image_to_string(
                    img, lang='por') + "\n"
            doc.close()

        # SE FOR IMAGEM (PNG/JPG): Lê direto
        else:
            imagem = Image.open(io.BytesIO(arquivo_bytes))
            texto_completo = pytesseract.image_to_string(imagem, lang='por')

        return texto_completo
