from flask import Flask, render_template, request
import random

app = Flask(__name__)

greetings = ["My Pookie Bear,", "Sweetheart", "Lovely", "Beloved", "Dear", "Sweet"]
compliments = [
    "You light up my life", 
    "Your smile is my sunshine", 
    "You are the apple of my eye",
    "My heart skips a beat every time I see you",
    "You're the reason I believe in love",
    "I think about you every night before I go to sleep",
    "I love you more than I love Shrek"
]
endings = ["Forever yours", "With all my love", "Yours always", "Eternally devoted", "The Bestest ever"]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        return render_template('letter.html', name=name)
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_love_letter():
    name = request.form['name']
    greeting = random.choice(greetings)
    compliment = random.choice(compliments)
    ending = random.choice(endings)
    
    letter = f"{greeting} {name},<br><br>{compliment}.<br><br>{ending},<br><br>Amy <3"
    return render_template('letter.html', letter=letter, name=name)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)