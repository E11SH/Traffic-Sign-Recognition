import os
import time
from flask import Flask, request, render_template, jsonify, url_for
from werkzeug.utils import secure_filename

# Import model and processing functions
from model_loader import model, label_map
from video_processor import process_video

#Flask App Initialization
app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'C:/Users/mhesh/Desktop/traffic-sign-recognition/static/uploads/'
app.config['PROCESSED_FOLDER'] = 'C:/Users/mhesh/Desktop/traffic-sign-recognition/static/processed_videos/'
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024  # 50 MB upload limit

#Ensure Directories Exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['PROCESSED_FOLDER'], exist_ok=True)


# Routes
@app.route('/')
def index():
    """Renders the main page."""
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    """Handles video upload and processing."""
    if 'videoFile' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['videoFile']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file:
        filename = secure_filename(file.filename)
        unique_filename = f"{int(time.time())}_{filename}"

        input_path = os.path.join(app.config['UPLOAD_FOLDER'], unique_filename)
        output_path = os.path.join(app.config['PROCESSED_FOLDER'], unique_filename)

        file.save(input_path)

        # Process the video
        try:
            process_video(input_path, output_path, model, label_map)
            video_url = url_for('static', filename=f'processed_videos/{unique_filename}')

            return jsonify({'processed_video_url': video_url})
        except Exception as e:
            return jsonify({'error': f'An error occurred during processing: {str(e)}'}), 500

    return jsonify({'error': 'File type not allowed'}), 400


if __name__ == '__main__':
    app.run(debug=True)