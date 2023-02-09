from combojsonapi.event.resource import EventsResource
from combojsonapi.permission import PermissionUser
from flask_combo_jsonapi import ResourceDetail, ResourceList

from blog.api.permissions.article import (ArticleGetDetailPermission,
                                          ArticlePatchPermission)
from blog.extensions import db
from blog.models import Article
from blog.schemas import ArticleSchema


class ArticleListEvents(EventsResource):

    def event_get_count(self, _permission_user: PermissionUser = None, *args, **kwargs):
        return {"count": Article.query.count()}


class ArticleList(ResourceList):
    events = ArticleListEvents
    schema = ArticleSchema
    data_layer = {
        "session": db.session,
        "model": Article,
    }


class ArticleDetail(ResourceDetail):
    schema = ArticleSchema
    data_layer = {
        "session": db.session,
        "model": Article,
        "permission_get": [ArticleGetDetailPermission],
        "permission_patch": [ArticlePatchPermission],
    }
