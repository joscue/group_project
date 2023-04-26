from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
#from flask_app.models import user, business

class Video:
    db = 'group_project'
    def __init__(self,data):
        self.id = data['id']
        self.title = data['title']
        self.description = data['description']
        self.updated_at = data['updated_at']
        self.created_at = data['created_at']
        self.creator = None

    @classmethod
    def save_vid(cls,data):
        query = "INSERT INTO videos ( title, description, updated_at, created_at ) VALUES ( %(title)s, %(description)s, NOW(), NOW());"
        return connectToMySQL(Video.db).query_db(query,data)
#put in when you've got it done   user_id,   %(user_id)s,    
    @classmethod
    def delete(cls,data):
        query = "DELETE FROM videos WHERE id = %(id)s"
        squery = "DELETE FROM categories WHERE video_id = %(id)s"
        connectToMySQL(Video.db).query_db(squery,data)
        return connectToMySQL(Video.db).query_db(query,data)
    
    @classmethod
    def update_vid(cls,data):
        query = "UPDATE videos SET title=%(title)s, description=%(description)s WHERE id = %(id)s"
        return connectToMySQL(Video.db).query_db(query,data)

    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM videos WHERE id = %(id)s;"
        results = connectToMySQL('group_project').query_db(query,data)
        return cls(results[0])
    
    @classmethod
    def get_all(cls,):
        query = "SELECT * FROM videos;"
        results = connectToMySQL(Video.db).query_db(query)
        videos = []
        for video in results:
            videos.append( cls(video) )
        return videos
    
    @classmethod
    def get_vids(cls,data):
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
    
    @staticmethod
    def validate_vid(data):
        valid =  True
        if len(data['title']) < 4:
            flash("")
            is_valid = False

    
class Category:
    db = 'group_project'
    def __init__(self,data):
        self.id = data['id']
        self.boats = data['boats']
        self.bushcraft = data['bushcraft']
        self.cabinetry = data['cabinetry']
        self.carpentry = data['carpentry']
        self.cars = data['cars']
        self.electronics = data['electronics']
        self.home_electricity = data['home_electricity']
        self.hvac = data['hvac']
        self.machining = data['machining']
        self.motorcycles = data['motorcycles']
        self.planes = data['planes']
        self.plumbing = data['plumbing']
        self.roofing = data['roofing']
        self.tractors = data['tractors']
        self.welding = data['welding']
        self.wood_working = data['wood_working']
        self.printing = data['printing']
        #self.user_id = data['user_id]
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create_category(cls,data):
        query = "INSERT INTO categories ( boats, bushcraft, cabinetry, carpentry, cars, electronics, home_electricity, hvac, machining, motorcycles, planes, plumbing, roofing, tractors, welding, wood_working, printing, created_at, updated_at ) VALUES ( %(boats)s, %(bushcraft)s, %(cabinetry)s, %(carpentry)s, %(cars)s, %(electronics)s, %(home_electricity)s, %(hvac)s, %(machining)s,%(motorcycles)s,%(planes)s,%(plumbing)s,%(roofing)s,%(tractors)s,%(welding)s,%(wood_working)s,%(printing)s, NOW(), NOW() );"
        return connectToMySQL(Category.db).query_db(query,data)