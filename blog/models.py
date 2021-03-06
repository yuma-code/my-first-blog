from django.conf import settings
from django.db import models
from django.utils import timezone

DEVICE_CHOICES=[
    ('PS4','PS4'),
    ('PC','PC')
]

PURPOSE_CHOICES=[
    ('カジュアル','カジュアル'),
    ('ランクマッチ','ランクマッチ'),
    ('イベント','イベント'),
]

RANK_CHOICES=[
    ('','指定なし'),
    ('bronz','ブロンズ'),
    ('silver','シルバー'),
    ('gold','ゴールド'),
    ('platinum','プラチナ'),
    ('diamond','ダイヤ'),
    ('master','マスター'),
    ('predator','プレデター')
]

NUM_CHOISES=[
    ('','指定なし'),
    ('1',1),
    ('2',2),
    ('3',3),
    ('4',4)
]

class Post(models.Model):
    # author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    psid= models.CharField(max_length=200)
    comment = models.TextField()
    device = models.CharField(max_length=20, choices=DEVICE_CHOICES,default='PS4')
    purpose = models.CharField(max_length=20, choices=PURPOSE_CHOICES,default='カジュアル')
    rank = models.CharField(max_length=20, choices=RANK_CHOICES,default='指定なし',blank=True)
    num = models.CharField(max_length=20, choices=NUM_CHOISES,default='指定なし',blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)


class Comment(models.Model):
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
