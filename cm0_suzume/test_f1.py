from flask import Flask

app=Flask(__name__)

@app.route('/')
def hello():
   name = "Hello World"
   return name
   

@app.route('/good_afternoon')
def good():
   name= "Good Afernoon"
   return name
   

if __name__ == "__main__":
   app.run()
