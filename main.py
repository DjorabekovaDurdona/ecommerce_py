from database import Base, engine, SessionLocal
from models import Product, Seller
Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)


session = SessionLocal()

try:
    seller = Seller(name="Muhammadyor")
    session.add(seller)
    session.commit()

    product = Product(id=1, name="Telefon",
                      description="fefef",
                      price=22.3,
                      seller_id=1)
    session.add(product)
    session.commit()
    
except Exception as error:
    session.rollback()
    print(f"NIMADIR XATO KETDI: {error}")

finally:
    session.close()
