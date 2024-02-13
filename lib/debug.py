#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Company, Dev, Freebie

if __name__ == '__main__':
    engine = create_engine('sqlite:///freebies.db')
    Session = sessionmaker(bind=engine)
    session = Session()


    # # Query all companies
    # companies = session.query(Company).all()

    # # For each company, print its name and the names of its devs
    # for company in companies:
    #     print(f'Company: {company.name}')
    #     print('Devs:')
    #     for dev in company.devs:
    #         print(f'- {dev.name}')

    # # Query all devs
    # devs = session.query(Dev).all()

    # # For each dev, print its name and the names of its companies
    # for dev in devs:
    #     print(f'Dev: {dev.name}')
    #     print('Companies:')
    #     for company in dev.companies:
    #         print(f'- {company.name}')


    # # For a particular dev what the freebies collected from different companies
    # dev = session.query(Dev).filter_by(name='Matthew Grant').first()

    # if dev is not None:
    #     print(dev.freebies)
    # else:
    #     print("Developer didn't collect freebies.")

    
    # # Query all freebies
    # freebies = session.query(Freebie).all()

    # for freebie in freebies:
    #     try:
    #         print(freebie.print_details())
    #     except Exception as e:
    #         print(f"Error printing details for freebie with id {freebie.id}: {e}")
    
    # # Query all companies
    # companies = session.query(Company).all()

    # for company in companies:
    #     try:
    #         # Test oldest_company method
    #         oldest_company = Company.oldest_company(session)
    #         print(f"Oldest company: {oldest_company}")
    #     except Exception as e:
    #         print(f"Error finding oldest company for company with id {company.id}: {e}")

    # # Query all devs
    # devs = session.query(Dev).all()

   
   
   # Query all devs and freebies
    devs = session.query(Dev).all()
    freebies = session.query(Freebie).all()

    # Test give_away method for each dev and freebie
    for dev in devs:
        for freebie in freebies:
            try:
                # Use a known dev for testing
                new_dev = devs[0]  # replace with a valid Dev instance
                result = dev.give_away(new_dev, freebie)
                print(f"Dev {dev.name} gave away {freebie.item_name} to {new_dev.name}: {result}")
            except Exception as e:
                print(f"Error giving away freebie with id {freebie.id} from dev with id {dev.id} to dev with id {new_dev.id}: {e}")

    # print(dev.received_one('Freebie Name'))
    # other_dev = Dev(name='Other Dev')
    # session.add(other_dev)
    # session.commit()
    # print(dev.give_away(other_dev, freebie))

    # print(Company.oldest_company(session))



    import ipdb; ipdb.set_trace()
