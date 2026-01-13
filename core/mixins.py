from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class OwnerRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        obj = self.get_object()
        return obj.owner == self.request.user