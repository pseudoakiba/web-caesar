from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

header = """
<!DOCTYPE html>
<html>
    <head>
        <style>
            form {
                background-color: yellow;
                padding: 30px;
                margin: 20px auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 100px;
            }
            
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
    """

rotate_form = """
      <form action="/encrypt" method="post">
        <h1>Message Encrypter</h1>
        <h2>(using Caesar rotation)</h2>
        <label for="rotation">
            Rotate by:
            <input type="text" name="rot"/>
            <textarea name="text">{0}</textarea>
        </label>
        <input type="submit" value="Encrypt message"/>
      </form>
      """

footer = """
    </body>
</html>
"""

@app.route("/encrypt", methods=['POST'])
def encrypt():
    message = request.form['text']
    rotation = request.form['rot']

    rotated = rotate_string(message,int(rotation))
    content = header + rotate_form.format(rotated) + footer + "<h3>Success! Your rotated message is: " + rotated + "</h1>"
    return content

@app.route("/")
def index():
    content = header + rotate_form.format('') + footer
    return content

app.run()

.gitignore