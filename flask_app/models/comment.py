from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
#from flask_app.models import user, business

class Comment:
    db = 'group_project'
    def __init__(self,data):
        self.id = data['id']
        self.comment = data['comment']
        self.comment_id = data['comment_id']
        self.video_id = data['video_id']
#        self.user_id = data['user_id']
        self.updated_at = data['updated_at']
        self.created_at = data['created_at']
        self.creator = None
        self.sub = None
        
    @classmethod
    def create_comment(cls,data):
        query = "INSERT INTO comments ( comment, comment_id, video_id, created_at, updated_at ) VALUES ( %(comment)s, %(comment_id)s, %(video_id)s, NOW(), NOW());"
        return connectToMySQL(Comment.db).query_db(query,data)
    #, user_id, %(user_id)s

    @classmethod
    def get_all(cls,data):
        query = "SELECT * FROM comments WHERE video_id = %(id)s;"
        results = connectToMySQL(Comment.db).query_db(query,data)
        comments = []
        for comment in results:
            comments.append( cls(comment) )
        for comment in comments:
            comment.sub = []
            c=0
            while c <= (len(comments)-1):
                if comment.id == comments[c].comment_id:
                    comment.sub.append(comments[c])
                    comments.pop(c)
                else:
                    c = c + 1 
        return comments
    
    @classmethod
    def get_comments(cls,data):
        query = """
                SELECT * FROM videos
                JOIN categories on videos.category_id = categories.id
                WHERE categories.%(category)s = 'true';
                """
        results = connectToMySQL(cls.db).query_db(query,data)
        jobs =[]
        for row in results:
            this_job = cls(row)
            user_data = {
                    "id": row['id'],
                    "first_name": row['first_name'],
                    "last_name": row['last_name'],
                    "email": "",
                    "birthday": "",
                    "password": "",
                    "created_at": row['created_at'],
                    "updated_at": row['updated_at']
            }
            this_job.creator = user.User(user_data)
            jobs.append(this_job)
        return jobs

    
    #i in  comments will pull the  value from list of coments
    #loop through the rest of the comments to check if any of their id maches the i's comment id
    #you might have to stop at 2, thats sufficient