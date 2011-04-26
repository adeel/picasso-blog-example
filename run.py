import pack
import blog
from blog.app import app

pack.adapters.serve_with_paste(app, {"port": blog.config.port})