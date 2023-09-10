from flask import Flask, request, render_template
import whisper
from flask_lt import run_with_lt
import time


app = Flask(__name__)
run_with_lt(app)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    global model
    file_name = str(int(time.time()))
    audio_file = request.files['file'].save(file_name+'_audio.wav')
    result = model.transcribe(file_name+'_audio.wav')

    text = result["text"]
    with open(file_name+'.txt','a+') as f:
      f.write(text)
    return render_template('result.html', text=text)


model = whisper.load_model("medium")

if __name__ == '__main__':
    app.run()
