# Import Flask modules
from flask import Flask, request, render_template
from flaskext.mysql import MySQL

# Create an object named app
app = Flask(__name__)

# This "/home/ec2-user/dbserver.endpoint" file has to be created from cloudformation
# template and it has RDS endpoint
db_endpoint = open("/home/ec2-user/dbserver.endpoint", 'r', encoding='UTF-8')

# Configure mysql database
app.config['MYSQL_DATABASE_HOST'] = db_endpoint.readline().strip()
app.config['MYSQL_DATABASE_USER'] = 'admin'
app.config['MYSQL_DATABASE_PASSWORD'] = 'clarusway_1234'
app.config['MYSQL_DATABASE_DB'] = 'clarusway_phonebook'
app.config['MYSQL_DATABASE_PORT'] = 3306
db_endpoint.close()
mysql = MySQL()
mysql.init_app(app)
connection = mysql.connect()
connection.autocommit(True)
cursor = connection.cursor()

def read_file_into_string(file_path):
    with open(file_path, 'r', encoding='UTF-8') as file:
        file_content = file.read()
    return file_content

data_phonebook_table = read_file_into_string("/home/ec2-user/app/code/clarusway_phonebook.phonebook.sql")
print(data_phonebook_table)
# cursor.execute(data_phonebook_table)