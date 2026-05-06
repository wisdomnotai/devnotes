#Importing dependencies
from fastapi import FastAPI

app = FastAPI()


#create posts
@app.post("/post")
def create_post():
    return {"message":"successful"}

#view all posts
@app.get("/posts")
def view_posts_all():
    return {"data":"data here"}

#view post by title
@app.get("/posts/{title}")
def view_posts_title():
    return {"data": "ypu"}

#view posts by tag
@app.get("/posts/{tag}")
def view_posts_tag():
    return {"data","taghe"}