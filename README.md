# Эндпоинты

`/api/pets/` -- все животные

`/api/pets/1` -- животное с id 1

`/api/pets/random/?count=4` -- 4 рандомных (для главной страницы)

`http://127.0.0.1:8000/media/photos/1.png` -- фото с названием 1.png

`/api/pets/available/` -- со статусом available

# Запуск проекта

### Требования

Перед запуском должны быть установлены:

- Docker
- Docker Compose

### Проверить установку:

`docker --version`
`docker compose version`

---

### Клонирование репозитория

`git clone https://github.com/x3genius/meow-backend`
`cd meow-backend`

---

### Создание файла .env

В корне проекта создать файл ".env", шаблон -- dotenv_example

---

### Сборка и запуск контейнеров

Выполнить:

`docker compose up --build`

После запуска будут подняты:

- Django
- PostgreSQL

---

### Выполнение миграций

Открыть второй терминал и выполнить:

`docker compose exec web python manage.py migrate`

---

### Создание администратора

При первом запуске необходимо создать суперпользователя:

`docker compose exec web python manage.py createsuperuser`

Следовать инструкциям в терминале.

---

### Доступ к приложению

Сайт:

http://localhost:8000

Административная панель:

http://localhost:8000/admin

---

### Остановка проекта

Остановить контейнеры:

`docker compose down`

---

### Полное удаление данных

Удалить контейнеры и тома PostgreSQL:

`docker compose down -v`

После выполнения команды база данных будет удалена полностью.
При следующем запуске потребуется заново выполнить миграции и создать суперпользователя.