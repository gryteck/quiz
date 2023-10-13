# FastAPI приложение 'Quiz'

В сервисе реализована REST API, принимающий на вход POST запросы по адресу "https://localhost:8000/quiz" с содержимым вида {"question_num":integer}

Сервис же, в свою очередь, запрашивает с публичного API по адресу https://jservice.io/api/random?count={count} уникальные вопросы в указанном количестве и сохраняет их в базу данных в случае, если таких еще нет в базе.

В качестве завершения, данный POST запрос возвращает те вопросы, которые успешно сохранил.

____
**Инструкция по развертке на Linux системах:**
1. Клонировать репозиторий 
<br>`$ git clone https://github.com/gryteck/quiz`
2. Собрать образы в docker-compose
<br>`$ docker compose build`
3. Поднять контейнеры (сервер займет порты 8000, 5432)
<br>`$ docker compose up`
____
**Пример запроса POST:**

```
POST /quiz HTTP/1.1
Host: localhost
Content-Type: application/json

{
  "questions_num": 3
}
```
Пример ответа, возвращаемого при данном POST запросе:
```
HTTP/1.1 200 OK
Content-Type: application/json
[
    {
        "id": 45950,
        "answer": "Magicians",
        "question": "The Linking Ring is the monthly publication of the International Brotherhood of these illusionists",
        "value": 300,
        "airdate": "1997-05-15T19:00:00.000Z",
        "created_at": "2022-12-30T18:56:53.664Z",
        "updated_at": "2022-12-30T18:56:53.664Z",
        "category_id": 856,
        "game_id": 1471,
        "invalid_count": null,
        "category": {
            "id": 856,
            "title": "hobbies",
            "created_at": "2022-12-30T18:40:03.600Z",
            "updated_at": "2022-12-30T18:40:03.600Z",
            "clues_count": 47
        }
    },
    {
        "id": 98229,
        "answer": "<i>The Little Engine That Could</i>",
        "question": "\"I think I can --  I think I can -- I think I can\" name this classic children's tale by Watty Piper",
        "value": 400,
        "airdate": "2003-09-10T19:00:00.000Z",
        "created_at": "2022-12-30T19:23:59.499Z",
        "updated_at": "2022-12-30T19:23:59.499Z",
        "category_id": 2425,
        "game_id": 3324,
        "invalid_count": null,
        "category": {
            "id": 2425,
            "title": "\"big\" & \"little\"",
            "created_at": "2022-12-30T18:48:35.719Z",
            "updated_at": "2022-12-30T18:48:35.719Z",
            "clues_count": 10
        }
    },
    {
        "id": 115300,
        "answer": "<i>War of the Worlds</i>",
        "question": "(Kelly of the Clue Crew reports from the canal in Regent's Park, London.)  In this pioneering science fiction novel about an attack on London the protagonist finds Regent's Canal a spongy mass of dark red vegetation",
        "value": 600,
        "airdate": "2007-02-26T20:00:00.000Z",
        "created_at": "2022-12-30T19:47:57.303Z",
        "updated_at": "2022-12-30T19:47:57.303Z",
        "category_id": 12721,
        "game_id": 1762,
        "invalid_count": null,
        "category": {
            "id": 12721,
            "title": "literary london",
            "created_at": "2022-12-30T19:47:56.533Z",
            "updated_at": "2022-12-30T19:47:56.533Z",
            "clues_count": 5
        }
    }
]


```
