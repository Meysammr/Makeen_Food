from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from rest_framework.permissions import AllowAny

schema_view = get_schema_view(
    openapi.Info(
        title='My Api',
        default_version='v1',
        description='api documentation using swagger',
        contact=openapi.Contact(email='youreemail@example.com'),
    ),
    public=True,
    permission_classes=[AllowAny]
)