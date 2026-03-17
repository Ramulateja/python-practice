#function is a reusability of a code without typing it again
def func():
    print("hi")
func()
func()
func()
#global variable and local variable
globalv=10
def function():
    global globalv
    globalv=11
    print(globalv)
function()