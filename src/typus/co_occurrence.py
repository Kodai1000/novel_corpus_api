from sqlalchemy import *
from sqlalchemy.orm import *

Base = declarative_base()
class co_occurrence(Base):
    __tablename__ = 'co_occurrence'
    id: Mapped[int] = mapped_column(primary_key=True)
    dep: Mapped[str] = mapped_column(String(255))
    head_word: Mapped[str] = mapped_column(String(255))
    head_word_pos: Mapped[str] = mapped_column(String(255))
    head_reading: Mapped[str] = mapped_column(String(255))
    target_word: Mapped[str] = mapped_column(String(255))
    target_word_pos: Mapped[str] = mapped_column(String(255))
    target_reading: Mapped[str] = mapped_column(String(255))
    count: Mapped[int] = mapped_column()
    logdice: Mapped[float] = mapped_column()
    average_distance: Mapped[int] = mapped_column()
    identifier: Mapped[str] = mapped_column(String(255))
    genre: Mapped[str] = mapped_column(String(255))
    
    def to_json(self):
        return {
            "id": self.id,
            "dep": self.dep,
            "head_word": self.head_word,
            "head_word_pos": self.head_word_pos,
            "head_reading": self.head_reading,
            "target_word": self.target_word,
            "target_word_pos": self.target_word_pos,
            "target_reading": self.target_reading,
            "count": self.count,
            "logdice": self.logdice,
            "average_distance": self.average_distance,
            "identifier": self.identifier,
            "genre": self.genre
        }
