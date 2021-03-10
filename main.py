from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return '''<body>
                    <p>
                        <a href="templates/base.html">/promotion_image</a>
                    </p>
                    <p>
                        <a href="templates/form_base.html">/form_sample</a>
                    </p>
                    <p>
                        /choice/
                    </p>
                    <p>
                        /results/<nickname>/<int:level>/<float:rating>
                    </p>
                </body>'''


@app.route('/choice/<planet_name>')
def choice(planet_name):
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet"
                   href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                   integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                   crossorigin="anonymous">
                    <title>Варианты выбора</title>
                  </head>
                  <body>
                        <h1>Мё предложение:{planet_name}</h1>

                        <h2>Эта планета близка к Земле<h2>

                        <div class="alert alert-primary" role="alert">
                            На ней много необходимых ресурсов.
                        </div>
                        
                        <div class="alert alert-secondary" role="alert">
                            На ней есть вода и атмосфера.
                        </div>
                        
                        <div class="alert alert-success" role="alert">
                            На ней есть небольшое магнитоное поле.
                        </div>
                        
                        <div class="alert alert-danger" role="alert">
                            Наконец, она просто красива!
                        </div>
                  </body>
                </html>'''


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def results(nickname, level, rating):
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet"
                   href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                   integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                   crossorigin="anonymous">
                    <title>Варианты выбора</title>
                  </head>
                  <body>
                        <h1>Результаты отборочного отбора</h1>
                        <h2>Претендента на участие в миссии {nickname}<h2>

                        <div class="alert alert-success" role="alert">
                            Поздравляем! Ваш рейтинг после {level} эиапа отбора
                        </div>

                        <div>
                            Составляет {rating}
                        </div>

                        <div class="alert alert-warning" role="alert">
                            Желаем удачи!
                        </div>
                  </body>
                </html>
'''


@app.route('/promotion_image')
def promotion_image():
    return render_template('base.html')


@app.route('/form_sample', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return render_template('form_base.html')
    elif request.method == 'POST':
        print(request.form['family_name'])
        print(request.form['name'])
        print(request.form['email'])
        print(request.form['education'])
        print(request.form['occupation'])
        print(request.form['gender'])
        print(request.form['why'])
        print(request.form['accept'])
        return "Форма отправлена"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
