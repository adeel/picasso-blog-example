import hashlib
import datetime

from blog.models import db

def get_hash(post):
  return hashlib.sha1(repr(post)).hexdigest()

def new(post):
  post["date"] = datetime.datetime.now()
  post["hash"] = get_hash(post)
  return db.posts.insert(post)

def is_valid(post):
  return (post and _is_title_valid(post.get("title", ''))
               and _is_body_valid(post.get("body", '')))

def _is_title_valid(title):
  return title.strip() != ""

def _is_body_valid(body):
  return body.strip() != ""