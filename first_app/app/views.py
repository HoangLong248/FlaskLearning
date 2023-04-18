from flask_appbuilder import AppBuilder, expose, BaseView, has_access
from app import appbuilder
from flask import render_template

class MyView(BaseView):
    default_view = "method1"
    
    @expose('/method1/')
    @has_access
    def method1(self):
        # do something with param1
        # and return it
        return "Hello"

    @expose('/method2/<string:param1>')
    @has_access
    def method2(self, param1):
        # do something with param1
        # and return it
        param1 = "Goodbyte %s" % (param1)
        return param1
    
    @expose('/method3/<string:param1>')
    @has_access
    def method3(self, param1):
        param1 = "Goodbye %s" % (param1)
        self.update_redirect()
        
        return render_template('method3.html', param1=param1)
    
appbuilder.add_view(MyView, "Method1", category='My View')
appbuilder.add_link('Method2', href="/myview/method2/john", category="My View")
appbuilder.add_link('Method3', href="/myview/method3/john", category="My View")