from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
#from flask_app.models import user, business

class Comment:
    db = 'group_project'
    def __init__(self,data):
        self.id = data['id']
        self.comment = data['title']
        self.comment_id = data['description']
        self.video_id = data['file_name']
        self.user_id = data['file_name']
        self.updated_at = data['updated_at']
        self.created_at = data['created_at']
        self.creator = None
        
    @classmethod
    def create_comment(cls,data):
        query = "INSERT INTO comments ( comment, comment_id, video_id, user_id, created_at, updated_at ) VALUES ( %(comment)s, %(comment_id)s, %(video_id)s, %(user_id)s, NOW(), NOW());"
        return connectToMySQL(Comment.db).query_db(query,data)
    

    
    #i in  comments will pull the  value from list of coments
    #loop through the rest of the comments to check if any of their id maches the i's comment id
    #you might have to stop at 2, thats sufficient