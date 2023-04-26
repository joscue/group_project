from flask_app import app
from flask import Flask
from flask import render_template, request, redirect, session
from flask_app.models.comment import Comment

@app.route('/start/comment/<int:id>/<int:cid>')
def start_comment(id,cid):
    video = str(id)
    session['comment_id'] = cid
    return redirect('/video/' + video)

@app.route('/create/comment/<int:id>', methods=['POST'])
def create_comment(id):
    data = {
        'comment': request.form['comment'],
        'comment_id': int(request.form['comment_id']),
        'video_id': id,
#        'user_id': session['user_id']
    }
    Comment.create_comment(data)
    video = str(id)
    session.pop('comment_id')
    return redirect('/video/' + video)

