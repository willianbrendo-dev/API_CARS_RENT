import csv
from django.core.management.base import BaseCommand
from cars.models import Car 


class Command(BaseCommand):
    help = 'Importa carros a partir de um arquivo CSV'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Caminho para o arquivo CSV')

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']

        try:
            with open(csv_file, newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    car, created = Car.objects.get_or_create(
                        name=row['name'],
                        defaults={
                            'description': row['description'],
                            'type': row['type'],
                            'capacity': int(row['capacity']),
                            'transmission': row['transmission'],
                            'fuel_type': row['fuel_type'],
                            'fuel_capacity': int(row['fuel_capacity']),
                            'price_per_day': row['price_per_day'],
                            'original_price': row['original_price'] or None,
                            'is_favorite': row['is_favorite'].strip().lower() == 'true'
                        }
                    )
                    if created:
                        self.stdout.write(self.style.SUCCESS(f"Carro '{car.name}' importado com sucesso."))
                    else:
                        self.stdout.write(self.style.WARNING(f"Carro '{car.name}' já existe."))
        except FileNotFoundError:
            self.stderr.write(self.style.ERROR(f"Arquivo '{csv_file}' não encontrado."))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f"Erro ao importar: {e}"))
