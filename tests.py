from django.test import TestCase

# Create your tests here.

# from django.db.models.functions import TruncMonth
#
# Sales.objects
#     .annotate(month=TruncMonth('timestamp'))   # Truncate to month and add to select list
#     .values('month')    # Group By month
#     .annotate(c=Count('id'))    # Select the count the grouping
#     .values('month', 'c')   # (might be redundant, haven't tested) select month and count
