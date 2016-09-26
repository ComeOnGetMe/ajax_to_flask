from flask import render_template, request, Flask
import json, logging, logging.handlers

logger = logging.getLogger('testlogger')
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s: %(message)s')
handler = logging.handlers.RotatingFileHandler('test.log', maxBytes=262144, backupCount=5)
handler.setFormatter(formatter)
logger.addHandler(handler)

app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def index():
    if request.method == 'POST':
        logger.info(json.dumps(request.form))
    return render_template('index.html')
