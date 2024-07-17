class LocationIdFilterMixin:
    def get_queryset(self):
        user_location = self.request.user.location
        return super().get_queryset().filter(location=user_location)
