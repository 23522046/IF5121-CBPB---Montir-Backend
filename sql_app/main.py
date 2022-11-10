import uvicorn
from sql_app.v1.endpoints import *

if __name__ == "__main__":
    uvicorn.run('core:app', host="0.0.0.0",port=8000,log_level="debug",reload=True)