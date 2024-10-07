# API для блога

Данное веб-приложение, позволяет пользователям создавать и публиковать свои собственные статьи, а также комментировать статьи других пользователей.

## Технологии

**Server:** Django, Django Rest Framework, sqlite3

## Функционал

1. Регистрация и авторизация пользователей
2. Создание и публикация статей
3. Комментирование статей
4. Отображение списка всех статей
5. Отображение отдельной статьи
6. Отображение списка комментариев к статье

## Установка

1. Клонировать репозиторий
2. Установить зависимости: pip install -r requirements.txt
3. Создать базу данных: python manage.py migrate
4. Запустить сервер: python manage.py runserver

### Статьи

#### Список всех статей

```http
  GET /api/post/all_post_list/
```

#### Отдельная статья

```http
  GET /api/post/post_id/${id}/
```
#### Создание новой статьи

```http
  POST /api/post/post_create/
```
#### Обновление статьи

```http
  PUT /api/post/post_update/${id}/
```
#### Удаление статьи

```http
  DELETE /api/post/post_delete/${id}/
```
#### Фильтация статьи по категориям 

```http
  GET /api/post/all_post_list/?category=${category}
```

### Auth

#### Регистрация пользователя

```http
  POST /api/auth/users/
```

#### Авторизация пользователя

```http
  POST /auth/token/login/
```
#### Выход пользователя

```http
  POST /auth/token/logout/
```

### Категории

#### Все категории

```http
  GET /api/categories/
```

### Комментарии

#### Список всех комментариев

```http
  GET /api/comments/all_comments_list/
```

#### Создание нового комментария

```http
  POST /api/comments/create_comment/
```
#### Обновление комментария

```http
  PUT /api/comments/update_comment/${id}/
```
#### Удаление комментария

```http
  DELETE /api/comments/comment_delete/${id}/
```