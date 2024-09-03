from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/image-editing')
def image_editing():
    return render_template('image_editing.html')

@app.route('/animation')
def animation():
    return render_template('animation.html')

@app.route('/audio-processing')
def audio_processing():
    return render_template('audio_processing.html')

@app.route('/text-generation')
def text_generation():
    return render_template('text_generation.html')

if __name__ == '__main__':
    app.run(debug=True)
