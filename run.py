import pump
import blog
from blog.app import app

pump.adapters.serve_with_paste(app, {"port": blog.config.port})