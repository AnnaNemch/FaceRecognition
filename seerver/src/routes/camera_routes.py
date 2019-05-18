from app import app

@app.route('/api/collect-data')
def handle_collect_data():
    return 'Collect data'

@app.route('/api/train')
def handle_train_data():
    return 'Training data'

@app.route('/api/recognize')
def handle_recognize_mode():
    return 'Recognize'

@app.route('/api/camera')
def get_camera_stream():
    return 'Camera stream'
