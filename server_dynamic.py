from flask import Flask, request, render_template_string
import os
import socket

app = Flask(__name__)
upload_folder = 'C:/Users/gwapo/OneDrive/Desktop/TESTING'

if not os.path.exists(upload_folder):
    os.makedirs(upload_folder)

app.config['UPLOAD_FOLDER'] = upload_folder
ip_address_file = 'C:/Users/gwapo/OneDrive/Desktop/TESTING/ip_address.txt'  # Specify the path here

upload_template = """
<!doctype html>
<title>Upload File</title>
<h1>Upload a File</h1>
<form method="post" enctype="multipart/form-data" action="/">
  <input type="file" name="file">
  <input type="submit" value="Upload">
</form>
"""

uploaded_template = """
<!doctype html>
<title>File Uploaded</title>
<h1>File uploaded successfully</h1>
<button onclick="window.location.href='/'">Upload Another File</button>
"""

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'No file part'
        file = request.files['file']
        if file.filename == '':
            return 'No selected file'
        if file:
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
            return render_template_string(uploaded_template)
    return render_template_string(upload_template)

def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.254.254.254', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

def save_ip_address(ip_address):
    with open(ip_address_file, 'w') as file:
        file.write(ip_address)

if __name__ == '__main__':
    ip_address = get_ip_address()
    full_address = f"{ip_address}:5000"
    save_ip_address(full_address)
    print(f"Server running on http://{full_address}/")
    app.run(host='0.0.0.0', port=5000)
