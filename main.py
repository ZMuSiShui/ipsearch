from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from src.searchIPIP import searchFromIPIP
from src.searchGeo import searchFromMaxmind

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

@app.post('/search/')
async def main(data: Data):
    ipdb = data.ipdb
    ipdata = data.ipdata
    if ipdb == "ipip":
        # search from ipip
        iplist = ipdata.split('\n')
        ipstr = searchFromIPIP(iplist)
        res = {
            "code": 200,
            "ipstr": ipstr
        }
        return res
    elif ipdb == "maxmind":
        # search from maxmind
        iplist = ipdata.split('\n')
        ipstr = searchFromMaxmind(iplist)
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


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app="main:app", host="0.0.0.0", port=8000)