from rest_framework import routers

from .views import (
    AddColorViewSet,
    DragandDropViewSet,
    DragandDropListViewSet,
    DraggableViewSet,
    DraggableListViewSet
)


router = routers.DefaultRouter(trailing_slash=False)

router.register('addingcolor', AddColorViewSet)
router.register('draganddrop', DragandDropViewSet)
router.register('draganddroplist', DragandDropListViewSet)
router.register('draggable', DraggableViewSet)
router.register('draggablelist', DraggableListViewSet)

urlpatterns = router.urls