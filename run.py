# 首先你需要在引用的python文件内导入该对象所在的文件，也就是main_menu.py
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import Ui_demo  # 导入该对象所在文件
import ctypes
import sys
# 指定Ui_MainWindow 为main_menu文件下的Ui_MainWindow对象。
Ui_MainWindow = Ui_demo.Ui_Dialog


class CoperQt(QtWidgets.QMainWindow, Ui_MainWindow):  # 创建一个Qt对象
    # 这里的第一个变量是你该窗口的类型，第二个是该窗口对象。
    # 这里是主窗口类型。所以设置成当QtWidgets.QMainWindow。
    # 你的窗口是一个会话框时你需要设置成:QtWidgets.QDialog
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)  # 创建主界面对象
        Ui_MainWindow.__init__(self)  # 主界面对象初始化
        self.setupUi(self)  # 配置主界面对象


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():
    # 将要运行的代码加到这里
    if __name__ == "__main__":
        app = QtWidgets.QApplication(sys.argv)
        window = CoperQt()  # 创建QT对象
        window.show()  # QT对象显示
        sys.exit(app.exec_())
else:
    if sys.version_info[0] == 3:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
    else:  # in python2.x
        ctypes.windll.shell32.ShellExecuteW(None, u"runas", unicode(sys.executable), unicode(__file__), None, 1)

