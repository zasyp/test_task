from pydantic import BaseModel
from datetime import datetime

class TableBase(BaseModel):
    name: str
    seats: int
    location: str

class TableCreate(TableBase):
    pass

class TableResponse(TableBase):
    id: int

class ReservationBase(BaseModel):
    customer_name: str
    table_id: int
    reservation_time: datetime
    duration_minutes: int

class ReservationCreate(ReservationBase):
    pass

class ReservationResponse(ReservationBase):
    id: int