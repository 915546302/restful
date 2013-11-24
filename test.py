from restful import Restful
#------------Test------------------
rest=Restful()
@rest.router('/wm/[a]?')
def test():
    a=rest.getAttribute('a')
    v=rest.query('u')
    if not v:
        v=''
    elif v is True:
        v='\"true\"'
    return '{\"test\":'+a+',\"value\":'+v+'}'

@rest.router('/vpc/[b]')
def test():
    attrB=rest.getAttribute('b')
    return '{\"vpc\":'+attrB+'}'

@rest.router('/post','POST')
def testPost():
    p=rest.query('p')
    v=rest.query('v')
    return '{\"q\":'+p+'\"v\":'+v+'}'
rest.run()