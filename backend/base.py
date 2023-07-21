from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


class Base:
    def __init__(self, name):
        self.name = name

    @app.get('/api/name')
    def get(self, name):
        pass

    @app.post('/api/name')
    def post(self, name):
        pass

    @app.put('/api/name')
    def put(self, name):
        pass

    @app.delete('/api/name')
    def delete(self, name):
        pass

