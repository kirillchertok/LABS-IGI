from ..models import News

class NewsRepository:
    @staticmethod
    def get_all():
        return News.objects.all()