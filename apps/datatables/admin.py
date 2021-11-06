# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from import_export import resources
from import_export.admin import ImportMixin

from apps.datatables.models import Transaction


class TransactionResource(resources.ModelResource):
    class Meta:
        model = Transaction
        fields = ['id', 'bill_for', 'issue_date', 'due_date', 'total', 'status']


@admin.register(Transaction)
class TransactionAdmin(ImportMixin, admin.ModelAdmin):
    list_display = ['id', 'bill_for', 'issue_date', 'due_date', 'total', 'status', 'created_time']
    resource_class = TransactionResource