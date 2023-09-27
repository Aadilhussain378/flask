from flask import Flask,request,render_template


app=Flask(__name__)  # create the object



@app.route('/')
def welcome():
    return "Welcome to the flask"

@app.route('/cal',method=["GET"])
def math_operstion():
    operation=request.json["operation1"]
    number1=request.json["number1"]
    number2=request.json["number2"]


    if operation=='add':
        result=number1+number2
    elif operation=='multiply':
        result=number1*number2
    elif operation=='division':
        result=number1/number2
    else:
        result=number1-number2



print(__name__)

if __name__=='__main__':
    app.run()