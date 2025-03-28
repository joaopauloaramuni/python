import qrcode
from PIL import Image

class QRCodeLogic:
    def __init__(self):
        self.qr_image = None

    def generate_qr(self, data, fill_color="black", back_color="white", box_size=10, image_path=None):
        try:
            # Criar QR Code básico
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_H,
                box_size=box_size,
                border=4,
            )
            qr.add_data(data)
            qr.make(fit=True)

            # Gerar imagem com cores personalizadas
            qr_img = qr.make_image(fill_color=fill_color, back_color=back_color)

            # Adicionar imagem central se fornecida
            if image_path:
                logo = Image.open(image_path)
                qr_width, qr_height = qr_img.size
                logo_size = qr_width // 4  # 25% do tamanho do QR
                
                # Redimensionar logo
                logo = logo.resize((logo_size, logo_size), Image.Resampling.LANCZOS)
                
                # Calcular posição central
                pos = ((qr_width - logo_size) // 2, (qr_height - logo_size) // 2)
                
                # Converter para modo compatível
                qr_img = qr_img.convert('RGBA')
                logo = logo.convert('RGBA')
                
                # Colocar logo no QR Code
                qr_img.paste(logo, pos, logo)

            self.qr_image = qr_img
            return qr_img

        except Exception as e:
            raise Exception(f"Erro ao gerar QR Code: {str(e)}")

    def save_qr(self, file_path):
        if self.qr_image:
            self.qr_image.save(file_path)
            return True
        return False
