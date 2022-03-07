from django.test import TestCase
from.models import Profile



class ProfileTestClass(TestCase):

    def setUp(self):
        self.Babra = Profile(name = 'Babra', profile_pic = 'image.jpg', bio='studying at moringa')
        self.Babra.save()

    def tearDown(self):
        Profile.objects.all().delete()
    

    def test_instance(self):
        self.assertTrue(isinstance(self.Babra, Profile))

    def test_save_method(self):
        self.Babra.save_profile()
        name = Profile.objects.all()

    def test_delete_method(self):
        self.profile_pic.delete_profile_pic()
        Profile = Profile.objects.all()
        self.assertTrue(len(Locations)==2) 



