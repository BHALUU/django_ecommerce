from .models import Category


def categories(request):
    print(Category.objects.all())
    return {"categories": Category.objects.filter(level=0)}
