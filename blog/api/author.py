from combojsonapi.event.resource import EventsResource
from flask_combo_jsonapi import ResourceDetail, ResourceList

from blog.extensions import db
from blog.models import Article, Author
from blog.schemas import AuthorSchema


class AuthorDetailEvents(EventsResource):

    def event_get_articles_count(self, id: int = None, *args, **kwargs):
        return {"count": Article.query.filter(Article.author_id == id).count()}


class AuthorList(ResourceList):
    schema = AuthorSchema
    data_layer = {
        "session": db.session,
        "model": Author,
    }


class AuthorDetail(ResourceDetail):
    events = AuthorDetailEvents
    schema = AuthorSchema
    data_layer = {
        "session": db.session,
        "model": Author,
    }
