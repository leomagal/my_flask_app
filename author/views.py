from my_blog import app

@app.route('/login')
def login():
    return "Login Successfull"