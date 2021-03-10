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
                            Составляет {rating}!
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
        return f'''
                <!doctype html>
                <html lang="en">
                <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet"
                          href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                          integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                          crossorigin="anonymous">
                    <link rel="stylesheet" type="text/css" href="static/css/form_style.css"/>
                    <title>Пример формы</title>
                </head>
                <body>
                
                <h2>Форма заявки на участие в миссии</h2>
                
                <div>
                    <form class="login_form" method="post">
                
                        <input type="family_name" class="form-control" id="family_name" aria-describedby="emailHelp"
                               placeholder="Введите фамилию" name="family_name">
                
                        <input type="name" class="form-control" id="name" placeholder="Введите имя" name="name">
                
                        <div class="form-group">
                            <label for="classSelect">Какое Ваше образование</label>
                            <select class="form-control" id="education" name="education">
                                <option>ученик Яндекс.Лицей</option>
                                <option>Школьник</option>
                                <option>Студент коледжа</option>
                                <option>Бакалавр</option>
                                <option>Специалитет</option>
                                <option>Магистр</option>
                                <option>Аспирант</option>
                                <option>Просветлённый</option>
                            </select>
                        </div>
                
                        <div>
                            <label>
                                Какова Ваша профессия
                            </label>
                            <div class="form-check">
                                <input class="form-check-input" type="checkbox" value="" name="occupationPROG>
                                                            <label class=" form-check-label" for="flexCheckDefault">
                                Программист
                                </label>
                            </div>
                            <div class="form-check">
                                <input class="form-check-input" type="checkbox" value=""  name="occupationROBO>
                                                          <label class=" form-check-label" for="flexCheckChecked">
                                Робототехник
                                </label>
                            </div>
                            <div class="form-check">
                                <input class="form-check-input" type="checkbox" value=""  name="occupationCHINA">
                                <label class="form-check-label" for="flexCheckChecked">
                                    Переводчик с китайского(中文翻译)
                                </label>
                            </div>
                        </div>
                
                        <div class="form-group">
                            <label for="why">Почему?</label>
                            <textarea class="form-control" id="why" rows="3" name="why"></textarea>
                        </div>

                        <div method="post" enctype="multipart/form-data">
                            <div class="form-group">
                                <label for="photo">Выберите файл</label>
                                <input type="file" class="form-control-file" id="photo" name="file">
                            </div>
                            <button type="submit" class="btn btn-primary">Отправить</button>
                        </div>
                
                        <div class="form-group">
                            <label for="form-check">Укажите пол</label>
                            <div class="form-check">
                                <input class="form-check-input" type="radio" name="gender" id="male" value="male" checked>
                                <label class="form-check-label" for="male">
                                    Мужской
                                </label>
                            </div>
                            <div class="form-check">
                                <input class="form-check-input" type="radio" name="gender" id="female" value="female">
                                <label class="form-check-label" for="female">
                                    Женский
                                </label>
                            </div>
                        </div>
                
                        <div class="form-group form-check">
                            <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                            <label class="form-check-label" for="acceptRules">Соглашаться!</label>
                        </div>
                        <button type="submit" class="btn btn-primary">Отправить</button>
                    </form>
                </div>
                </body>
                </html>'''
    elif request.method == 'POST':
        print("Фамилия", request.form['family_name'])
        print("Имя", request.form['name'])
        print("Статус образованности", request.form['education'])

        print("Почему", request.form['why'])
        print("Пол", request.form['gender'])
        print("Согласен", request.form['accept'])
        return "Форма отправлена"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
