from .loader import app


@app.route('/')
def hi():
    return "Hi"
