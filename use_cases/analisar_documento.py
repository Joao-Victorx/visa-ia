from domain.entities.documento import Documento
from domain.interfaces.ocr_gateway import OCRGateway
from datetime import datetime


class AnalisarDocumentoUseCase:
    def __init__(self, ocr_gateway, ia_service):
        self.ocr_gateway = ocr_gateway
        self.ia_service = ia_service

    def executar(self, arquivo_bytes: bytes, nome_arquivo: str):
        # Agora o gateway recebe os bytes E o nome para saber se é PDF
        texto = self.ocr_gateway.executar_ocr(arquivo_bytes, nome_arquivo)

        # Chama a IA para analisar o texto extraído
        resultado_ia = self.ia_service.analisar_conformidade(texto)

        return {
            "texto": texto,
            "status": "Divergente" if resultado_ia["score"] < 0.7 else "Conforme",
            "analise_detalhada": resultado_ia
        }
