from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile, Project, Review 


# Create your tests here.
#1
class ProfileTestClass(TestCase):

    # test 1 Set up Method
    def setUp(self):
        self.user = User(username='juma.a')
        self.user.save()
        self.profile = Profile(
            contact="0700112233",
            profile_picture='testpicture.png',
            bio='bwanamkunaji',
            user=self.user
            )
        self.profile.save_profile()

    def test_instance(self):
        self.assertTrue(isinstance(self.profile,Profile))

    def test_save_profile(self):
        self.profile.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)

    def test_delete_profile(self):
        self.profile.save_profile()
        self.profile.delete_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile) == 0)

    def tearDown(self):
        Profile.objects.all().delete()

#2
class ProjectTestClass(TestCase):
     # test 2 Set up Method
    def setUp(self):
        self.project = Project(
        image='testpicture.png',
        title ='Django',
        description="star-awwaaards",
        link="https://www.star-awwwards.co.ke"
        )

    def tearDown(self):
        Project.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.project, Project))

    def test_save_project(self):
        self.project.save_project()
        projects = Project.objects.all()
        self.assertTrue(len(projects)>0)

    def test_delete_project(self):
        self.project.save_project()
        projects = Project.objects.all()
        self.project.delete_project()
        projects = Project.objects.all()
        self.assertTrue(len(projects)==0)   



class ReviewTestClass(TestCase):
    def setUp(self):
        self.user = User(username='juma.a')
        self.user.save()
        self.project = Project(
            title ='Django', 
            image='testpicture.png',
            description="awwaaards",
            link="https://www.star-awwwards.co.ke"
            )
        self.project.save_project()
        self.new_review=Review(
            design="10",
            usability="10",
            content="10",
            user=self.user,
            project=self.project
            )
        self.new_review.save_review()

    def tearDown(self):
        Review.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_review,Review))

    def test_save_review(self):
        reviews = Review.objects.all()
        self.assertTrue(len(reviews)>0)

    def test_delete_review(self):
        self.new_review.save_review()
        self.new_review.delete_review()
        reviews = Review.objects.all()
        self.assertTrue(len(reviews)==0)             