class Dev():
    ENV = 'development'
    DEBUG = True
    SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://edu:123456@192.168.65.120/edu?charset=utf8'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_ECHO = True
