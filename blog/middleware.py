from pump.util.response import redirect

def wrap_requiring_login(app):
  def wrapped(request):
    if request["session"].get("is_logged_in"):
      return app(request)
    else:
      return redirect("/login")
  return wrapped