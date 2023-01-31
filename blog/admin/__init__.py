def register_admin_views():
    from blog import models
    from blog.admin.views import ArticleAdminView, TagAdminView, UserAdminView
    from blog.extensions import admin, db

    admin.add_view(ArticleAdminView(models.Article, db.session, category="Models"))
    admin.add_view(TagAdminView(models.Tag, db.session, category="Models"))
    admin.add_view(UserAdminView(models.User, db.session, category="Models"))
