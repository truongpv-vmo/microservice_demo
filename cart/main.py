from fastapi import FastAPI
 
app = FastAPI()
 
@app.get("/")
def root ():
  return {"message": "Hello World!"}

 
@app.get("/list")
def root ():
  return [{"message": "Hello World!"}]


 
@app.get("/add")
def root ():
  return {"message": "Hello World!"}

 
@app.get("/remove")
def root ():
  return {"message": "Hello World!"}