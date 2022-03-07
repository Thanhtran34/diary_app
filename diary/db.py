import mysql.connector

class Database:
    def __init__(self, **kwargs):
        self.connection = mysql.connector.connect(**kwargs)
        self.cursor = self.connection.cursor(dictionary=True)

    def find_user_by_id(self, user_id):
        self.cursor.execute(f"SELECT * FROM user WHERE user_id = '{user_id}'")

        return self.cursor.fetchone()

    def find_user_by_username(self, username):
        self.cursor.execute(f"SELECT * FROM user WHERE username = '{username}'")
        
        return self.cursor.fetchone()

    def create_user(self, username, password):
        self.cursor.execute(f"INSERT INTO user (username, password) VALUES ('{username}', '{password}')")
        self.connection.commit()

        return self.cursor.lastrowid

    def create_diary(self, user_id, diary_type):
        self.cursor.execute(f"INSERT INTO diaries VALUES (0, {user_id},'{diary_type}', NOW())")
        self.connection.commit()

        return self.cursor.lastrowid

    def find_diary_by_user_id(self, user_id):
        self.cursor.execute(f"SELECT * FROM diaries WHERE user_id = {user_id}")

        return self.cursor.fetchall()
    
    def find_diary_by_id(self, diary_id):
        self.cursor.execute(f"SELECT * FROM diaries WHERE diary_id = {diary_id}")

        return self.cursor.fetchone()

    def find_story_by_name(self, story_name):
        self.cursor.execute(f"SELECT * FROM story WHERE name = '{story_name}'")
        return self.cursor.fetchone()
    
    def create_story(self, story_name, story_content):
        self.cursor.execute(f"INSERT INTO exercise VALUES (0, '{story_name}', '{story_content}')")
        self.connection.commit()

        return self.cursor.lastrowid
    
    def create_diary_type(self, diary_id, story_id, name, day, process):
        self.cursor.execute(f"INSERT INTO diary_type VALUES (0, {diary_id}, {story_id}, {name}, {day}, {process})")
        self.connection.commit()

        return self.cursor.lastrowid

    def find_story_data_for_diary_by_story_id(self, story_id):
        self.cursor.execute(("SELECT name, description "
                            "FROM diary_type "
                            "INNER JOIN story "
                            "ON diary_type.story_id = story.story_id "
                            f"WHERE story_id = {story_id}"))

        return self.cursor.fetchall()

    def find_story_details_by_user_id(self, user_id):
        self.cursor.execute(("SELECT "
                                "story.name AS name, "
                                "ROUND(AVG(process), 1) AS avg_process, "
                                "MAX(process) AS max_process, "
                                "ROUND(AVG(working_day), 1) AS avg_working_day, "
                                "SUM(working_day) AS total_working_day "
                            "FROM diary_type "
                            "INNER JOIN diaries "
                                "ON diary_type.diary_id = diaries.diary_id "
                            "INNER JOIN story "
                                "ON diary_type.story_id = story.story_id "
                            f"WHERE user_id = {user_id} "
                            "GROUP BY story.name"))

        return self.cursor.fetchall()
 
    def find_all_diary(self):
        self.cursor.execute("SELECT * FROM diary_list")

        return self.cursor.fetchall()