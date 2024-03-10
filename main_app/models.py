from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name="Название")
    model = models.CharField(max_length=150, verbose_name="Модель")
    date_of_release = models.DateField(verbose_name="Дата выхода продукта на рынок")

    def __str__(self):
        return f"{self.name}, {self.model}"

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"


class TheLinkOfTheNetwork(models.Model):
    factory = 'factory'
    retail_network = 'retail_network'
    individual_entrepreneur = 'individual_entrepreneur'
    type_provider = [
        (factory, 'Завод'),
        (retail_network, 'Розничная сеть'),
        (individual_entrepreneur, 'Индивидуальный предприниматель'),
    ]

    type_provider = models.CharField(max_length=50, verbose_name='Тип поставщика', choices=type_provider)
    name = models.CharField(max_length=150, verbose_name="Название")
    email = models.EmailField(max_length=150, verbose_name="email")
    country = models.CharField(max_length=150, verbose_name="Страна")
    city = models.CharField(max_length=150, verbose_name="Город")
    street = models.CharField(max_length=150, verbose_name="Улица")
    house_number = models.CharField(max_length=10, verbose_name="Номер дома")
    products = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Продукты", **NULLABLE)
    provider = models.ForeignKey('TheLinkOfTheNetwork', on_delete=models.CASCADE, verbose_name="Поставщик", **NULLABLE)
    debit_to_the_provider = models.DecimalField(max_digits=20, decimal_places=2,
                                                verbose_name="Задолженность перед поставщиком", **NULLABLE)
    creation_time = models.TimeField(auto_now_add=True, verbose_name="Время создания", **NULLABLE)

    def __str__(self):
        return f"{self.name}, {self.provider}"

    class Meta:
        verbose_name = "Звено сети"
        verbose_name_plural = "Звенья сети"
        ordering = ("-city",)
