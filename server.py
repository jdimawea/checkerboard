from flask import Flask, render_template # Import Flask to allow us to create our app


app = Flask(__name__)    # Create a new instance of the Flask class called "app"


@app.route('/')          # The "@" decorator associates this route with the function immediately following
def checkerboard():
    return render_template('index.html')


@app.route('/<int:x>')
def checkerboardRow(x, boardColumn = 0, boardRow = 0):
    return render_template('row_col.html', boardColumn = 8, boardRow = x)


@app.route('/<int:x>/<int:y>')
def drawbyInput(x, y):
    return render_template('row_col.html', boardColumn = x, boardRow = y)


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

