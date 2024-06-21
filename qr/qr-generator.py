import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.colormasks import RadialGradiantColorMask
from qrcode.image.styles.moduledrawers import CircleModuleDrawer

#dir
imagenlogo = ''

qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
qr.add_data('')

img_2 = qr.make_image(image_factory=StyledPilImage, color_mask=RadialGradiantColorMask(center_color=(227, 23, 10), edge_color=(13, 27, 30)), module_drawer=CircleModuleDrawer(), embeded_image_path=imagenlogo)

#dir
img_2.save('')