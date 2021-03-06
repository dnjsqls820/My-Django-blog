# post/models.py
from django.db import models
# Create your models here.

# class모델을 정의함
# 모델의 이름은 Post
# models 는 Post가 장고 모델임을 의미함 이 코드 때문에 장고는 Post가 데이터베이스에 저장되어야한다고 알게됌
# models.CharField 짧은 문자열 정보
# models.TextField 글자수 제한없는 텍스트
# models.DateTimeField 날짜와 시간
# models.ForeignKey 다른 모델에 대한 링크
# def publish(self)는 publish라는 메서드
# def 는 이것이 함수/메서드라는 뜻
# 메서드 이름은 소문자나 언더스코어를 사용함
# 메서드는 무언가를 돌려줌 return
# 여기서든 __str__를 호출하면 Post모델의 제목 텍스트(string)를 받게 됨


# class Posting(models.Model):
#     author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     title = models.CharField(max_length=200)
#     text = models.TextField()
#     created_date = models.DateTimeField(default=timezone.now)
#     published_date = models.DateTimeField(blank=True, null=True)


#     def publish(self):
#         self.published_date = timezone.now()
#         self.save()

#     def __str__(self):
#         return self.title


class Board(models.Model):
    title = models.CharField(max_length=64, verbose_name='글 제목')
    contents = models.TextField(verbose_name='글 내용')
    writer = models.ForeignKey('user.Member', on_delete=models.CASCADE, verbose_name='작성자')
    write_dttm = models.DateTimeField(auto_now_add=True, verbose_name='글 작성일')

    board_name = models.CharField(max_length=32, default='Python', verbose_name='게시판 종류')
    update_dttm = models.DateTimeField(auto_now=True, verbose_name='마지막 수정일')
    hits = models.PositiveIntegerField(default=0, verbose_name='조회수')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'board'
        verbose_name = '게시판'
        verbose_name_plural = '게시판'