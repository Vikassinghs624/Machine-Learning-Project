from flask import Flask

app = Flask(__name__)


@app.route('/home',methods=['GET','POST'])
def home():
    return 'First Machine Learning Project'


if __name__=="__main__":
    app.run(debug=True)