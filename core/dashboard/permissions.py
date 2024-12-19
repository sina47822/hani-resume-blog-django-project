from django.contrib.auth.mixins import UserPassesTestMixin
from account.models import UserType


class HasHamgamAccessPermission(UserPassesTestMixin):

    def test_func(self):
        if self.request.user.is_authenticated:
            return self.request.user.type == UserType.hamgam.value
        return False
    

class HasHamrahAccessPermission(UserPassesTestMixin):

    def test_func(self):
        if self.request.user.is_authenticated:
            return self.request.user.type == UserType.hamrah.value
        return False