# -------------------------------------------------------------------------------
# Name:         config.py
# Description:  
# Author:       zhnmozhang@gmail.com--EP45-DS3L
# Date:         2020/3/17  22:54
# -------------------------------------------------------------------------------

import logging


class Config(object):
    # config
    SECRET_KEY = "SDUASHFIRFGHRTOHJR"
    # DataBase
    MONGO_URI = ''
    # MONGO_USERNAME = ''
    # MONGO_PASSWORD = ''


class Development_Config(Config):
    DEBUG = True
    LOGGIONG_LEVEL = logging.DEBUG


class Production_Config(Config):
    pass


configs = {
    "development": Development_Config,
    "production": Production_Config
}
