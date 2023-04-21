from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.responses import FileResponse

some_file_path = "Template/page.html"
app = FastAPI()


@app.get("/")
async def main():
    return FileResponse(some_file_path)


#@app.get("/")
#async def root():
#    return {"message": "Hello World"}