from django.test import TestCase

# Create your tests here.
class TestNeighbourhood(TestCase):
    def setUp(self):
       
        self.new_neighbourhood = neighbourhood(Name='Kasarani', City='Nairobi', Town='Kasarani',Info='Yes', securitycontact='955', healthcontact='955', Occupantscount='3')
        self.new_User = User(username= 'sandys', password='Stanford2020*')
        self.new_user = user(user= self.new_User,Neighbourhood= self.new_neighbourhood)

    def tearDown(self):
        user.objects.all().delete()
        neighbourhood.objects.all().delete()
        Business.objects.all().delete()

    def testinstance(self):

        self.assertTrue(isinstance(self.new_neighbourhood, neighbourhood))
    def testsaveneighbourhood(self):
        self.new_User.save()
        self.new_neighbourhood.save()
        self.new_user.saveuser()
        neighbourhoods = neighbourhood.objects.all()
        self.assertTrue(len(neighbourhoods)>0)

    def testdeleteneighbourhood(self):
        self.new_User.save()
        self.new_neighbourhood.save()
        self.new_user.saveuser()
        neighbourhoods = neighbourhood.objects.all()
        self.assertTrue(len(neighbourhoods)>0)
        self.new_neighbourhood.deletehood()
        neighbourhoods = neighbourhood.objects.all()
        self.assertEqual(len(neighbourhoods),0)