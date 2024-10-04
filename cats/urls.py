from rest_framework.routers import SimpleRouter

from cats.views import BreedViewSet, CatsViewSet

router = SimpleRouter(use_regex_path=False)
router.register(r'breeds', BreedViewSet)
router.register(r'cats', CatsViewSet, basename="cats")
urlpatterns = router.urls