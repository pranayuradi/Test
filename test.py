from flask import Flask, request, render_template_string, jsonify

app = Flask(__name__)

# Simple HTML template for login form
login_form_html = """
<!DOCTYPE html>
<html>
<head><title>Login</title></head>
<body>
  <form action="/login" method="post">
    Username: <input type="text" name="username" /><br><br>
    Password: <input type="password" name="password" /><br><br>
    <input type="submit" value="Login" />
  </form>
</body>
</html>
"""

# Dummy credentials for example
VALID_USERNAME = "user"
VALID_PASSWORD = "pass"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        # Render the HTML login form
        return render_template_string(login_form_html)
    elif request.method == 'POST':
        # Support both form-data and JSON payload
        data = request.form if request.form else request.json
        username = data.get('username')
        password = data.get('password')
        if username == VALID_USERNAME and password == VALID_PASSWORD:
            return jsonify({"message": "Login successful!"})
        else:
            return jsonify({"message": "Invalid credentials."}), 401

if __name__ == '__main__':
    app.run(debug=True)
