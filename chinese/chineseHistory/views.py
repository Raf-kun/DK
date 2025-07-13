from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Review
import json


def index(request):
    return render(request, "index.html")


@csrf_exempt
def submit_review(request):
    if request.method == 'POST':
        try:
            # Проверяем, что данные пришли в JSON формате
            try:
                data = json.loads(request.body)
            except json.JSONDecodeError:
                return JsonResponse({'status': 'error', 'message': 'Неверный формат данных'}, status=400)

            # Проверяем наличие ключа 'review'
            if 'review' not in data:
                return JsonResponse({'status': 'error', 'message': 'Отсутствует текст отзыва'}, status=400)

            # Создаем отзыв с проверкой на пустую строку
            review_text = data['review'].strip()
            if not review_text:
                return JsonResponse({'status': 'error', 'message': 'Текст отзыва не может быть пустым'}, status=400)

            review = Review.objects.create(text=review_text)
            return JsonResponse({
                'status': 'success',
                'message': 'Отзыв сохранен!',
                'review_id': review.id  # Добавляем ID созданного отзыва
            })
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': f'Ошибка сервера: {str(e)}'}, status=500)
    return JsonResponse({'status': 'error', 'message': 'Метод не разрешен'}, status=405)


def get_reviews(request):
    try:
        reviews = Review.objects.all().order_by('-created_at')
        reviews_list = [{
            'text': review.text, 
            'date': review.created_at.strftime('%d.%m.%Y %H:%M'),
            'id': review.id
        } for review in reviews]
        return JsonResponse({'status': 'success', 'reviews': reviews_list})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
