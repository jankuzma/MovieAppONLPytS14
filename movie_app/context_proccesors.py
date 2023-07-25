from datetime import datetime


def zegarek(request):
    return {'date':datetime.now().date}