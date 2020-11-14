from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published')
    content = models.TextField()
    likes = models.IntegerField(default=0)
    views = models.IntegerField(default=0)

    @property
    def excerpt(self):
        """Fetch first 500 characters of content"""
        excerpt = self.content[:500]
        excerpt += "..." if len(self.content) > 500 else ""
        return excerpt
    
    @property
    def pub_str(self):
        """Publication date as formatted string"""
        return self.pub_date.strftime("%-d %b %Y")

    def __str__(self):
        return self.title