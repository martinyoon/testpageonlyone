from flask import Flask, render_template, send_file

app = Flask(__name__)

@app.route('/')
def show_image():
    return render_template('image.html')

@app.route('/get_image')
def get_image():
    filename = 'templates/assets/img/image001.jpg'
    return send_file(filename, mimetype='image/jpg')

if __name__ == '__main__':
    app.run(debug=False)
