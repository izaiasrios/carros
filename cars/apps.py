from django.apps import AppConfig



class CarsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cars'



def ready(self):
        # Importa o módulo de signals para registrá-los
        import cars.signals