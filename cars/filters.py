from dj_rql.filter_cls import AutoRQLFilterClass
from cars.models import Car, Review


class CarFilterClass(AutoRQLFilterClass):
    MODEL = Car


class ReviewFilterClass(AutoRQLFilterClass):
    MODEL = Review
