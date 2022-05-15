from fastapi import FastAPI
from routers.employees.employee import router as employee_router
from routers.timesheets.timesheet import router as timesheet_router
from db.sqlite.database import engine_sqlite
from db.mysql.database import engine_mysql

import models.employee as employee_models
import models.timesheet as timesheet_models

import os

app = FastAPI()

employee_models.Base.metadata.create_all(bind=engine_sqlite)
timesheet_models.Base.metadata.create_all(bind=engine_mysql)

prefix = os.getenv("API_PREFIX", "")

app.include_router(router=employee_router, prefix="{prefix}employee".format(prefix=prefix))
app.include_router(router=timesheet_router, prefix="{prefix}timesheet".format(prefix=prefix))