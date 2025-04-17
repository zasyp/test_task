from sqlalchemy import or_, and_
from datetime import timedelta
from models import Reservation


def has_time_conflict(session, table_id, new_start, new_duration):
    new_end = new_start + timedelta(minutes=new_duration)
    
    conflict_condition = or_(
        and_(
            Reservation.reservation_time <= new_start,
            Reservation.reservation_time + func.make_interval(0, 0, 0, 0, 0, Reservation.duration_minutes, 0) > new_start
        ),
        and_(
            Reservation.reservation_time < new_end,
            Reservation.reservation_time + func.make_interval(0, 0, 0, 0, 0, Reservation.duration_minutes, 0) >= new_end
        )
    )
    
    return session.query(Reservation).filter(
        Reservation.table_id == table_id,
        conflict_condition
    ).count() > 0