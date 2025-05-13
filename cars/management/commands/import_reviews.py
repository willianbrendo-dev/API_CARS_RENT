import csv
from django.core.management.base import BaseCommand
from cars.models import Review, Car

class Command(BaseCommand):
    help = 'Importa avaliações a partir de um CSV'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Caminho para o arquivo CSV de avaliações')

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']

        try:
            with open(csv_file, newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    try:
                        car = Car.objects.get(id=row['car_id'])
                        Review.objects.create(
                            car=car,
                            user_name=row['user_name'],
                            user_position=row['user_position'],
                            comment=row['comment'],
                            rating=int(row['rating']),
                            date=row['date']
                        )
                        self.stdout.write(self.style.SUCCESS(f"Avaliação de {row['user_name']} importada."))
                    except Car.DoesNotExist:
                        self.stderr.write(self.style.WARNING(f"Carro com id {row['car_id']} não encontrado."))
        except FileNotFoundError:
            self.stderr.write(self.style.ERROR(f"Arquivo '{csv_file}' não encontrado."))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f"Erro ao importar avaliações: {e}"))
