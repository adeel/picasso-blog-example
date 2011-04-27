from blog.controllers import *
from blog import config

def login(req):
  return "auth/login", {}

def login_post(req):
  password = req["params"].get("password")
  if password and password == config.password:
    req["session"]["is_logged_in"] = True
    return redirect("/")
  else:
    req["flash"]["error"] = "Wrong password."
    return login(req)