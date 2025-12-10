from flask import Flask, request, send_file
from PIL import Image
import pyheif
import io

app = Flask(__name__)

@app.route('/convert-heic-to-jpg', methods=['POST'])
def convert_heic_to_jpg():
    if 'file' not in request.files:
        return "No file part", 400
    file = request.files['file']
    if file.filename == '':
        return "No selected file", 400
    if file and file.filename.lower().endswith('.heic'):
        try:
            heif_file = pyheif.read(file.stream)
            image = Image.frombytes(
                heif_file.mode, 
                heif_file.size, 
                heif_file.data,
                "raw",
                heif_file.mode,
                heif_file.stride,
            )
            output_buffer = io.BytesIO()
            image.save(output_buffer, format="JPEG")
            output_buffer.seek(0)
            return send_file(output_buffer, mimetype='image/jpeg', as_attachment=True, download_name='converted.jpg')
        except Exception as e:
            return f"Error converting file: {e}", 500
    return "Invalid file format", 400

@app.route('/health', methods=['GET'])
def health_check():
    return "OK", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)