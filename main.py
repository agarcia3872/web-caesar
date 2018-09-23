from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>
<html>
  <head>
    <style>
      form {{
          background-color: #eee;
          padding: 20px;
          margin: 0 auto;
          width: 540px;
          font: 16px sans-serif;
          border-radius: 10px;
      }}
      text-area {{
          margin: 10px 0;
          width: 540px;
          height: 120px;
      }}

    </style>
  </head>
  <body>
    <form method='POST'>
      <label>
      Rotate by:
        <input type="text" name="rot" value= "0" />
        <br>
        <textarea rows="10" cols="50" name="text">{0}</textarea>
        <br>
        <input type="submit" value="Submit Query"/>
      </label>
    </form>
  </body>
</html>
"""
@app.route("/", methods=['POST'])
def encrypt():
    rotated = request.form['rot']
    text = request.form['text']
        
    encrypted = rotate_string(text, int(rotated))

    #return "<h1>" + encrypted + "</h1>"
    return form.format(encrypted)

@app.route("/")
def index():
    return form.format("")

app.run()