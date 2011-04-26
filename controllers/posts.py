from picasso import *

def index(req):
  posts = [
    {"title": "First post", "body": "Hi everyone"}]
  return "posts/index", {"posts": posts}