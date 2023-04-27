from flask_app import app
from flask import Flask
from flask import render_template, request, redirect, session
from flask_app.models.video import Video, Category
from flask_app.models.comment import Comment
import os

#--creating video/////////////////////////////////////////////////////

@app.route('/new/vid')
def input_vid_data():
    return render_template('create_vid.html')

@app.route('/create/vid/', methods=["POST"])
def create_vid_data():
    print(session['user_id'])
    v_data = {
        'title': request.form['title'],
        'description': request.form['description'],
        'user_id': session['user_id']
    }
    video = Video.save_vid(v_data)
    if 'video_id' in  session:
        session.pop('video_id')
    session['video_id'] = video
    c_data = {
        'boats': request.form['boats'],
        'bushcraft': request.form['bushcraft'],
        'cabinetry': str(request.form['cabinetry']),
        'carpentry': request.form['carpentry'],
        'cars': request.form['cars'],
        'electronics': request.form['electronics'],
        'home_electricity': request.form['home_electricity'],
        'hvac': request.form['hvac'],
        'machining': request.form['machining'],
        'motorcycles': request.form['motorcycles'],
        'planes': request.form['planes'],
        'plumbing': request.form['plumbing'],
        'roofing': request.form['roofing'],
        'tractors': request.form['tractors'],
        'welding': request.form['welding'],
        'wood_working': request.form['wood_working'],
        'printing': request.form['printing'],
        'video_id': session['video_id']
    }
    Category.create_category(c_data)
    return redirect('/new/vid')
# + video_id

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
    id = str(session['video_id'])
    session.pop('video_id')
    
    video.save('flask_app/static/videos/' + id + '.mp4')
    Video.make_thumbnail({'id':id})
#    session['video'] = video.filename
    return redirect('/video/' + id)
#    return 'invalid video file'

#--updating video//////////////////////////////////////////////////////

@app.route('/update/vdata/<int:num>')
def update_d(num):

    return render_template('update_vid.html', id = num)

@app.route('/update/data/<int:num>', methods=['POST'])
def update_data(num):
    data = {
        'id': num,
        'title': request.form['title'],
        'description': request.form['description'],
    }
    session['video_id'] = Video.update_vid(data)
    video = str(num)

    return redirect('/update/vdata/'+ video)

@app.route('/update/<int:num>', methods=['POST'])
def update_vid(num):
    session.pop('video_id')
    if'video' not in request.files:
        return 'No video file found'
    video = request.files['video']
    if video.filename =='':
        return 'No video selected'
#    if video and allowed_file(video.filename):
    id = str(num)
    os.remove('flask_app/static/videos/' + id + '.mp4')
    video.save('flask_app/static/videos/' + id + '.mp4')
    Video.make_thumbnail({'id':str(num)})
    return redirect('/video/' + id)

#--delete//////////////////////////////////////////////////

@app.route('/delete/<int:id>')
def delete_vid(id):
    Video.delete({'id':id})
    return redirect ('/dashboard')

#--display videos/////////////////////////////////////////////////////


@app.route('/video/<int:num>')
def prev(num):

    return render_template('preview.html', video = Video.get_by_id({'id':num}), comments = Comment.get_all({'id':num}), video_links = Video.get_all())

@app.route('/dashboard')
def dash():
    if 'video_id' in  session:
        session.pop('video_id')
    return render_template('dashboard.html', videos = Video.get_all())

@app.route('/categories/<string:cat>')
def category_search(cat):
    if cat == 'boats':
        video = Video.get_v_boats()
    if cat == 'bushcraft':
        video = Video.get_v_bushcraft()
    if cat == 'cabinetry':
        video = Video.get_v_cabinetry()
    if cat == 'cars':
        video = Video.get_v_cars()
    if cat == 'carpentry':
        video = Video.get_v_carpentry()
    if cat == 'electronics':
        video = Video.get_v_electronics()
    if cat == 'home_electricity':
        video = Video.get_v_he()
    if cat == 'hvac':
        video = Video.get_v_hvac()
    if cat == 'machining':
        video = Video.get_v_machining()
    if cat == 'motorcycles':
        video = Video.get_v_motorcycles()
    if cat == 'planes':
        video = Video.get_v_planes()
    if cat =='plumbing':
        video = Video.get_v_plumbing()
    if cat == 'roofing':
        video = Video.get_v_roofing()
    if cat == 'tractors':
        video = Video.get_v_tractors()
    if cat == 'welding':
        video = Video.get_v_welding()
    if cat == 'wood_working':
        video = Video.get_v_ww()
    if cat == 'printing':
        video = Video.get_v_3dp()

    return render_template('category.html', videos = video)
