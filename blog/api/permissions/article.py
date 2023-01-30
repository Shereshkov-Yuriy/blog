from combojsonapi.permission import (PermissionForGet, PermissionForPatch,
                                     PermissionMixin, PermissionUser)
from flask_combo_jsonapi.exceptions import AccessDenied
from flask_login import current_user

from blog.models import Article


class ArticleGetDetailPermission(PermissionMixin):
    ALL_AVAILABLE_FIELDS = [
        "id",
        "author_id",
        "title",
        "body",
        "created_at",
        "updated_at",
        "author",
        "tags",
    ]

    def get(self, *args, many=False, user_permission: PermissionUser = None, **kwargs) -> PermissionForGet:
        if current_user.is_anonymous:
            raise AccessDenied("No access")

        self.permission_for_get.allow_columns = (self.ALL_AVAILABLE_FIELDS, 10)
        return self.permission_for_get


class ArticlePatchPermission(PermissionMixin):
    AVAILABLE_FIELDS_FOR_PATCH = [
        "title",
        "body",
    ]

    def patch_permission(self, *args, user_permission: PermissionUser = None, **kwargs) -> PermissionForPatch:
        self.permission_for_patch.allow_columns = (self.AVAILABLE_FIELDS_FOR_PATCH, 10)
        return self.permission_for_patch

    def patch_data(self, *args, data=None, obj=None, user_permission: PermissionUser = None, **kwargs) -> dict:
        permission_for_patch = user_permission.permission_for_patch_permission(model=Article)
        if not (current_user.is_authenticated and (current_user.is_staff or current_user.author == obj.author)):
            raise AccessDenied("Only authors and admins can change the data")
        return {
            key: val
            for key, val in data.items()
            if key in permission_for_patch.columns
        }
