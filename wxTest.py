import wx
import gui as wxFormBuilderTest
import tkinter as tk

class TransformFrame(wxFormBuilderTest.MainFrame):
    def __init__(self, parent):
        wxFormBuilderTest.MainFrame.__init__(self, None)
    
    def TransformFile(self, event):
        print("It's alive!")
        location = self.DirPicker.GetPath()
        print(location)

if __name__ == "__main__":
    app = wx.App(False)
    frame = TransformFrame(None)
    frame.Show(True)
    app.MainLoop()
