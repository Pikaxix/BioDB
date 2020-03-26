#-------------------------------------------------------------------------------
# Name:         demo.py
# Description:  
# Author:       zhnmozhang@gmail.com--EP45-DS3L
# Date:         2020/3/17  23:55
#-------------------------------------------------------------------------------

from . import api
from flask import current_app
from flask import jsonify

@api.route("/index")
def index():
    current_app.logger.error("error_info")
    current_app.logger.warn("warn info")
    current_app.logger.debug("debug info")

    # return "index page"
    return jsonify("saddddddddddddd")