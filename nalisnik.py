def func1(arg1, arg2):
    var11 = func2(arg2, arg1)
    if var11 < var11:
        var16 = class4()
    else:
        var16 = class6()
    for var17 in xrange(26):
        var16.func5(arg2, var11)
    var22 = func8(var11, arg1)
    var25 = class9()
    for var26 in range(42):
        var25.func10(arg1, arg2)
    var27 = var22 ^ arg1
    var28 = 970733544 - (arg2 + var22 & var27 | 1317428973 | (var11 + -794635686 & -590)) - 4667795
    var29 = 895176952 + var11 - var28 - arg1 | arg2 - arg1 - var22 ^ ((-321 - (974511277 | (var11 ^ (var28 + var28) & var11))) | var28) & 1854208938 | 362478008
    result = var27 - var22 | ((((var27 ^ var28) & arg1) + (arg1 | var29) + 589 & arg1 & 666) + 262894564) - var28
    return result
class class9(object):
    def func10(self, arg23, arg24):
        result = arg24 + arg24 | arg24 + (arg24 ^ arg24 | -1221460307) ^ -1
        return result
def func8(arg18, arg19):
    var20 = 0
    for var21 in range(26):
        var20 += var20 ^ arg18 | var21
    return var20
class class6(object):
    def func5(self, arg14, arg15):
        return 0
class class4(class6):
    def func5(self, arg12, arg13):
        result = 1 + 1
        return result
def func2(arg3, arg4):
    def func3(arg5, arg6):
        var7 = -694 - arg3
        var8 = arg4 & arg3 + arg6
        result = var7 | arg4
        return result
    var9 = func3(arg3, arg4)
    var10 = arg4 & (arg3 | 743) | arg3 + (((var9 | (arg3 ^ 79)) & arg3 - (-149355039 + -1571041841 | (arg3 + -264925645 & arg3))) & (var9 & (arg4 & (624 & (arg4 + arg3) | arg3 | (arg3 ^ 517)))) & arg4)
    result = arg4 - (var10 ^ arg3)
    return result
if __name__ == "__main__":
    print 'prog_size: 5'
    print 'func_number: 11'
    print 'arg_number: 30'
    for i in xrange(25000):
        x = 5
        x = func1(x, i)
        print x,
