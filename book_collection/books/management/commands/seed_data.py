from django.core.management.base import BaseCommand
from books.models import Author, Book

class Command(BaseCommand):
    help = 'Seeds the database with sample data for authors and books'

    def handle(self, *args, **options):
        # Create sample authors
        author1 = Author.objects.create(name="George Orwell", bio="Famous writer", birth_date="1903-06-25")
        author2 = Author.objects.create(name="J.K. Rowling", bio="Author of Harry Potter", birth_date="1965-07-31")

        # Create sample books
        Book.objects.create(title="1984", author=author1, publication_year=1949, genre="Dystopian", description="A classic novel about totalitarianism.")
        Book.objects.create(title="Animal Farm", author=author1, publication_year=1945, genre="Satire", description="An allegory of the Russian Revolution.")
        Book.objects.create(title="Harry Potter and the Philosopher's Stone", author=author2, publication_year=1997, genre="Fantasy", description="The start of a magical adventure.")

        self.stdout.write(self.style.SUCCESS('Successfully seeded the database with sample data!'))