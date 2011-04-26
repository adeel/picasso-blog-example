from picasso import *

from blog.controllers import posts

routes = setup_routes(
  GET("/", posts.index),
  GET("/new", posts.new),
  POST("/new", posts.save),
  GET("/posts/:hash", posts.view),
  routing.not_found("<h1>Not Found</h1>"))

app = setup_app(routes, {"views": {"template_dir": "blog/views"}})