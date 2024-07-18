from flask import Flask, request, redirect, url_for, render_template_string
import os
import qrcode

app = Flask(__name__)
upload_folder = 'C:/Users/gwapo/OneDrive/Desktop/TESTING'
if not os.path.exists(upload_folder):
    os.makedirs(upload_folder)

app.config['UPLOAD_FOLDER'] = upload_folder

html_template = """
<!doctype html>
<title>Upload File</title>
<h1>Upload a File</h1>
<form method=post enctype=multipart/form-data>
  <input type=file name=file>
  <input type=submit value=Upload>
</form>
"""

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
            return 'File uploaded successfully'
    return render_template_string(html_template)

def generate_qr_code(url, filename='qrcode.png'):
    img = qrcode.make(url)
    img.save(filename)

if __name__ == '__main__':
    url = 'http://192.168.100.10:5000/'  # Replace with your IP address
    generate_qr_code(url)
    app.run(host='0.0.0.0', port=5000)
