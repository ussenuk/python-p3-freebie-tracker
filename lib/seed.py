#!/usr/bin/env python3

# Script goes here!
from faker import Faker
import random

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Company, Dev, Freebie

if __name__ == '__main__':
    engine = create_engine('sqlite:///freebies.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    session.query(Company).delete()
    session.query(Dev).delete()
    session.query(Freebie).delete()

    fake = Faker()

    item_names = ['hoodie','laptop sticker', 
                  'flask', 'water bottle', 'T-shirt',
                'key holder', 'pen','bag','notebook',
                'flash disk']
    
    devs = []
    for i in range(50):
        dev = Dev(
            name=fake.name(),
        )

        session.add(dev)
        session.commit()

        devs.append(dev)
    
    companies = []
    for i in range(10):
        company = Company(
            name = fake.name(),
            founding_year=fake.year()
        )
        # add and commit individually to get IDs back
        
        session.add(company)
        session.commit()

        companies.append(company)


    freebies = []
    for i in range(50):
        dev = random.choice(devs)
        company = random.choice(companies)

        # Create association between dev and company
        dev.companies.append(company)
        company.devs.append(dev)

        freebie = Freebie(
                item_name =random.choice(item_names),
                value = random.randint(5,100),
                company_id=company.id,
                dev_id=dev.id,
            )


        session.add(freebie)
        session.commit()

        freebies.append(freebie)

    session.close()


    