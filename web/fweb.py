import falcon


class HomeResource:

    def on_get(self, request, response):
        response.body = "Home"


app = falcon.API()
app.add_route('/', HomeResource())
