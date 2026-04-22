import sqlite3

class DB_Manager:
    def __init__(self, database):
        self.database = database # имя базы данных
        
    def create_tables(self):
        # Implementation to create database tables
        conn = sqlite3.connect(self.database)
        cursor = conn.cursor()
        with conn:
            conn.execute(""" 
CREATE TABLE project_skills
     (skill_id INTEGER,
      project_id INTEGER,
    FOREIGN KEY (skill_id) REFERENCES skills(skill_id),  
    FOREIGN KEY (project_id) REFERENCES projects(project_id))   )
    FOREIGN KEY (project_id)  REFERENCES CarsID (project_id) ON DELETE SET NULL
                         """)

        conn.execute(""" 
CREATE TABLE skills
     (skill_id INTEGER PRIMARY KEY,
      skill_name TEXT NOT NULL)""")
        conn.execute("""
            create table status
            (status_id INTEGER PRIMARY KEY,
             status_name TEXT NOT NULL)""")
        conn.execute("""
CREATE TABLE projects
    project_id INTEGER PRIMARY KEY,
    user_id INTEGER,
    project_name TEXT NOT NULL,
    description TEXT,
    url TEXT,
    status_id INTEGER,
    FOREIGN KEY(status_id) REFERENCES status(status_id))""")


if __name__ == '__main__':
        manager = DB_Manager(DATABASE)
        manager.create_tables()     
        
        conn.commit()
        conn.close()