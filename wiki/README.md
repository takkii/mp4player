### 使い方

```markdown
# mariadb、rootパスワード設定
mysql -u root -p
use mysql;
ALTER USER 'root'@'localhost' IDENTIFIED BY "20070920";

# マイグレーション
python manage.py makemigrations
python manage.py migrate

# 管理者を作成、ユーザ名、メールアドレス、パスワード設定
python manage.py createsuperuser
```

```markdown
# wsgiサーバ: 本番用、稼働時はdockerでnginxを利用する
waitress-serve --port=80 mp4player.wsgi:application

> INFO:waitress:Serving on http://0.0.0.0:80

# ローカルサーバ: 開発用、初期値、localhost:8000
python manage.py runserver localhost:80

> WARNING: This is a development server. Do not use it in a production setting. Use a production WSGI or ASGI server instead.
> For more information on production servers see: https://docs.djangoproject.com/en/5.2/howto/deployment/
```

※ 開発用と本番用でサーバ切り替えが必要。