from fastapi import FastAPI, Body

import os
import imghdr
from PIL import Image
import base64
import io

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.post("/img_to_base64")
async def image_to_base64(body: dict = Body(...)):
    path: str = body.get('path')
    if path and os.path.exists(path) and os.path.isfile(path):
        _, file_extension = os.path.splitext(path)
        image_extensions = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp'}
        if file_extension.lower() not in image_extensions:
            raise Exception('not a image file')
        with Image.open(path) as image:
            # 创建一个字节流
            buffered = io.BytesIO()
            # 将图片保存到字节流
            image.save(buffered, format='PNG')  # 可以根据需要更改格式
            # 获取字节流的内容并编码为 Base64
            img_str = base64.b64encode(buffered.getvalue()).decode('utf-8')
        return img_str
    else:
        raise Exception('not a valid file path')
