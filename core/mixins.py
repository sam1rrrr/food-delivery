from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class OwnerRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        obj = self.get_object()

        if hasattr(obj, 'restaurant'):
            return obj.restaurant.owner == self.request.user or self.request.user.is_superuser
        
        return obj.owner == self.request.user