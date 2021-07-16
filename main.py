import time

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from src.searchIPIP import searchFromIPIP
from src.searchGeo import searchFromMaxmind
from src.searchQQZeng import searchFromQQZeng
from src.searchCZ88 import searchFromCZ88

app = FastAPI()
BACKEND_CORS_ORIGINS = ["*"]

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


@app.post('/search')
async def main(data: Data):
    ipdb = data.ipdb
    ipdata = data.ipdata
    if ipdb == "ipip":
        # search from ipip
        start_time = time.time()
        iplist = ipdata.strip().split('\n')
        ipstr = searchFromIPIP(iplist)
        end_time = time.time()
        res = {
            "code": 200,
            "ipstr": ipstr,
            "time": end_time - start_time
        }
        return res
    elif ipdb == "maxmind":
        # search from maxmind
        start_time = time.time()
        iplist = ipdata.strip().split('\n')
        ipstr = searchFromMaxmind(iplist)
        end_time = time.time()
        res = {
            "code": 200,
            "ipstr": ipstr,
            "time": end_time - start_time
        }

        return res

    elif ipdb == "qqzeng":
        # search from maxmind
        start_time = time.time()
        iplist = ipdata.strip().split('\n')
        ipstr = searchFromQQZeng(iplist)
        end_time = time.time()
        res = {
            "code": 200,
            "ipstr": ipstr,
            "time": end_time - start_time
        }

        return res

    elif ipdb == "cz88":
        # search from maxmind
        start_time = time.time()
        iplist = ipdata.strip().split('\n')
        ipstr = searchFromCZ88(iplist)
        end_time = time.time()
        res = {
            "code": 200,
            "ipstr": ipstr,
            "time": end_time - start_time
        }

        return res

    else:
        res = {
            "code": 400,
            "msg": "Not Support The Current Query Method"
        }
        return res


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app="main:app", host="0.0.0.0", port=8000)
