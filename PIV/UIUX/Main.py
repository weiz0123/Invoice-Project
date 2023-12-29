from Data_Management.User_Level_Management import User_Level_Management
"""
DETAILS:
为了成功的对接，我们先做一个实验，大概了解一下我计划的流程 （如果又跟好的建议，可以修改）
在这里，我们会对接 search box (UI 的部分)， 跟 target list (data 的部分）
如果你对 search box （QLineEdit) 不熟悉， 跳到 Note* 部分, 如果熟悉，直接往下看

在 main 里，有一个 ‘USER’， 它将会包含所有对数据读写以及更新的function
比如要得到一个含有所有公司名字的list i.e. ['companyI', 'companyII']
那么可以用 USER.display_compnay_name() 来获取该list

这个list将会是你的 'target_list' -> 如果对target_list不熟悉，看Note*





Note* ctrl c+v 一下code，跑跑看
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QLabel, QCompleter
from PyQt6.QtCore import Qt

class BlindSearchApp(QWidget):
    def __init__(self):
        super().__init__()
        self.target_list = ['apple', 'abandon','abnormal','orange']
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.search_input = QLineEdit(self)
        layout.addWidget(self.search_input)

        completer = QCompleter(self.target_list, self.search_input)
        completer.setCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)  # Set case sensitivity
        self.search_input.setCompleter(completer)

        self.result_label = QLabel("Suggested items will appear as you type", self)
        layout.addWidget(self.result_label)

        self.setLayout(layout)
        self.setWindowTitle("Blind Search App")

def run_app():
    app = QApplication(sys.argv)
    window = BlindSearchApp()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    run_app()

"""


def main():
  # make sure to change the path to match your test environemnt
  DEFAULT_PATH = "C:\\Users\\zhouw\\OneDrive\\Documents\\personal sci project\\vs\\ProjectIV\\Test_Resource\\company_test"
  USER: User_Level_Managment = User_Level_Management(DEFAULT_PATH)
  target_list = USER.display_company_name() # 可以去看看， User_Level_Managment 里面有哪些function




main()
