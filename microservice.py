from flask import Flask, render_template,request
from werkzeug.utils import secure_filename
from tesseract import characterization
from multiprocessing import Pool
from dictCrawl import searchWord

app_port = 22222
app = Flask(__name__)


@app.route('/')
def render_file():
    return render_template('upload.html')


@app.route('/getImage', methods=['GET','POST'])
def default():
    #start_time = time.time()
    if request.method=='POST':
        f=request.files['file']
        filePath='upload/'+secure_filename(f.filename)
        f.save(filePath)

        str= searchWord(characterization(filePath,"eng"))
        #print("--- %s seconds ---" % (time.time() - start_time))
        return str


if __name__ == '__main__':
    pool = Pool(processes=8)
    pool.map(app.run(host='0.0.0.0',port=app_port,debug=True))
    #app.run(host='0.0.0.0', port=app_port, debug=True)