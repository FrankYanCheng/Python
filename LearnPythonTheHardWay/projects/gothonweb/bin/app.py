import web

urls = (
    '/', 'Index'
)

app = web.application(urls, globals())
render=web.template.render('templates/')
#renders=web.template.render('templates/test.html')
class Index:
    def GET(self):
        test = "Hello World"
        return render.index(greeting=test)
class Test:
    def GET(self):
        hw="Hello"
        return render.test(test=hw)
if __name__ == "__main__":
   app.run()
