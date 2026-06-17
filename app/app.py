from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import os
from dotenv import load_dotenv
from fastapi import UploadFile, File, Form
from app.Schema import Postcreate
from Database.db import Collection
from datetime import datetime
import uuid
from imagekitio import ImageKit

load_dotenv()

imagekit = ImageKit(
    private_key=os.getenv("IMAGENET_PRIVATE_KEY")
)

app = FastAPI()

@app.get('/')
def home():
    return{"message":"Hello world"}


text_post = {
    1: "First Post",
    2: "Second Post",
    3: "Third Post"
}

@app.get('/posts')
def get_all_post():
    return text_post

@app.get('/posts/{id}')
def get_selected_post(id:int):
    try:
        return {
            "num":id,
            "text":text_post.get(id)
        }
    except KeyError:
        return {"error": "Post not found"}
    

@app.get('/putting')
def get_query(name:str,age:int):
    return{
        "name":name,
        "age":age
    }


@app.post("/posts")
def create_post(postm:Postcreate) -> Postcreate:
    new_post = {"title":postm.title , "content":postm.content}
    text_post[max(text_post.keys()) + 1] = new_post
    return new_post 


@app.get("/upload", response_class=HTMLResponse)
def upload_form():
    return """
    <form action="/upload" method="post" enctype="multipart/form-data">
        <input type="file" name="file" required>
        <input type="text" name="caption" placeholder="Caption" required>
        <button type="submit">Upload</button>
    </form>
    """


@app.post("/upload")
async def upload_post(
    file: UploadFile = File(...),
    caption: str = Form(...)
):

    file_bytes = await file.read()

    upload = imagekit.files.upload(
        file=file_bytes,
        file_name=file.filename
    )

    image_url = upload.url

    post_data = {
        "id": str(uuid.uuid4()),
        "caption": caption,
        "url": image_url,
        "file_name": file.filename,
        "file_type": file.content_type,
        "created_at": datetime.utcnow()
    }

    result = Collection.insert_one(post_data)

    post_data["_id"] = str(result.inserted_id)
    return post_data



from bson import ObjectId
from bson.errors import InvalidId


@app.get("/feed")
def get_feed():

    posts = list(
        Collection.find().sort("created_at", -1)
    )

    posts_data = []

    for post in posts:
        posts_data.append({
            "id": str(post["_id"]),
            "caption": post["caption"],
            "url": post["url"],
            "file_name": post["file_name"],
            "file_type": post["file_type"],
            "created_at": post["created_at"]
        })

    return {
        "posts": posts_data
    }

@app.delete("/posts/{post_id}")
def delete_post(post_id: str):
    try:
        object_id = ObjectId(post_id)
    except InvalidId:
        return {"success": False, "message": "Invalid post id"}

    result = Collection.delete_one({"_id": object_id})

    if result.deleted_count == 0:
        return {"success": False, "message": "Post not found"}

    return {"success": True, "message": "Post deleted"}

