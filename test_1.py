import unittest
class Order_test(unittest.TestCase):
    def __init__(self,method,order,orderd):
        super().__init__(method)
        self.order=order
        self.orderd=orderd
    def test_Order(self):
        try:
            self.assertNotIn(self.order,self.orderd)
        except:
            print('命令错误')
        else:
            print('命令正确')
class Context_test(unittest.TestCase):
    def __init__(self,method,type,typed):
        super().__init__(method)
        self.type=type
        self.typed=typed
    def test_Context(self):
        try:
            self.assertEqual(self.type, self.typed)
        except AssertionError as e:
            print('文件目录正确')
        else:
            print('文件目录错误')
order=input('请输入您的命令：')
r=unittest.TestSuite()
r.addTest(Order_test('test_Order',order,['wc.exe -c,\file.txt','wc.exe -w,\file.txt','wc.exe -l,\file.txt','wc.exe -z,\file.txt','wc.exe -k,\file.txt']))
type=input('请输入文件的目录及名称：')
try:
    f=open(type,'r',encoding="utf-8")
except FileNotFoundError as e:
    type='FileNotFoundError'
r.addTest(Context_test('test_Context',type,'FileNotFoundError'))
R=unittest.TextTestRunner()
R.run(r)