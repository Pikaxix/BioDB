# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:         __init__.py.py
# Description:  
# Author:       zhnmozhang@gmail.com--EP45-DS3L
# Date:         2020/3/17  23:51
# -------------------------------------------------------------------------------

from flask import Blueprint
from app import Mongodb

# create BluePrint object
api = Blueprint("api", __name__)

from . import demo
from . import system_view