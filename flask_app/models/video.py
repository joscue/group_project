from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import os, cv2
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
#category searches//////////////////////////////////////////////////////    
    @classmethod
    def get_v_boats(cls):
        query = """
                SELECT * FROM categories
                JOIN videos on categories.video_id = videos.id
                WHERE categories.boats = 'true';
                """
        results = connectToMySQL(cls.db).query_db(query)
        jobs =[]
        for row in results:
            this_job = cls(row)
            jobs.append(this_job)
        return jobs
    
    @classmethod
    def get_v_bushcraft(cls):
        query = """
                SELECT * FROM categories
                JOIN videos on categories.video_id = videos.id
                WHERE categories.bushcraft = 'true';
                """
        results = connectToMySQL(cls.db).query_db(query)
        jobs =[]
        for row in results:
            this_job = cls(row)
            jobs.append(this_job)
        return jobs
    
    @classmethod
    def get_v_cabinetry(cls):
        query = """
                SELECT * FROM categories
                JOIN videos on categories.video_id = videos.id
                WHERE categories.cabinetry = 'true';
                """
        results = connectToMySQL(cls.db).query_db(query)
        jobs =[]
        for row in results:
            this_job = cls(row)
            jobs.append(this_job)
        return jobs
    
    @classmethod
    def get_v_cars(cls):
        query = """
                SELECT * FROM categories
                JOIN videos on categories.video_id = videos.id
                WHERE categories.cars = 'true';
                """
        results = connectToMySQL(cls.db).query_db(query)
        jobs =[]
        for row in results:
            this_job = cls(row)
            jobs.append(this_job)
        return jobs
    
    @classmethod
    def get_v_carpentry(cls):
        query = """
                SELECT * FROM categories
                JOIN videos on categories.video_id = videos.id
                WHERE categories.carpentry = 'true';
                """
        results = connectToMySQL(cls.db).query_db(query)
        jobs =[]
        for row in results:
            this_job = cls(row)
            jobs.append(this_job)
        return jobs
    
    @classmethod
    def get_v_electronics(cls):
        query = """
                SELECT * FROM categories
                JOIN videos on categories.video_id = videos.id
                WHERE categories.electronics = 'true';
                """
        results = connectToMySQL(cls.db).query_db(query)
        jobs =[]
        for row in results:
            this_job = cls(row)
            jobs.append(this_job)
        return jobs
    
    @classmethod
    def get_v_he(cls):
        query = """
                SELECT * FROM categories
                JOIN videos on categories.video_id = videos.id
                WHERE categories.home_electricity = 'true';
                """
        results = connectToMySQL(cls.db).query_db(query)
        jobs =[]
        for row in results:
            this_job = cls(row)
            jobs.append(this_job)
        return jobs
    
    @classmethod
    def get_v_hvac(cls):
        query = """
                SELECT * FROM categories
                JOIN videos on categories.video_id = videos.id
                WHERE categories.hvac = 'true';
                """
        results = connectToMySQL(cls.db).query_db(query)
        jobs =[]
        for row in results:
            this_job = cls(row)
            jobs.append(this_job)
        return jobs

    @classmethod
    def get_v_machining(cls):
        query = """
                SELECT * FROM categories
                JOIN videos on categories.video_id = videos.id
                WHERE categories.machining = 'true';
                """
        results = connectToMySQL(cls.db).query_db(query)
        jobs =[]
        for row in results:
            this_job = cls(row)
            jobs.append(this_job)
        return jobs

    @classmethod
    def get_v_morotrcycles(cls):
        query = """
                SELECT * FROM categories
                JOIN videos on categories.video_id = videos.id
                WHERE categories.motorcycles = 'true';
                """
        results = connectToMySQL(cls.db).query_db(query)
        jobs =[]
        for row in results:
            this_job = cls(row)
            jobs.append(this_job)
        return jobs
    
    @classmethod
    def get_v_planes(cls):
        query = """
                SELECT * FROM categories
                JOIN videos on categories.video_id = videos.id
                WHERE categories.planes = 'true';
                """
        results = connectToMySQL(cls.db).query_db(query)
        jobs =[]
        for row in results:
            this_job = cls(row)
            jobs.append(this_job)
        return jobs

    @classmethod
    def get_v_plumbing(cls):
        query = """
                SELECT * FROM categories
                JOIN videos on categories.video_id = videos.id
                WHERE categories.plumbing = 'true';
                """
        results = connectToMySQL(cls.db).query_db(query)
        jobs =[]
        for row in results:
            this_job = cls(row)
            jobs.append(this_job)
        return jobs
    
    @classmethod
    def get_v_roofing(cls):
        query = """
                SELECT * FROM categories
                JOIN videos on categories.video_id = videos.id
                WHERE categories.roofing = 'true';
                """
        results = connectToMySQL(cls.db).query_db(query)
        jobs =[]
        for row in results:
            this_job = cls(row)
            jobs.append(this_job)
        return jobs
    
    @classmethod
    def get_v_tractors(cls):
        query = """
                SELECT * FROM categories
                JOIN videos on categories.video_id = videos.id
                WHERE categories.tractors = 'true';
                """
        results = connectToMySQL(cls.db).query_db(query)
        jobs =[]
        for row in results:
            this_job = cls(row)
            jobs.append(this_job)
        return jobs
    
    @classmethod
    def get_v_welding(cls):
        query = """
                SELECT * FROM categories
                JOIN videos on categories.video_id = videos.id
                WHERE categories.welding = 'true';
                """
        results = connectToMySQL(cls.db).query_db(query)
        jobs =[]
        for row in results:
            this_job = cls(row)
            jobs.append(this_job)
        return jobs
    
    @classmethod
    def get_v_ww(cls):
        query = """
                SELECT * FROM categories
                JOIN videos on categories.video_id = videos.id
                WHERE categories.wood_working = 'true';
                """
        results = connectToMySQL(cls.db).query_db(query)
        jobs =[]
        for row in results:
            this_job = cls(row)
            jobs.append(this_job)
        return jobs
    
    @classmethod
    def get_v_3dp(cls):
        query = """
                SELECT * FROM categories
                JOIN videos on categories.video_id = videos.id
                WHERE categories.3d_printings = 'true';
                """
        results = connectToMySQL(cls.db).query_db(query)
        jobs =[]
        for row in results:
            this_job = cls(row)
            jobs.append(this_job)
        return jobs

#validations//////////////////////////////////////////////////////////////
    @staticmethod
    def validate_vid(data):
        valid =  True
        if len(data['title']) < 4:
            flash("")
            is_valid = False

    @staticmethod
    def make_thumbnail(data):
        thumb = cv2.VideoCapture('flask_app/static/videos/' + data['id'] + '.mp4')
        the_frame = 0
        while (True):
            success, frame = thumb.read()
            cv2.imwrite('flask_app/static/images/' + data['id'] + '.jpg', frame)
            break


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