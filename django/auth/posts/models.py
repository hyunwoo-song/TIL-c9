from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
# ResizeToFill : 300, 300 맞추고 넘치는 부분 잘라냄
# ResizeToFit : 300, 300 맞추고 남는 부분을 빈 공간으로 둠.





# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    # image = models.ImageField(blank=True)
    image = ProcessedImageField(
            upload_to='posts/images', # 저장위치
            processors=[ResizeToFill(300, 300)], # 처리할 작업 목록
            format='JPEG', # 저장 포맷 (확장자)
            options={'quality':90} # 저장 포맷 관련 옵션
        )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    
    def __str__(self):
        return self.title
        
        
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()