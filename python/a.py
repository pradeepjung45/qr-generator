import qrcode
from PIL import Image


def generate_qr_code(data, output_file):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=1,
    )

    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color='black', back_color='white')

    img.save(output_file)
    print(f"The output is {output_file}")


def main():
    input_image_path = 'input_image.jpg'
    output_qr_code_path = 'output_qr_code.jpg'

    try:
        img = Image.open(input_image_path)
        img.show()
    except IOError:
        print(f"Cannot open image file {input_image_path}")

    generate_qr_code(input_image_path, output_qr_code_path)


if __name__ == "__main__":
    main()
