from django.conf import settings
from django.conf.urls.static import static
from django.urls import path


from .views import AnsAccept, AnsCreate, AnsDelete, AnsDetail, AnsList, \
    PrivateList, StickerCreate, StickerDelete, StickerDetail, StickerList,\
    StickerUpdate


urlpatterns = [
    path(
        'private/',
        PrivateList.as_view(),
        name='private_list'
    ),
    path(
        'private/<int:pk>/accept',
        AnsAccept.as_view(),
        name='ans_accept'
    ),
    path(
        'private/<int:pk>/delete',
        AnsDelete.as_view(),
        name='ans_delete'
    ),
    path(
        'stickers/',
        StickerList.as_view(),
        name='stickers'
    ),
    path(
        'stickers/<int:pk>',
        StickerDetail.as_view(),
        name='sticker'
    ),
    path(
        'stickers/create',
        StickerCreate.as_view(),
        name='sticker_create'
    ),
    path(
        'stickers/<int:pk>/update',
        StickerUpdate.as_view(),
        name='sticker_update'
    ),
    path(
        'stickers/<int:pk>/delete',
        StickerDelete.as_view(),
        name='sticker_delete'
    ),
    path(
        'stickers/<int:pk>/ans',
        AnsList.as_view(),
        name='stickers_ans'
    ),
    path(
        'ans/<int:pk>',
        AnsDetail.as_view(),
        name='ans'
    ),
    path(
        'stickers/<int:pk>/ans/create',
        AnsCreate.as_view(),
        name='ans_create'
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
