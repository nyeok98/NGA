from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class Blog(models.Model):
    request_place = models.CharField(max_length=20)

    # choicefield가 없어서 charfield에서 쓸 수 있도록 정의
    MEET_PLACE_SELECT_CHOICES = (
        ('흑석', '흑석'),
        ('정문', '정문'),
        ('중문', '중문'),
        ('후문', '후문'),
        ('상도', '상도'),
    )

    # charfield로 들어와서 choices로 정해둔 거불러오기
    meet_place_select = models.CharField(
        max_length=2,
        choices=MEET_PLACE_SELECT_CHOICES,
        default='흑석',
    )
    meet_place_detail = models.CharField(max_length=20)
    request_item = models.CharField(max_length=50, default='')
    request_detail = models.TextField()

    # PositiveIntegerField는 0부터 무한대까지 수량 조절할 수 있는 필드
    request_quantity = models.PositiveIntegerField(default=1)

    fees = models.IntegerField('Fees', default=1000)

    # validators 속성은 최소글자, 최대글자수를 정의
    limited_time_hour = models.IntegerField('Hour', default=0, validators=[
                                            MinValueValidator(0), MaxValueValidator(23)])
    limited_time_min = models.IntegerField('Minute', default=0, validators=[
                                           MinValueValidator(0), MaxValueValidator(59)])
    limited_time_sec = models.IntegerField('Second', default=0, validators=[
                                           MinValueValidator(0), MaxValueValidator(59)])
    # 나타낼 object의 이름을 reqeust_place로 정의

    def __str__(self):
        return self.request_place
