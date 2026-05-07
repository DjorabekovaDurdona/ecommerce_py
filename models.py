from sqlalchemy import Integer, String, Float, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import Base


class Seller(Base):
    __tablename__ = 'sellers'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(length=50), index=True)
    products: Mapped[list["Product"]] = relationship("Product", back_populates="seller")


class Product(Base):
    __tablename__ = 'products'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(length=50), index=True)
    description: Mapped[str] = mapped_column(String(length=50), index=True)
    price: Mapped[float] = mapped_column(Float, primary_key=True)

    seller_id: Mapped[int] = mapped_column(Integer, ForeignKey("sellers.id"))
    seller: Mapped["Seller"] = relationship("Seller", back_populates="products")


class Customer(Base):
    __tablename__ = 'customers'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(length=50), index=True)
  
    orders: Mapped["Order"] = relationship("Order", back_populates="customer")


class Order(Base):
    __tablename__ = 'orders'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(length=50), index=True)

    customer_id: Mapped[int] = mapped_column(Integer, ForeignKey("customers.id"))

    customer: Mapped[list["Customer"]] = relationship("Customer", back_populates="orders")
