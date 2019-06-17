from django.test import TestCase
from .models import AddUser, EmailGroup


class AddUserTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.user = AddUser(id=1, first_name='New', last_name='User',
                            email='test@user.com', phone=12345678)

    # Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.user, AddUser))

    def test_get_full_name(self):
        self.user.save()
        self.assertEqual(self.user.full_name, 'New User')


class EmailGroupTestClass(TestCase):
    # Setup Method
    def setUp(self):
        self.user = AddUser(first_name='New', last_name='User',
                            email='test@user.com', phone=123456789)
        self.group = EmailGroup(id=1, Title='Testing',
                                users=self.user, members=1)

    # Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.group, EmailGroup))

    def test_create_EmailGroup(self):
        self.user.save()
        self.group.create_EmailGroup()
        self.assertTrue(len(EmailGroup.objects.all()) > 0)

    def test_delete_business(self):
        self.group.delete_EmailGroup()
        self.assertTrue(len(EmailGroup.objects.all()) == 0)
    
    # def test_find_EmailGroup(self):
    #     self.group = EmailGroup.find_EmailGroup(1)
    #     self.assertEqual(self.group.id, 1)