import os

from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import whisper
from flask_cors import CORS

app = Flask(__name__)
UPLOAD_FOLDER = "content/"
ALLOWED_AUDIO_EXTENSIONS = set(["mp3", "wav", "ogg"])  # Разрешенные расширения для аудиофайлов
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024 * 1024
CORS(app)
model = whisper.load_model("base")


def allowed_file(filename):
    allowed_extensions = set(["mp4", "mov", "avi", "mkv", "wmv", "flv"])
    return "." in filename and filename.rsplit(".", 1)[1].lower() in allowed_extensions

def allowed_audio_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_AUDIO_EXTENSIONS

@app.route('/test', methods=['GET'])
def test():
    return jsonify({"status": 200}), 200

@app.route("/upload-video", methods=["POST"])
def upload_video():
    if "video" not in request.files:
            return jsonify({"message": "Видео не было загружено"}), 400

    video = request.files["video"]

    if video.filename == "":
        return jsonify({"message": "Пожалуйста, выберите видео файл"}), 400

    if video and allowed_file(video.filename):
        filename = secure_filename(video.filename)
        video_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
        video.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
        if os.path.exists(video_path):
            result = model.transcribe(video_path)
            return jsonify({"message": "Видео успешно загружено", "filename": filename, "result": result['segments']}), 200
        return jsonify({"message": "Видео успешно загружено", "filename": filename, "result": "null"}), 200

    return jsonify({"message": "Неправильный формат видео файла"}), 400

@app.route("/upload-audio", methods=["POST"])
def upload_audio():
    if "audio" not in request.files:
        return jsonify({"message": "Аудио не было загружено"}), 400

    audio = request.files["audio"]

    if audio.filename == "":
        return jsonify({"message": "Пожалуйста, выберите аудио файл"}), 400

    if audio and allowed_audio_file(audio.filename):
        filename = secure_filename(audio.filename)
        audio_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
        audio.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
        if os.path.exists(audio_path):
            result = model.transcribe(audio_path)
            return jsonify({"message": "Аудио успешно загружено", "filename": filename, "result": result['segments']}), 200
        return jsonify({"message": "Аудио успешно загружено", "filename": filename, "result": "null"}), 200

    return jsonify({"message": "Неправильный формат аудио файла"}), 400

if __name__ == "__main__":
    os.makedirs("content", exist_ok=True)
    app.run(debug=True)
