from flask import redirect, url_for
from flask_admin import AdminIndexView, expose
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user


class CustomAdminView(ModelView):
    def create_blueprint(self, admin):
        """
        Create Flask blueprint.
        """
        blueprint = super().create_blueprint(admin)
        blueprint.name = f"{blueprint.name}_admin"
        return self.blueprint

    def get_url(self, endpoint, **kwargs):
        if not (endpoint.startswith(".") or endpoint.startswith("admin.")):
            endpoint = endpoint.replace(".", "_admin.")
        return super().get_url(endpoint, **kwargs)

    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_staff

    def inaccessible_callback(self, name, **kwargs):
        # redirect to login page if user doesn't have access
        return redirect(url_for("auth.login"))


class CustomAdminIndexView(AdminIndexView):
    @expose("/")
    def index(self):
        if not (current_user.is_authenticated and current_user.is_staff):
            return redirect(url_for("auth.login"))
        return super(CustomAdminIndexView, self).index()


class TagAdminView(CustomAdminView):
    column_searchable_list = ("name",)
    column_filters = ("name",)
    create_modal = True
    edit_modal = True


class ArticleAdminView(CustomAdminView):
    column_filters = ("author_id",)
    can_export = True
    export_types = ("csv", "xlsx")
    can_view_details = True
    details_modal = True


class UserAdminView(CustomAdminView):
    column_exclude_list = ("password",)
    column_details_exclude_list = ("password",)
    column_export_exclude_list = ("password",)
    column_searchable_list = ("first_name", "last_name", "username", "is_staff", "email")
    column_filters = ("first_name", "last_name", "username", "is_staff", "email")
    can_create = False
    can_delete = False
    can_edit = True
    can_view_details = False
    column_editable_list = ("first_name", "last_name", "is_staff")
    form_columns = ("first_name", "last_name", "is_staff")
