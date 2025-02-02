from flask import Flask, render_template_string, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Для работы сессии

# Счётчик кликов
click_count = 0

# Telegram-ссылка
telegram_link = "https://t.me/nebelisa_pro"  # Замените your_username на свой Telegram-никнейм

@app.route('/')
def home():
    global click_count
    return render_template_string('''
        <!doctype html>
        <html lang="en">
          <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <title>Мой сайт</title>
            <!-- Подключаем Bootstrap -->
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
            <!-- Подключаем Google Fonts -->
            <link href="https://fonts.googleapis.com/css2?family=Pacifico&family=Roboto:wght@400;700&display=swap" rel="stylesheet">
            <style>
              /* Настройки шрифтов */
              body {
                font-family: 'Roboto', sans-serif;
                background: linear-gradient(135deg, #ff9a9e, #fad0c4);
                color: #333;
                margin: 0;
                padding: 0;
                min-height: 100vh;
                display: flex;
                flex-direction: column;
              }
              h1, h2, h3 {
                font-family: 'Pacifico', cursive;
                color: #fff;
              }

              /* Шапка */
              .header {
                background: linear-gradient(135deg, #6a11cb, #2575fc);
                color: white;
                padding: 1rem;
                text-align: center;
                box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
              }
              .header a {
                color: white;
                text-decoration: none;
                margin: 0 10px;
                font-weight: bold;
              }
              .header a:hover {
                text-shadow: 0 0 10px #fff;
              }

              /* Карточка */
              .card {
                max-width: 400px;
                margin: 2rem auto;
                background: rgba(255, 255, 255, 0.9);
                border-radius: 15px;
                box-shadow: 0 8px 15px rgba(0, 0, 0, 0.2);
                overflow: hidden;
              }
              .card-body {
                padding: 1.5rem;
                text-align: center;
              }
              .card-title {
                font-size: 1.5rem;
                margin-bottom: 1rem;
              }
              .btn-primary {
                background: linear-gradient(135deg, #ff9a9e, #fad0c4);
                border: none;
                color: #333;
                font-weight: bold;
                transition: transform 0.3s ease;
              }
              .btn-primary:hover {
                transform: scale(1.1);
                box-shadow: 0 8px 15px rgba(0, 0, 0, 0.2);
              }

              /* Футер */
              .footer {
                background: linear-gradient(135deg, #6a11cb, #2575fc);
                color: white;
                text-align: center;
                padding: 1rem;
                position: relative;
                bottom: 0;
                width: 100%;
                margin-top: auto;
              }
              .footer a {
                color: white;
                text-decoration: none;
                font-weight: bold;
              }
              .footer a:hover {
                text-shadow: 0 0 10px #fff;
              }
            </style>
          </head>
          <body>
            <!-- Шапка -->
            <div class="header">
              <h1>Привет медвед молодёж!</h1>
              <nav>
                <a href="/">Главная</a>
                <a href="/about">АНЕКДОТЫ</a>
              </nav>
            </div>

            <!-- Основной контент -->
            <div class="card mx-auto">
              <div class="card-body text-center">
                <h5 class="card-title">Связаться со мной</h5>
                <p class="card-text">Нажмите кнопку ниже, чтобы перейти в Telegram.</p>
                <a href="{{ telegram }}" target="_blank" class="btn btn-primary">Напишите мне в Telegram</a>
                <div class="mt-3">
                  <p>Количество кликов: {{ clicks }}</p>
                  <form action="/increment" method="POST">
                    <button class="btn btn-success" type="submit">хомяк</button>
                  </form>
                  <form action="/reset" method="POST">
                    <button class="btn btn-danger mt-2" type="submit">Сбросить счётчик</button>
                  </form>
                </div>
              </div>
            </div>

            <!-- Футер -->
            <div class="footer">
              <p>&copy; 2025 Это только мой сайт никого ему не продам. Все права не защищены. <a href="mailto:your_email@example.com">Напишите мне</a></p>
            </div>
          </body>
        </html>
    ''', telegram=telegram_link, clicks=click_count)

@app.route('/increment', methods=['POST'])
def increment_click():
    global click_count
    click_count += 1
    return redirect(url_for('home'))

