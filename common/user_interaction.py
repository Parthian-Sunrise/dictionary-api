from PyQt5.QtWidgets import QApplication, QInputDialog

app = QApplication([])
text, ok = QInputDialog.getText(None, "Input", "What's your name?:")
if ok:
    if text=="Matthew":
        text, ok = QInputDialog.getText(None, "Input", "Smelly boy:")
    else:
        text, ok = QInputDialog.getText(None, "Input", "Good, Matthew's not here!:")
