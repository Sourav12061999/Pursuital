from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
class Batch(models.Model):
    name = models.CharField(max_length=255)#name will be web or and or da
    type = models.CharField(max_length=255) # Type will be either FT or PT
    def __str__(self):
        return self.name

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser):
    name = models.CharField(max_length=255)
    student_id = models.CharField(max_length=255, default="")
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE, default=1)
    profile_image = models.CharField(max_length=255, default="")
    role = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'role', "batch", "student_id", ]

    def __str__(self):
        return self.email

class Campaign(models.Model):
    name = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    progress = models.CharField(max_length=100)
    link_identifier = models.CharField(max_length=255)
    description = models.TextField()
    cover_photo = models.CharField(max_length=255)
    status = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class CampaignUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)
    enrollment_date = models.DateField()
    status = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.user.username} - {self.campaign.name}"
class Goal(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateField()
    type = models.CharField(max_length=255)
    def __str__(self):
        return self.title
class GoalUser(models.Model):
    campaign_user = models.ForeignKey(CampaignUser, on_delete=models.CASCADE)
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE)
    submission = models.TextField()

    def __str__(self):
        return f"{self.campaign_user} - {self.goal}"
class Milestone(models.Model):
    name = models.CharField(max_length=255)
    goal_count = models.IntegerField()

    def __str__(self):
        return self.name

class MilestoneUser(models.Model):
    milestone = models.ForeignKey(Milestone, on_delete=models.CASCADE)
    campaign_user = models.ForeignKey(CampaignUser, on_delete=models.CASCADE)
    achievement_date = models.DateField()
    def __str__(self):
        return f"{self.milestone} - {self.campaign_user}"