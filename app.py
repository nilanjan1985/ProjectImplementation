
from flask import Flask
<<<<<<< HEAD
from housing.logger import logging
from housing.exception import HousingException
=======
>>>>>>> b4dec1384b977e07ebc84d840e27e9991685526e
app=Flask(__name__)

@app.route("/",methods=['GET','POST'])
def index():
<<<<<<< HEAD
    try:
        raise Exception("We are testing custom exception")
    except Exception as e:
        housing=HousingException(e,sys)
        logging.info(housing.error_message)
        logging.info("We are testing logging module")
    return "CI CD pipeline has been establisjed"
=======
    return "CI CD pipeline has been established"
>>>>>>> b4dec1384b977e07ebc84d840e27e9991685526e

if __name__=="__main__":
    app.run(debug=True)