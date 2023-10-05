from flask import Flask
from housing.logger import logging
import sys
from housing.exception import HousingException

app = Flask(__name__)


@app.route('/home',methods=['GET','POST'])
def home():
    try:
        raise Exception("We are testing custom exception")
    except Exception as e:
        housing=HousingException(e,sys)
        logging.info(housing.error_message)
        logging.info("we are testing the logging module")
    return 'First Machine Learning Project'


if __name__=="__main__":
    app.run(debug=True)