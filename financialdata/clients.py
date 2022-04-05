from sqlite3 import connect
from sqlalchemy import create_engine, engine

def get_mysql_financialdata_conn() -> engine.base.Connection:
    user = "root"
    password = "test"
    host = "localhost"
    port = "3306"
    database = "FinancialData"

    address = f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}"
    engine = create_engine(address)
    connect = engine.connect()
    
    return connect