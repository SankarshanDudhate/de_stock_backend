from flask_seeder import Seeder
from CustomApi.models import *
from faker import Faker, Generator
from seeds.categoryList import categories

class freshSeed(Seeder):
  def run(parameter_list):
    db.drop_all()
    db.create_all()

    faker = Faker()
    # generator = Generator()

    db.session.add(User(
      name = 'Hitesh Joshi',
      email = 'joshihitesh090@gmail.com',
      phoneNo = '9999999999',
      password = 'Password',
      address = 'my permanent address',
    ))

    for i in range(5):
      user = User(
              name = faker.name(),
              email = faker.email(),
              phoneNo = faker.phone_number(),
              password = "Password",
              address = faker.address()
            )
      print(user.name + " added to Database")
      db.session.add(user)

    for category in categories:
      c = Category(
        name = category
      )

      print(c.name)
      db.session.add(c)

    for i in range(20):
      product = Product(
        name = faker.name(),
        category_id = faker.random.randrange(1,44),
        subCategory_id = None,
        available = True if faker.random.randrange(2) else False,
        user_id = faker.random.randrange(1,6)
      )

      print(product.name)
      db.session.add(product)