import wx
import MenghelloWxGui as mywx

if __name__ == '__main__':
    app = wx.App()
    frame = mywx.MyFrame1(None)
    frame.Show()
    app.MainLoop()