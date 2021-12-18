import os
import shutil
from flask import Flask, render_template, request
from separate import separate
from transfer import transfer

app = Flask(__name__)

@app.route('/')
def upload_file():
    return render_template('upload.html')


@app.route('/result', methods=['GET', 'POST'])
def result():
    if request.method == 'POST':
        f = request.files['file']
        in_channel = request.form['channel']
        out_tone = request.form['tone']
        f.save(f.filename)
        separate(f.filename, ".")
        fn, ext = os.path.splitext(f.filename)
        inp_file = f"mdx_extra/{fn}/{in_channel}.{ext}"
        out_file = f"static/{f.filename}_{in_channel}_{out_tone}.{ext}"
        print(inp_file, out_file)
        transfer(inp_file, out_tone, "static/")
        os.remove(f.filename)
        shutil.rmtree("mdx_extra")
        return 'file uploaded successfully'
    else:
        return render_template('upload.html')


if __name__ == '__main__':
    app.run(debug=True)