@app.route('/reset', methods=['POST'])
def reset_click():
    global click_count
    click_count = 0
    return redirect(url_for('home'))

@app.route('/about')
def about():
    return render_template_string('''
        <!doctype html>
        <html lang="en">
          <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <title>АНЕКДОТЫ</title>
            <!-- Подключаем Bootstrap -->
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
            <!-- Подключаем Google Fonts -->
            <link href="https://fonts.googleapis.com/css2?family=Pacifico&family=Roboto:wght@400;700&display=swap" rel="stylesheet">
            <style>
              /* Настройки шрифтов */
              body {
                font-family: 'Roboto', sans-serif;
                background: linear-gradient(135deg, #ff9a9e, #fad0c4);
                color: #333;
                margin: 0;
                padding: 0;
                min-height: 100vh;
                display: flex;
                flex-direction: column;
              }
              h1, h2, h3 {
                font-family: 'Pacifico', cursive;
                color: #fff;
              }

              /* Шапка */
              .header {
                background: linear-gradient(135deg, #6a11cb, #2575fc);
                color: white;
                padding: 1rem;
                text-align: center;
                box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
              }
              .header a {
                color: white;
                text-decoration: none;
                margin: 0 10px;
                font-weight: bold;
              }
              .header a:hover {
                text-shadow: 0 0 10px #fff;
              }

              /* Основной контент */
              .container {
                padding: 2rem;
                text-align: center;
                background: rgba(255, 255, 255, 0.9);
                border-radius: 15px;
                margin: 2rem auto;
                max-width: 600px;
                box-shadow: 0 8px 15px rgba(0, 0, 0, 0.2);
              }

              /* Футер */
              .footer {
                background: linear-gradient(135deg, #6a11cb, #2575fc);
                color: white;
                text-align: center;
                padding: 1rem;
                position: relative;
                bottom: 0;
                width: 100%;
                margin-top: auto;
              }
              .footer a {
                color: white;
                text-decoration: none;
                font-weight: bold;
              }
              .footer a:hover {
                text-shadow: 0 0 10px #fff;
              }
            </style>
          </head>
          <body>
            <!-- Шапка -->
            <div class="header">
              <h1>АНЕКДОТЫ</h1>
              <nav>
                <a href="/">Главная</a>
                <a href="/about">АНЕКДОТЫ</a>
              </nav>
            </div>

            <!-- Основной контент -->
            <div class="container my-5">
              <h2>сперма члены сиськи</h2>
              <p>Попали в ад американец, индус и русский, встретили Дьявола.
— Всем, кто сюда попадает, я даю шанс попасть в рай. Для этого необходимо выдержать три удара кнутом, не закричав. Я даже разрешу вам защищаться чем угодно, — произнёс Дьявол и достал ужасный огромный горящий кнут.
Первым вышел американец, поднял тяжёлый валун:
— Я готов!
Дьявол размахнулся и первым же ударом разнёс камень в пыль. После второго удара американец заорал как бешеный…
— Следующий, — произнёс хозяин ада.
Выходит индус.
— Чем будешь защищаться?
— Ничем! — отвечает индус, — Я 80 лет занимался йогой, и в медитации тело не чувствует боли!
— Ладно.
Первый удар. Индус молчит. Второй удар. Индус молчит. Третий удар. Индус молчит.
— Невероятно! — Воскликнул поражённый Сатана. — Ещё никто не выдерживал трёх ударов! Ну что же, ты заслужил место в раю, можешь отправляться туда.
— Нет, — говорит индус, — хочу остаться и посмотреть. Во всех анекдотах русские выигрывают. Интересно, как он выкрутится на этот раз.
— Ладно, останься. Ну, так чем ты думаешь защищаться? — обращается Чёрт к русскому.
— Индусом, конечно…</p>
              <a href="/" class="btn btn-primary">Вернуться на главную</a>
            </div>

            <!-- Футер -->
            <div class="footer">
              <p>&copy; 2025 Это только мой сайт никого ему не продам. Все права не защищены. <a href="mailto:gdon24348@gmail.com">Напишите мне</a></p>
            </div>
          </body>
        </html>
    ''')

if __name__ == '__main__':
    app.run(debug=True)