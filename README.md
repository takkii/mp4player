### 試作版動画配信サイト、仕様書

```markdown
# FireFox / 対応済み、現在は動作する。
動画ファイル形式.mp4、「サポートされたファイル形式およびMIMEタイプの動画が見つかりませんでした。」
```

- [管理者側](http://localhost/admin/)、管理画面へログイン。各種設定ができる。

- [動画配信サイト](http://localhost)に表示、[ファイル情報](localhost/video/1/)へアクセスもできる。

> アップロードしたい動画をMicrosoft Clipcampで編集しmp4形式でエクスポートする必要あり。

```markdown
# bashでコンテナ内に入る
docker-compose exec db bash

# mariadb、rootパスワード設定
mysql -u root -p
use mysql;
ALTER USER 'root'@'localhost' IDENTIFIED BY "20070920";

# マイグレーション
docker-compose exec web python manage.py makemigrations
docker-compose exec web python manage.py migrate

# 管理者を作成、ユーザ名、メールアドレス、パスワード設定
docker-compose exec web python manage.py createsuperuser
```

※ 2025/04/10、Dockerfileは未検証。ユーザテストも未だ。

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