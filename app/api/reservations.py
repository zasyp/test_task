from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from models import Reservation, Table
from schemas import ReservationCreate, ReservationResponse
from database import get_db

router = APIRouter(tags=["Reservations"])

@router.get("/reservations/", response_model=list[ReservationResponse])
def get_all_reservations(db: Session = Depends(get_db)):
    """Получить список всех бронирований"""
    return db.query(Reservation).all()

@router.post("/reservations/", response_model=ReservationResponse, status_code=201)
def create_reservation(
    reservation: ReservationCreate, 
    db: Session = Depends(get_db)
):
    """Создать новое бронирование"""
    table = db.query(Table).get(reservation.table_id)
    if not table:
        raise HTTPException(status_code=404, detail="Table not found")
    
    existing = db.query(Reservation).filter(
        Reservation.table_id == reservation.table_id,
        Reservation.reservation_time <= (
            reservation.reservation_time + 
            timedelta(minutes=reservation.duration_minutes)
        ),
        Reservation.reservation_time + 
        timedelta(minutes=Reservation.duration_minutes) >= 
        reservation.reservation_time
    ).first()
    
    if existing:
        raise HTTPException(
            status_code=409,
            detail="Time slot already booked"
        )
    
    db_reservation = Reservation(**reservation.dict())
    db.add(db_reservation)
    db.commit()
    db.refresh(db_reservation)
    return db_reservation

@router.delete("/reservations/{reservation_id}", status_code=204)
def delete_reservation(reservation_id: int, db: Session = Depends(get_db)):
    """Удалить бронирование"""
    reservation = db.query(Reservation).get(reservation_id)
    
    if not reservation:
        raise HTTPException(status_code=404, detail="Reservation not found")
    
    db.delete(reservation)
    db.commit()
    return