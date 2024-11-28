import uvicorn

if __name__ == "__main__":
    # Point to the `main.py` file inside the `src` folder
    uvicorn.run("src.main:app", host="0.0.0.0", port=8000, reload=True)