from sqlalchemy.orm import Mapped, declarative_base, mapped_column


__all__ = ['Base', 'ItemModel']


Base = declarative_base()


class ItemModel(Base):
    __tablename__ = 'items'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    value: Mapped[float]
    quantity: Mapped[int]
