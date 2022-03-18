import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    """Base configuration"""
    DEBUG = False
    TESTING = False
    MIGRATION_DIR = os.path.join(basedir, 'uber', 'migrations')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              r'sqlite:///' + os.path.join(basedir, 'lacrema.db') + '?check_same_thread=False'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or '82d4ee5aea9c0fd2d0939077143ae683'