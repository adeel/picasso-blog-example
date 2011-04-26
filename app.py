from picasso import *

from controllers import posts

routes = setup_routes(
  GET("/", posts.index),
  routing.not_found("<h1>Not Found</h1>"))

app = setup_app(routes, {"views": {"template_dir": "views"}})
pack.adapters.serve_with_paste(app)