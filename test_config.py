import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'test.db')
#SQLALCHEMY_DATABASE_URI = 'postgresql://sunday:@localhost/bucketlist'
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'migrations')