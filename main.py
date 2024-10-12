from flask import Flask, render_template, request, send_file
from PIL import Image, ImageDraw, ImageFont
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

def add_watermark(input_image_path, output_image_path, text, font_path, font_size, opacity, color, spacing, angle):
    # Ouvre l'image
    image = Image.open(input_image_path).convert("RGBA")
    txt_layer = Image.new("RGBA", image.size, (255, 255, 255, 0))
    font = ImageFont.truetype(font_path, font_size)
    draw = ImageDraw.Draw(txt_layer)
    width, height = image.size
    text_bbox = font.getbbox(text)
    text_width, text_height = text_bbox[2] - text_bbox[0], text_bbox[3] - text_bbox[1]

    for y in range(0, height, text_height + spacing):
        for x in range(0, width, text_width + spacing):
            text_img = Image.new("RGBA", (text_width, text_height), (255, 255, 255, 0))
            text_draw = ImageDraw.Draw(text_img)
            text_draw.text((0, 0), text, font=font, fill=color + (opacity,))
            rotated_text = text_img.rotate(angle, expand=1)
            txt_layer.paste(rotated_text, (x, y), rotated_text)

    watermarked_image = Image.alpha_composite(image, txt_layer)
    watermarked_image = watermarked_image.convert("RGB")
    watermarked_image.save(output_image_path)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        input_image = request.files['input_image']
        text = request.form.get('text', 'trhacknon')
        font_size = int(request.form.get('font_size', 20))
        opacity = int(request.form.get('opacity', 75))
        color = request.form.get('color', '255,0,0')
        spacing = int(request.form.get('spacing', 30))
        angle = int(request.form.get('angle', 45))

        # Save the uploaded image
        input_image_path = os.path.join(app.config['UPLOAD_FOLDER'], input_image.filename)
        input_image.save(input_image_path)

        # Convert the color string to a tuple of integers
        color_tuple = tuple(map(int, color.split(',')))

        output_image_path = os.path.join(app.config['UPLOAD_FOLDER'], 'watermarked_' + input_image.filename)
        add_watermark(input_image_path, output_image_path, text, 'Arial.ttf', font_size, opacity, color_tuple, spacing, angle)

        return send_file(output_image_path, as_attachment=True)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=False,  host='0.0.0.0', port=5000)
