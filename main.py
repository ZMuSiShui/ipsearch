from fastapi import FastAPI, Request
from starlette.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates

from src.searchIPIP import searchFromIPIP
from src.searchGeo import searchFromMaxmind
from src.searchQQZeng import searchFromQQZeng
from src.seaechCZ88 import searchFromCZ88

app = FastAPI()
BACKEND_CORS_ORIGINS = ["*"]
templates = Jinja2Templates(directory="templates")

app.add_middleware(CORSMiddleware,
                   allow_origins=[str(origin) for origin in BACKEND_CORS_ORIGINS],
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"],
                   expose_headers=["Content-Disposition"]
                   )

class Data(BaseModel):
    ipdb: str
    ipdata: str

@app.post('/search/')
async def main(data: Data):
    ipdb = data.ipdb
    ipdata = data.ipdata
    if ipdb == "ipip":
        # search from ipip
        iplist = ipdata.strip().split('\n')
        ipstr = searchFromIPIP(iplist)
        res = {
            "code": 200,
            "ipstr": ipstr
        }
        return res
    elif ipdb == "maxmind":
        # search from maxmind
        iplist = ipdata.strip().split('\n')
        ipstr = searchFromMaxmind(iplist)
        res = {
            "code": 200,
            "ipstr": ipstr
        }

        return res

    elif ipdb == "qqzeng":
        # search from maxmind
        iplist = ipdata.strip().split('\n')
        ipstr = searchFromQQZeng(iplist)
        res = {
            "code": 200,
            "ipstr": ipstr
        }

        return res
    
    elif ipdb == "cz88":
        # search from maxmind
        iplist = ipdata.strip().split('\n')
        ipstr = searchFromCZ88(iplist)
        res = {
            "code": 200,
            "ipstr": ipstr
        }

        return res

    else:
        res = {
            "code": 400,
            "msg": "Not Support The Current Query Method"
        }
        return res
@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app="main:app", host="0.0.0.0", port=8000)