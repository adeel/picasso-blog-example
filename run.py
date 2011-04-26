import pack
from blog.app import app

pack.adapters.serve_with_paste(app)