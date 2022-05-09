
from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel #membuat request body
from uvicorn
#aaaaa
app = FastAPI()


#path operation decoration
#harus ada path ('/')/endpoint/routh
#method/operation = get
@app.get('/blog')
#path operation function
def index(limit = 10, published: bool = True, sort: Optional[str]= None):
    #return published #ini dihilangkan kalau mau menjalankan kode sampai bawah
    if published:
        return {'data': f'{limit} published blogs from the db'}
    else:
        return {'data': f'{limit} blogs from the db'}
    


@app.get('/blog/unpublished')
def unpublished():
    return {'data': 'all unpublished blogs'} #dictionary



#page selanjutnya
@app.get('/blog/{id}')
def show(id: int):
    #fetch blog with id = id
    return {'data': id}



@app.get('/blog/{id}/comments')
def comments(id, limit=10):
    #fetch comments of blog with id = id
    return {'data': {'1','2'}}


#untuk menjelaskan kelas yg berdasarkan pydantic model
class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]



#create data
@app.post('/blog')
def create_blog(request : Blog):
    return{'data': f"Blog is created with title as {request.title}"}


#untuk ganti port
#if __name__ = "__main__":
#    uvicorn.run(app, host:"127.0.0.1", port= 9000)