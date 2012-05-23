from gunicorn import config

from gunicorn.app.base import Application


def run_app(app, address="127.0.0.1:8000"):
    '''
    run the passed wsgi-application inside gunicorn
    '''
    class App(Application):
        def init(self, parser, opt, args):
            #self.cfg.set('worker_class', 'ggevent')
            self.cfg.set('bind', address)
        
        def load(self):
            return app
    
    App().run()


if __name__ == '__main__':

    def hello_wsgi(environ, start_response):
        start_response('200 OK', [('Content-Type', 'text/plain')])
        yield 'Hello World\n'
    
    run_app(hello_wsgi, "0.0.0.0:8888")
