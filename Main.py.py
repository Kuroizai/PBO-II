import wx
import MenghelloWxGui as mywx


app = wx.App()
frame = mywx.MyFrame1(None)
frame.Show()
app.MainLoop()