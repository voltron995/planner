from app import app
from app import views

app.add_url_rule('/', view_func=views.FrontendAppView.as_view('home'))
app.add_url_rule('/<path:path>', view_func=views.FrontendAppView.as_view('frontend_app'))
