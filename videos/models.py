from django.contrib.auth.models import User
from django.db import models


class Video(models.Model):
    title = models.CharField(max_length=200)  # 動画のタイトル
    description = models.TextField(blank=True, null=True)  # 動画の説明
    video_file = models.FileField(upload_to='movies/', blank=True, null=True)  # 動画ファイルを保存
    created_at = models.DateTimeField(auto_now_add=True)  # 登録日
    category = models.CharField(max_length=100, blank=True, null=True)  # 動画のカテゴリー
    thumbnail = models.ImageField(upload_to='thumbnails/', blank=True, null=True)  # サムネイル画像
    duration = models.PositiveIntegerField(blank=True, null=True)  # 動画の長さ（秒単位）
    is_published = models.BooleanField(default=True)  # 公開状態
    uploaded_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)  # アップロードしたユーザー
    view_count = models.PositiveIntegerField(default=0)  # 視聴回数
    updated_at = models.DateTimeField(auto_now=True)  # 最終更新日
    published_at = models.DateTimeField(null=True, blank=True)  # 公開日

    def __str__(self):
        return self.title
