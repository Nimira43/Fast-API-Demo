from fastapi import FastAPI

app = FastAPI()

@app.get('/hello')
def index():
  return {'message': 'Hello FastAPI!!!'}

@app.get('/blog/{id}')
def get_blog(id):
  return {'message': f'Blog with id {id}'}