# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         manage.py
# Description:  
# Author:       zhnmozhang@gmail.com--EP45-DS3L
# Date:         2020/3/17  22:31
#-------------------------------------------------------------------------------

from app import create_app

app=create_app("development")


if __name__ == '__main__':
    app.run()