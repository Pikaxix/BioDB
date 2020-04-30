# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:         __init__.py.py
# Description:  
# Author:       zhnmozhang@gmail.com--EP45-DS3L
# Date:         2020/3/17  23:51
# -------------------------------------------------------------------------------

from flask import Blueprint
from app import Mongodb
from flask_cors import CORS


# create BluePrint object
api = Blueprint("api", __name__)
CORS(api)

from . import demo
from . import microbe