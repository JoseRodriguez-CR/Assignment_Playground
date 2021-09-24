from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route( '/' )
def welcome():
    return "Welcome!"

@app.route( '/play', methods=['GET'] )  #/<int:num>
def play():
    counterList = []
    num = 3
    for i in range(0, num):
        counterList.append(num)
    return render_template( 'index.html', counter = counterList )

@app.route( '/play/<int:num>', methods=['GET'] )  #/<int:num>
def playNum( num):
    counterList = []
    for i in range(0, num):
        counterList.append(num)
    return render_template( 'index.html', counter = counterList )
'''
@app.route( '/play/<int:num>/<str:color>', methods=['GET'] )  #/<int:num>
def playNumColor( num, color ):
    counterList = []
    for i in range(0, num):
        counterList.append(num)
    return render_template( 'index.html', counter = counterList, color =color )
'''


if __name__ == "__main__":
    app.run( debug = True)
