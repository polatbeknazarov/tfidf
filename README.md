# TF-IDF Веб-приложение на FastAPI

Это веб-приложение на FastAPI позволяет загружать текстовые файлы и отображает таблицу из 50 самых значимых слов по их TF (Term Frequency) и IDF (Inverse Document Frequency) значению. Слова сортируются по убыванию IDF.

## Установка и запуск
1. **Клонируйте репозиторий:**
```bash
git clone https://github.com/polatbeknazarov/tfidf.git
cd tfidf
```

2. **Создайте виртуальное окружение и активируйте его:**
```bash
python -m venv venv
source venv/bin/activate  # Для Linux/Mac
venv\Scripts\activate     # Для Windows
```

3. **Установите зависимости:**
```bash
pip install -r requirements.txt
```

4. **Запустите приложение:**
```bash
uvicorn app.main:app --reload

# Или перейдите в app и запустите

cd app
uvicorn main:app --reload
```



