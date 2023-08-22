from fastapi import FastAPI,Request,Body,Header
from fastapi.responses import HTMLResponse
from redis_om import get_redis_connection,HashModel,JsonModel,Migrator
import uvicorn
from typing import Annotated



redis = get_redis_connection(
    host="127.0.0.1",
    port=6379,
    db=0,
    decode_responses=True,

)

class teamname(HashModel):
    sk_team_name: str


    class Meta:
        database = redis
Migrator().run()
app=FastAPI()
@app.get('/skillup/challange',response_class=HTMLResponse)
def index():
    return "Congrats! you found me. now its time to recievd a new hint! you must send a Get request to another address to find the true authentication keys. this new route is a child of skillup in the last quest. the name cames after a joke.<br> <b>'What do you call a fake noodle?'</b> <br>the answer is the name."

@app.get('/skillup/impasta',response_class=HTMLResponse)
def impasta():
      return "Nice. finally someone understand my name!<br>finall step is here. send a post request to a grandchild of skillup called CyberSec and write this in the request body : <b>'{\"Sk_team_name\":\"YOURTEAMNAME\"}'</b> <br >be careful . you must replace the <b>YOURTEAMNAME</b> part with your team name. just choose one .<br>you must use <b>WeArePinkHats: False and Content-Type: application/json</b> in the header."

@app.post("/skillup/cybersec")
async def cybersec(body: teamname,request=Request,WeArePinkHats: str =Header(None)):
    validate=WeArePinkHats
    print(validate)
    if validate=='False':
        newteam=teamname(sk_team_name=body.sk_team_name)
        newteam.save()
        return newteam
    else: return "bad bad bad"
if __name__=="__main__":
       uvicorn.run("api:app",host="127.0.0.1",port=8000, reload=True)