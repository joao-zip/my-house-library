from fastapi import FastAPI


app = FastAPI()


@app.get('/')
def test_running():
    return {"message": "It's running!"}
