rightClick(Pattern("1727620298733.png").similar(0.81))
type('H')
wait(2)
type('1')
wait(2)

if exists(Pattern("1727620639651.png").similar(0.97)):
    rightClick("S28R.png")
    type('H')
    type(Key.RIGHT)
    type(Key.ENTER)
    wait(5)
    if exists(Pattern("S28Y.png").exact()):
                print("S28 PASS ROUTE NOT SET")
                rightClick("S28Y.png")
                type('H')
                type('C')
                wait(2)
                rightClick("S28R.png")
                type('H')
                type('E')
                wait(2)
                
    else:
                print("fail") 
else:
                print("fail") 
if exists("S26Y.png"):
    rightClick("S24R.png")
    type('H')
    type(Key.RIGHT)
    type(Key.DOWN)
    type(Key.DOWN)
    type(Key.DOWN)
    type(Key.ENTER)
    wait(5)
    if exists(Pattern("S24Y.png").exact().targetOffset(-24,-5)):
                print("FAIL")
                rightClick("S24Y.png")
                type('H')
                type('C')
                wait(2)
                rightClick("S24R.png")
                type('H')
                type('E')
                wait(2)
                
    else:
                print("S24 PASS ROUTE NOT SET") 
else:
                print("PASS") 
if exists("S26Y.png"):
    rightClick(Pattern("SH218R.png").exact())
    type('D')
    type(Key.ENTER)
    wait(5)
    if exists(Pattern("SH218Y.png").exact()):
                print("FAIL")
                rightClick(Pattern("SH218Y.png").exact())
                type('D')
                type('C')
                wait(2)
                rightClick(Pattern("SH218R.png").exact())
                type('D')
                type('E')
                wait(2)
                
    else:
                print("SH218 PASS ROUTE NOT SET") 
else:
                print("PASS") 