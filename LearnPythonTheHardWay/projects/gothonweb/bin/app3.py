import web

urls={
    '/caculate','test'
}

app=web.application(urls,globals())

render=web.template.render('templates/')

class test(object):

    def GET(self):
        return render.caculating()

    def POST(self):
        form=web.input(a="0",b="0")
        total="%s , %s" (form.a,form.b)
        return render.index(greeting=total)

if __name__=="__main__":
    app.run()
        

