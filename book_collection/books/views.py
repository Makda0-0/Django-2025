import json
from django.http import JsonResponse, HttpResponseBadRequest, HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .models import Author, Book

# Helper function to serialize models to JSON
def serialize_author(author):
    return {
        'id': author.id,
        'name': author.name,
        'bio': author.bio,
        'birth_date': str(author.birth_date) if author.birth_date else None,
    }

def serialize_book(book):
    return {
        'id': book.id,
        'title': book.title,
        'author': serialize_author(book.author),
        'publication_year': book.publication_year,
        'genre': book.genre,
        'description': book.description,
    }

# Author Views
@csrf_exempt  # For simplicity in API; in production, handle CSRF properly
@require_http_methods(["GET"])
def author_list(request):
    authors = Author.objects.all()
    data = [serialize_author(author) for author in authors]
    return JsonResponse({'authors': data})

@csrf_exempt
@require_http_methods(["GET"])
def author_detail(request, pk):
    try:
        author = Author.objects.get(pk=pk)
        data = serialize_author(author)
        return JsonResponse(data)
    except Author.DoesNotExist:
        return HttpResponseNotFound(JsonResponse({'error': 'Author not found'}))

# Book Views
@csrf_exempt
@require_http_methods(["GET"])
def book_list(request):
    books = Book.objects.all()
    data = [serialize_book(book) for book in books]
    return JsonResponse({'books': data})

@csrf_exempt
@require_http_methods(["GET"])
def book_detail(request, pk):
    try:
        book = Book.objects.get(pk=pk)
        data = serialize_book(book)
        return JsonResponse(data)
    except Book.DoesNotExist:
        return HttpResponseNotFound(JsonResponse({'error': 'Book not found'}))

@csrf_exempt
@require_http_methods(["POST"])
def book_create(request):
    try:
        data = json.loads(request.body)
        author = Author.objects.get(pk=data['author_id'])
        book = Book.objects.create(
            title=data['title'],
            author=author,
            publication_year=data['publication_year'],
            genre=data.get('genre'),
            description=data.get('description')
        )
        return JsonResponse({'message': 'Book created', 'book': serialize_book(book)}, status=201)
    except (KeyError, Author.DoesNotExist, json.JSONDecodeError):
        return HttpResponseBadRequest(JsonResponse({'error': 'Invalid data'}))

@csrf_exempt
@require_http_methods(["PUT"])
def book_update(request, pk):
    try:
        book = Book.objects.get(pk=pk)
        data = json.loads(request.body)
        if 'title' in data:
            book.title = data['title']
        if 'author_id' in data:
            book.author = Author.objects.get(pk=data['author_id'])
        if 'publication_year' in data:
            book.publication_year = data['publication_year']
        if 'genre' in data:
            book.genre = data['genre']
        if 'description' in data:
            book.description = data['description']
        book.save()
        return JsonResponse({'message': 'Book updated', 'book': serialize_book(book)})
    except (Book.DoesNotExist, Author.DoesNotExist, json.JSONDecodeError):
        return HttpResponseBadRequest(JsonResponse({'error': 'Invalid data or book not found'}))

@csrf_exempt
@require_http_methods(["DELETE"])
def book_delete(request, pk):
    try:
        book = Book.objects.get(pk=pk)
        book.delete()
        return JsonResponse({'message': 'Book deleted'})
    except Book.DoesNotExist:
        return HttpResponseNotFound(JsonResponse({'error': 'Book not found'}))