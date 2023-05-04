import django_filters
from .models import Job

class JobFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains') # one word from title
    description = django_filters.CharFilter(lookup_expr='icontains') # one word from description

    class Meta:
        model = Job
        fields = '__all__'
        exclude = ['owner','published_at','salary','image','Vacancy','slug']