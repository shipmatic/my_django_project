from faker import Faker
from account.models import Profile
fake=Faker()

from account.models import Profile

for i in range (50):
    profile = Profile(
        login=fake.email()+str(i),
        password=fake.password(), 
        nickname=fake.name()+str(i))
    profile.save()
    