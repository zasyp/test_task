from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Table
from schemas import TableCreate, TableResponse
from database import get_db


router = APIRouter(tags=["tables"])

@router.get("/tables", response_model=TableResponse)
def get_all_tables(db: Session = Depends(get_db)):
    return db.query(Table).all()

@router.post("/tables", response_model=TableCreate)
def create_new_table(table: TableCreate, db: Session = Depends(get_db)):
    """Создание нового столика"""
    db_table = Table(**table.dict())
    db.add(db_table)
    db.commit()
    db.refresh(db_table)
    return db_table

router.delete("/tables/{table_id}")
def delete_table(table_id: int, db: Session = Depends(get_db)):
    """Удаление столика"""
    table = db.query(Table).get(table_id)

    if not table:
        raise HTTPException(status_code=404, detail="Table not found")

    if table.reservations:
            raise HTTPException(
                status_code=400,
                detail="Cannot delete table with active reservations"
            )
        
    db.delete(table)
    db.commit()
    return