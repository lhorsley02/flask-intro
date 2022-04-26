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

    return "<!doctype html><html>Hi! This is the home page. <a href='/hello'>Hello!</a> <a href='/diss'>Insults...</a> </html>"


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
        <form action="/greet" method='GET'>
          What's your name? <input type="text" name="person"></br>
       What compliment would you like?</br>
          <input type="radio" name="compliment" value="are fantastic!">Fantastic<br>
          <input type="radio" name="compliment" value="are cool!">Cool<br>
          <input type="radio" name="compliment" value="are killing it!">Killing it!<br>
          <input type="radio" name="compliment" value="are a Superstar!">Superstar!<br>
          <input type="submit" value="Submit">
      </form>
      </body>
    </html>
    """

@app.route('/diss')
def diss_user():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Oh, its you...</h1>
        <form action="/insult" method='GET'>
          What's your name? <input type="text" name="person"></br>
       Which insult would you like?</br>
          <input type="radio" name="diss" value="are inadequate.">You're inadequate<br>
          <input type="radio" name="diss" value="are... odd.">You're odd<br>
          <input type="radio" name="diss" value="look like you enjoy eating celery.">Surprise Insult<br>
          <input type="radio" name="diss" value="look like you would lose a fight with a Chihuahua.">Surprise Insult<br>
          <input type="radio" name="diss" value="should love yourself, because no one else does.">Surprise Insult<br>
          <input type="radio" name="diss" value="look like you eat mayonnaise plain.">Surprise Insult<br>
          <input type="radio" name="diss" value="need therapy">Surprise Insult<br>
          <input type="submit" value="Submit">
      </form>
      </body>
    </html>
    """

@app.route('/insult')
def diss_person():
    """Get user by name."""

    player = request.args.get("person")

    diss = request.args.get("diss")

    return f"""
    <!doctype html>
    <html>
      <head>
        <title>A Diss</title>
      </head>
      <body>
        {player}. I think you {diss}
      </body>
    </html>
    """

@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")

    compliment = request.args.get("compliment")

    return f"""
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {player}! I think you {compliment}
      </body>
    </html>
    """


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")
