def func1(arg1, arg2):
    var5 = class2()
    for var6 in [3 | -2 for i in (i & (-1 + ((-6 & i) & 9 ^ -2)) for i in ((5 ^ arg1) | i for i in range(19)))]:
        var7 = var5.func3
        var7(var6, arg1)
    var11 = func4(arg2, arg1)
    var12 = ((501992827 & -1521264496) | -834227090 + 286) - -1266670300
    if var11 < arg1:
        var13 = var11 & arg2 ^ arg2 - (((1739534437 | var11) + ((-141 | (arg1 ^ arg2 + var11)) | (-799440823 + var11) | (arg1 | (var12 + (var11 + (1223749656 + arg2))) + 688))) - ((arg2 ^ arg2) ^ 315))
    else:
        var13 = 1091159145 - var12 + arg2
    result = arg2 & (arg2 & arg2)
    return result
class class2(object):
    def func3(self, arg3, arg4):
        return 0
def func4(arg8, arg9):
    closure = [0]
    def func5(acc, rest):
        var10 = closure[0] - (((-10 + -10 + acc) | -10) + -4 - -4)
        closure[0] += var10
        if acc == 0:
            return var10
        else:
            result = func5(acc - 1, var10)
            return result
    result = func5(10, 0)
    return result
if __name__ == "__main__":
    print 'prog_size: 5'
    print 'func_number: 6'
    print 'arg_number: 14'
    for i in xrange(25000):
        x = 5
        x = func1(x, i)
        print x,
