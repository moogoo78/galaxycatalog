from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    DateTime,
    Boolean,
)
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import JSONB

from app.database import Base


class Taxon(Base):
    __tablename__ = 'taxon'
    id = Column(Integer, primary_key=True)
    rank = Column(String(50))
    full_scientific_name = Column(String(500))
    first_epithet = Column(String(500))
    infraspecific_epithet = Column(String(500))
    author = Column(String(500))
    canonical_name = Column(String(500))
    status = Column(String(50))
    # abcd: Botanical
    #hybrid_flag =
    #CultivarName

    # abcd: Zoological
    #Subgenus
    #SubspeciesEpithet
    #Breed
    source_data = Column(JSONB)
