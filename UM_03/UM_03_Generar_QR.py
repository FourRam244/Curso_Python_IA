import qrcode

def generar_qr(datos,nombre_archivo):
    qr=qrcode.QRCode(
        version=1,
        error_correction=qrcode.ERROR_CORRECT_L,
        box_size=4,
        border=4
    )
    qr.add_data(datos)
    qr.make(fit=True)

    img=qr.make_image(fill_color="black",back_color="white")
    img.save(nombre_archivo+".png")

datos_para_qr="http://www.python.org"
nombre_archivo="codigo_qr"
generar_qr(datos_para_qr,nombre_archivo)