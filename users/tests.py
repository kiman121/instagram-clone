from django.test import TestCase
from .models import Profile
from django.contrib.auth.models import User
# Create your tests here.
class ProfileTestCase(TestCase):
    '''
    Test class for the Profile module
    '''
    def setUp(self):
        '''
        Method that creates the instance of the Profile class before every test
        '''
        # Save Profile
        self.new_profile = Profile(name='James')
        # self.new_profile.save()
        

    def test_instance(self):
        '''
        Test case that checks if the object is being instanciated correctly
        '''
        self.assertTrue(isinstance(self.new_profile, Profile))


    def test_save_method(self):
        '''
        Test case that confirms that the Profile object is being saved
        '''
        self.new_profile.save_profile()
        my_profiles = Profile.objects.all()
        self.assertTrue(len(my_profiles) > 0)
    
    def test_update_method(self):
        '''
        Test case that confirms if the update_profile method updates a profile record (name attribute)
        '''
        self.new_profile.save_profile()
        record_id = Profile.objects.last().id
        Profile.update_profile(record_id, "Hellen")
       
        my_profile = Profile.objects.get(id=record_id)

        self.assertEqual(my_profile.name, "Hellen")


