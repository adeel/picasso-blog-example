from picasso import *

from blog.controllers import auth
from blog.controllers import posts

auth_routes = setup_routes(
  GET("/login", auth.login),
  POST("/login", auth.login_post))

post_routes = setup_routes(
  GET("/", posts.index),
  GET("/new", posts.new),
  POST("/new", posts.save),
  GET("/posts/:hash", posts.view))

routes = setup_routes(
  auth_routes,
  post_routes,
  routing.not_found("<h1>Not Found</h1>"))

app = setup_app(routes, {"views": {"template_dir": "blog/views"}})