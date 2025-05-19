# aso-analysis-tool
External single-page on RapidAPI/ASOMobile/ASOWorld. Analysis by keywords. API service (backend + frontend):  1) 5 competitors, 2) aver/max number of indexed keywords for competitors, 3) traffic loss assessment. Application title or link to the App Store/Google Play. The system finds the corresponding app_id via the ASOMobile/ASOWorld API.
Creating an external single-page service based on RapidAPI/ASOMobile/ASOWorld + building the logic of competitive analysis by keywords

📍 Backend Stack:
Django 5.0.6
● Python 3.2+
● FastAPI
● Celery (for tasks)
● Redis (optional for cache)
● DB: SQLite for saving sessions

Чтобы избежать сложностей с получением URL API адреса, я создала test_data.json файл для тестирования  различных сценариев работы API. Вот его содержимое:

{
  "results": [
    {
      "title": "Application 1",
      "developer": "Developer 1",
      "rating": 4.5,
      "app_id": "com.example.app1"
    },
    {
      "title": "Application 2",
      "developer": "Developer 2",
      "rating": 4.2,
      "app_id": "com.example.app2"
    }
  ]
}
После введения названия приложения в посковое окно, например, Application 1,  и нажатия кнопки SEARCH выходит вот такой результат:
{
  "app": {
    "id": 1,
    "name": "Application 1",
    "api_app_id": "com.example.app1",
    "indexed_keywords_count": 0
  },
  "competitors": []
}
Данный результат означает, что тестовый JSON-файл  читается и обрабатывается корректно, и приложение "Application 1" было успешно найдено и возвращено API-эндпоинтом.
Данный результат работы приложения и пустым списком конкурентов ("competitors": []), говорит о следующем:
    • Код успешно прочитал test_data.json. 
    • Код нашел приложение с названием "Application 1" (или с app_query, который  использовалсы для поиска). 
    • Данные этого приложения были сериализованы с помощью AppSerializer. 
    • Функция get_competitors вернула пустой список (что, вероятно, является ожидаемым поведением, если для этого тестового приложения нет связанных конкурентов в базе данных).
