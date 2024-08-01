from flask import Flask, render_template_string, request

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Simple XSS Example</title>
        <style>
            body {
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
                font-family: Arial, sans-serif;
                background-color: #f0f0f0;
            }
            .container {
                text-align: center;
                background-color: white;
                padding: 20px;
                border-radius: 8px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            }
            form {
                margin: 0;
            }
            input[type="text"] {
                width: 100%;
                padding: 10px;
                margin: 10px 0;
                border: 1px solid #ccc;
                border-radius: 4px;
            }
            input[type="submit"] {
                padding: 10px 20px;
                border: none;
                border-radius: 4px;
                background-color: #007BFF;
                color: white;
                cursor: pointer;
            }
            input[type="submit"]:hover {
                background-color: #0056b3;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Simple XSS Example</h1>
            <form method="POST" action="/submit">
                <label for="message">Enter a message:</label><br>
                <input type="text" id="message" name="message"><br>
                <input type="submit" value="Submit">
            </form>
        </div>
    </body>
    </html>
    '''

@app.route('/submit', methods=['POST'])
def submit():
    message = request.form['message']
    return render_template_string(f'''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Message Submitted</title>
        <style>
            body {{
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
                font-family: Arial, sans-serif;
                background-color: #f0f0f0;
            }}
            .container {{
                text-align: center;
                background-color: white;
                padding: 20px;
                border-radius: 8px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            }}
            p {{
                word-wrap: break-word;
                max-width: 300px;
                margin: 0 auto;
            }}
            a {{
                display: inline-block;
                margin-top: 20px;
                padding: 10px 20px;
                border-radius: 4px;
                background-color: #007BFF;
                color: white;
                text-decoration: none;
            }}
            a:hover {{
                background-color: #0056b3;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Message Submitted</h1>
            <p>{message}</p>
            <a href="/">Go back</a>
        </div>
    </body>
    </html>
    ''')

if __name__ == '__main__':
    app.run(debug=True)
