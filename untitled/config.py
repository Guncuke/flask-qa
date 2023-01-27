SECRET_KEY = 'alksjdlajlvjlas'


# 数据库配置
HOSTNAME = '127.0.0.1'
PORT = 3306
USERNAME = 'root'
PASSWORD = 'wch010411'
DATABASE = 'qa_platform'
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI

# 邮箱配置
MAIL_SERVER = 'smtp.qq.com'
MAIL_USE_SSL = True
MAIL_PORT = 465
MAIL_USERNAME = '780530653@qq.com'
MAIL_PASSWORD = 'kohvpkhruzdkbbaf'
MAIL_DEFAULT_SENDER = '780530653@qq.com'
