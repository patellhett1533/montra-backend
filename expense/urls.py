from rest_framework.routers import DefaultRouter
from .views import ExpenseApi

router = DefaultRouter()
router.register("expense", ExpenseApi, basename="expense")
urlpatterns = router.urls