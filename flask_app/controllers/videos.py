from flask_app import app
from flask import Flask
from flask import render_template, request, redirect, session
from flask_app.models.video import Video, Category

#--creating video/////////////////////////////////////////////////////

@app.route('/')
def input_vid_data():
    return render_template('create_vid.html')

@app.route('/create/vid/', methods=["POST"])
def create_vid_data():
    v_data = {
        'title': request.form['title'],
        'description': request.form['description']
    }
    video = Video.save_vid(v_data)
    if 'video_id' in  session:
        session.pop('video_id')
    session['video_id'] = video
    return redirect('/upload/vid')
# + video_id

@app.route('/upload/vid')
def upload_vid():

    return render_template('upload_vid.html')

ALLOWED_EXTENSIONS = ['.mp4']

def allowed_file(file):
    return '.' in file and file.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['POST'])
def upload():
    if'video' not in request.files:
        return 'No video file found'
    video = request.files['video']
    if video.filename =='':
        return 'No video selected'
#    if video and allowed_file(video.filename):
    video_data = Video.upload_vid({
        'id': session['video_id'],
        'file_name': video.filename
    })
    id = str(session['video_id'])
    session.pop('video_id')
    video.save('flask_app/static/videos/' + id + '.mp4')

#    session['video'] = video.filename
    return redirect('/preview/' + id)
#    return 'invalid video file'

#--updatng video//////////////////////////////////////////////////////

@app.route('/<int:num>')
def update_data(num):
    return render_template('update_data.html')

@app.route('/preview/<int:num>')
def prev(num):

    return render_template('preview.html', video_name = num,)


