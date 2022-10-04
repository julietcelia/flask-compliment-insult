"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Home page."""

    return "<!doctype html><html>Hi! This is the home page. <a href='/hello'> Say hello! </a> </html>"


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          What's your name? <input type="text" name="person"><br>
          Select a compliment:<br>
          <input type="radio" name = "compliment" value ="awesome">awesome
          <input type="radio" name = "compliment" value ="terrific">terrific
          <input type="radio" name = "compliment" value ="fantastic">fantastic
          <input type="radio" name = "compliment" value ="neato">neato
          <input type="radio" name = "compliment" value ="fabulous">fabulous
          <input type="radio" name = "compliment" value ="wowza">wowza
          <input type="radio" name = "compliment" value ="oh-so-not-meh">oh-so-not-meh
          <input type="radio" name = "compliment" value ="brilliant">brilliant
          <input type="radio" name = "compliment" value ="ducky">ducky
          <input type="radio" name = "compliment" value ="coolio">coolio
          <input type="radio" name = "compliment" value ="incredible">incredible
          <input type="radio" name = "compliment" value ="wonderful">wonderful
          <input type="radio" name = "compliment" value ="smashing">smashing
          <input type="radio" name = "compliment" value ="lovely">lovely
          <input type="submit" value="Submit"><br>
          </form>

          <form action="/diss">
          Or, if you want to be insulted, what's your name? <input type="text" name="person"><br>
          Select a diss:<br>
          <input type="radio" name = "insult" value ="bad">bad
          <input type="radio" name = "insult" value ="horrible">horrible
          <input type="radio" name = "insult" value ="crap">crap
          <input type="radio" name = "insult" value ="ugho">ugho
          <input type="radio" name = "insult" value ="trash">trash
          <input type="radio" name = "insult" value ="yikes">yikes
          <input type="radio" name = "insult" value ="bah-hum-bug">bah-hum-bug
          <input type="radio" name = "insult" value ="ignorant">ignorant
          <input type="radio" name = "insult" value ="a loser">a loser
          <input type="radio" name = "insult" value ="cringe">cringe
          <input type="radio" name = "insult" value ="absurd">absurd
          <input type="radio" name = "insult" value ="terrible">terrible
          <input type="radio" name = "insult" value ="unfortunate">unfortunate
          <input type="radio" name = "insult" value ="gross">gross
          <input type="submit" value="Submit">
        </form>
      </body>
    </html>
    """


@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")
    compliment = request.args.get("compliment")
    # compliment = choice(AWESOMENESS)

    return f"""
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {player}! I think you're {compliment}!
      </body>
    </html>
    """

@app.route('/diss')
def diss_person():
    """Diss user by name."""

    player = request.args.get("person")
    insult = request.args.get("insult")

    return f"""
    <!doctype html>
    <html>
      <head>
        <title>An Insult</title>
      </head>
      <body>
        Hi, {player}! I think you're {insult}!
      </body>
    </html>
    """


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")
