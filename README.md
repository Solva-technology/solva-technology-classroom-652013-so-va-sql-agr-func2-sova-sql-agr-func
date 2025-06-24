# solva-generators-iterators
Репозиторий с практическими задачами по теме: агрегатные функции sql.

## 🚀 Быстрый старт

### 1. Клонирование репозитория

```bash
git clone ssh-сслыка из репозитория
cd solva-sql-arg-func
```

### 2. Создание и активация виртуального окружения

#### 💻 Linux/macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

#### 🪟 Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Установка зависимостей

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

---

### 4. Создание таблиц
В файле tasks/schema.sql напишите скрипт, который создаст таблицу с нужными полями.
Запускать скрипт не нужно!

### 5. Сборка БД
В корневой директории проекта запустите скрипт вручную или с помощью команды
```
python build_db.py
```

---

### 6. Проверка решения
После решения задачи в файлах query вам необходимо проверить проект прежде чем отправить его на ревью:
```
flake8 . && isort --check-only --diff . && pytest
```