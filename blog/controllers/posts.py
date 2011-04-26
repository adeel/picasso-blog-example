from blog.controllers import *

def index(req):
  posts = db.posts.find(sort=[("date", -1)])
  return "posts/index", {"posts": posts}

def new(req, post={}):
  return "posts/form", {"post": post}

def save(req):
  post = req["params"].get("post", {})
  if not models.post.is_valid(post):
    req["flash"]["error"] = "Invalid post."
    return new(req, post)

  models.post.new(post)

  req["flash"]["notice"] = "The post has been inserted."
  return redirect("/")

def view(req, hash):
  post = db.posts.find_one({"hash": hash})
  if post:
    return "posts/view", {"post": post}