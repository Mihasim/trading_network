from django.contrib import admin
from django.db.models import QuerySet

from main_app.models import Product, TheLinkOfTheNetwork


@admin.register(Product)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ("name", "model", "date_of_release")


@admin.register(TheLinkOfTheNetwork)
class TheLinkOfTheNetworkAdmin(admin.ModelAdmin):
    list_display = ("type_provider", "name", "email", "country", "city", "street", "house_number", "products", "provider", "debit_to_the_provider", "creation_time")
    list_filter = ("city",)
    actions = ['del_debit']

    @admin.action(description="Очистить задолженость перед поставщиком")
    def del_debit(self, request, queryset: QuerySet):
        queryset.update(debit_to_the_provider=0)
        self.message_user(
            request,
            f"Задолженность была очищена"
        )
