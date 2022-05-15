from os import execvpe
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.timesheet import Timesheet as TimesheetSchema
from models.timesheet import Timesheet as TimesheetModel
from models.employee import Employee as EmployeeModel
from db.mysql.database import SessionLocal as SessionLocal_mysql
from db.sqlite.database import SessionLocal as SessionLocal_sqlite
from datetime import datetime

router = APIRouter()

def get_db_mysql() -> Session:
    """
    Complete the full cycle of a db session (open, close).
    """
    try:
        db = SessionLocal_mysql()
        yield db
    finally:
        db.close()

def get_db_sqlite() -> Session:
    """
    Complete the full cycle of a db session (open, close).
    """
    try:
        db = SessionLocal_sqlite()
        yield db
    finally:
        db.close()

@router.get("/all", tags=["timesheet"], status_code=200)
async def get_all_timesheets(db: Session = Depends(get_db_mysql)):
    """
    Get all timesheets.
    """
    try:
        timesheets = db.query(TimesheetModel).all()
        return timesheets
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post('/add/', tags=["timesheet"], status_code=201)
async def add_timesheet_entry(emp_id: str, timesheet: TimesheetSchema, db_mysql: Session = Depends(get_db_mysql), db_sqlite: Session = Depends(get_db_sqlite)):
    """
    Add a new timesheet entry.
    """
    try:
        employee_ = db_sqlite.query(EmployeeModel).filter(EmployeeModel.id == emp_id).first()
        if not employee_:
            raise HTTPException(status_code=404, detail="Employee not found")
        else:
            timesheet = TimesheetModel(
                id = timesheet.id,
                employee_id = employee_.id,
                employee_name = employee_.first_name + " " + employee_.surname,
                date = datetime.now(),
                hours = timesheet.hours,
                description = timesheet.description
            )
            if db_mysql.query(TimesheetModel).filter(TimesheetModel.id == timesheet.id).first():
                raise HTTPException(status_code=400, detail="Timesheet id already exists")
            else:
                db_mysql.add(timesheet)

    except ValueError as e:
        db_mysql.rollback()
        raise HTTPException(status_code=400, detail=str(e)) 

    else:
        db_mysql.commit()
        return db_mysql.query(TimesheetModel).filter(TimesheetModel.id == timesheet.id).first()
