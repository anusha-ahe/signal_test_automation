rightClick(Pattern("1727620298733.png").similar(0.81))
type('H')
wait(2)
type('1')
wait(2)

if exists(Pattern("1727620639651.png").similar(0.97)):
    rightClick("S28_R.png")
    type('H')
    type(Key.RIGHT)
    type(Key.ENTER)
    wait(5)
    if exists(Pattern("S28_Y.png").exact()):
                print("S28 PASS ROUTE NOT SET")
                rightClick("S28_Y.png")
                type('H')
                type('C')
                wait(2)
                rightClick("S28_R.png")
                type('H')
                type('E')
                wait(2)
                
    else:
                print("fail") 
else:
                print("fail") 
if exists("S26_Y.png"):
    rightClick("S24_R.png")
    type('H')
    type(Key.RIGHT)
    type(Key.DOWN)
    type(Key.DOWN)
    type(Key.DOWN)
    type(Key.ENTER)
    wait(5)
    if exists(Pattern("S24_Y.png").exact().targetOffset(-24,-5)):
                print("FAIL")
                rightClick("S24_Y.png")
                type('H')
                type('C')
                wait(2)
                rightClick("S24__R.png")
                type('H')
                type('E')
                wait(2)
                
    else:
                print("S24 PASS ROUTE NOT SET") 
else:
                print("PASS") 
if exists("S26_Y.png"):
    rightClick(Pattern("SH218_R.png").exact())
    type('D')
    type(Key.ENTER)
    wait(5)
    if exists(Pattern("SH218_Y.png").exact()):
                print("FAIL")
                rightClick(Pattern("SH218_Y.png").exact())
                type('D')
                type('C')
                wait(2)
                rightClick(Pattern("SH218_R.png").exact())
                type('D')
                type('E')
                wait(2)
                
    else:
                print("SH218 PASS ROUTE NOT SET") 
else:
                print("PASS") 