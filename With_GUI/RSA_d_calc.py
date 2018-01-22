import sys, os, PyQt5
from PyQt5 import QtCore, uic, QtWidgets

if hasattr(sys, "_MEIPASS"):
    qtCreatorFile = os.path.join(sys._MEIPASS, "RSA_d_calc.ui")
    pyqt = os.path.dirname(PyQt5.__file__)
    QtWidgets.QApplication.addLibraryPath(os.path.join(pyqt, "plugins"))
    os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = sys._MEIPASS
else:
    qtCreatorFile = "RSA_d_calc.ui"

#qtCreatorFile = "RSA_d_calc.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

def gcd(a, b):
    # Return the GCD of a and b using Euclid's Algorithm
    while a != 0:
        a, b = b % a, a
    return b

def findModInverse(a, m):
    # Returns the modular inverse of a % m, which is
    # the number x such that a*x % m = 1

    if gcd(a, m) != 1:
        return None # no mod inverse if a & m aren't relatively prime

    # Calculate using the Extended Euclidean Algorithm:
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    while v3 != 0:
        q = u3 // v3 # // is the integer division operator
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % m

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.d_button.clicked.connect(self._calculate_d)

    def _calculate_d(self):
        try:
            e = int(self.e_field.text())
            p = int(self.p_field.text())
            q = int(self.q_field.text())

            d = findModInverse(e, (p - 1) * (q - 1))

        except Exception as ex:
            d = ex

        self.d_field.setText(str(d))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
