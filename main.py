from flask import Flask
import os, random

app= Flask(__name__)

@app.route("/")
def Home():
    return  '<h1>Indifference_Game</h1><i><a href="/livelli">i livelli</i>'

@app.route("/livelli")
def liv():
    levels = {
        "level1": os.listdir('static/images/levels/level1'),
        "level2": os.listdir('static/images/levels/level2'),
        "level2": os.listdir('static/images/levels/level3'),
        "level2": os.listdir('static/images/levels/level4'),
        "level2": os.listdir('static/images/levels/level5'),
        "level2": os.listdir('static/images/levels/level6'),
        "level2": os.listdir('static/images/levels/level7'),
        "level2": os.listdir('static/images/levels/level8'),
        "level2": os.listdir('static/images/levels/level9'),
        "level2": os.listdir('static/images/levels/level10'),
    }
    random_image = random.choice(levels['level1'])
    random_image = random.choice(levels['level2'])
    random_image = random.choice(levels['level3'])
    random_image = random.choice(levels['level4'])
    random_image = random.choice(levels['level5'])
    random_image = random.choice(levels['level6'])
    random_image = random.choice(levels['level7'])
    random_image = random.choice(levels['level8'])
    random_image = random.choice(levels['level9'])
    random_image = random.choice(levels['level10'])
    return "<h1>Livelli<h1>"

app.run(debug=True)



