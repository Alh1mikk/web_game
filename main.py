from flask import Flask, render_template, request, redirect

app = Flask(__name__)

#Запуск страницы с контентом
@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
