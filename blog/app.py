from picasso import *

import blog
from blog.controllers import auth
from blog.controllers import posts

main_routes = setup_routes(
  GET("/", posts.index),
  GET("/posts/:hash", posts.view),
  GET("/login", auth.login),
  POST("/login", auth.login_post))

admin_routes = blog.middleware.wrap_requiring_login(
  setup_routes(
    GET("/new", posts.new),
    POST("/new", posts.save)))

routes = setup_routes(
  main_routes,
  admin_routes,
  routing.not_found("<h1>Not Found</h1>"))

app = setup_app(routes, {"views": {"template_dir": "blog/views"}})