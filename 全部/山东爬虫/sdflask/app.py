from flask import Flask,render_template,request
from sdpc.shandong import sdcx
app = Flask(__name__)


@app.route('/',methods=["GET"])
def hello_world():
    return render_template("sd.html")

@app.route('/1/',methods=["POST"])
def hblongs():
    hphm = request.form.get("plate_number")
    hpzl = request.form.get("car_type")
    fdjh = request.form.get("vin")
    b = sdcx(hphm,hpzl,fdjh)
    return b

if __name__ == '__main__':
    # app.run(debug=False, host='0.0.0.0', port=9900)
    app.run()