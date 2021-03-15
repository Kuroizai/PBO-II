# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 800,420 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.Size( 800,420 ), wx.Size( -1,-1 ) )
		self.SetFont( wx.Font( 12, 74, 90, 90, False, "Berlin Sans FB" ) )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		
		main_sizer = wx.BoxSizer( wx.VERTICAL )
		
		main_sizer.SetMinSize( wx.Size( -1,1 ) ) 
		self.Spacer = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.Spacer.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
		self.Spacer.SetMinSize( wx.Size( 800,1 ) )
		self.Spacer.SetMaxSize( wx.Size( -1,1 ) )
		
		main_sizer.Add( self.Spacer, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.NamePanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.NamePanel.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
		self.NamePanel.SetMinSize( wx.Size( 800,-1 ) )
		
		name_sizer = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText1 = wx.StaticText( self.NamePanel, wx.ID_ANY, u"Adwitya Sadhu Prayastita", wx.Point( 100,100 ), wx.Size( -1,-1 ), wx.ALIGN_CENTRE )
		self.m_staticText1.Wrap( -1 )
		self.m_staticText1.SetFont( wx.Font( 12, 74, 90, 90, False, "Arial Rounded MT Bold" ) )
		self.m_staticText1.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		
		name_sizer.Add( self.m_staticText1, 0, wx.EXPAND|wx.ALL, 5 )
		
		
		self.NamePanel.SetSizer( name_sizer )
		self.NamePanel.Layout()
		name_sizer.Fit( self.NamePanel )
		main_sizer.Add( self.NamePanel, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.Nim_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.Nim_panel.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
		self.Nim_panel.SetMinSize( wx.Size( 800,-1 ) )
		
		nim_sizer = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText11 = wx.StaticText( self.Nim_panel, wx.ID_ANY, u"192410101054", wx.Point( 100,100 ), wx.Size( -1,-1 ), wx.ALIGN_CENTRE )
		self.m_staticText11.Wrap( -1 )
		self.m_staticText11.SetFont( wx.Font( 12, 74, 90, 90, False, "Arial Rounded MT Bold" ) )
		
		nim_sizer.Add( self.m_staticText11, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		self.Nim_panel.SetSizer( nim_sizer )
		self.Nim_panel.Layout()
		nim_sizer.Fit( self.Nim_panel )
		main_sizer.Add( self.Nim_panel, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.Spacer1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.Spacer1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
		self.Spacer1.SetMinSize( wx.Size( 800,1 ) )
		self.Spacer1.SetMaxSize( wx.Size( 800,1 ) )
		
		main_sizer.Add( self.Spacer1, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.HelloPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.HelloPanel.SetMinSize( wx.Size( 800,-1 ) )
		
		gSizer2 = wx.GridSizer( 0, 5, 10, 50 )
		
		self.m_staticText5 = wx.StaticText( self.HelloPanel, wx.ID_ANY, u"H", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )
		self.m_staticText5.SetFont( wx.Font( 48, 74, 90, 90, False, "Arial Rounded MT Bold" ) )
		self.m_staticText5.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		
		gSizer2.Add( self.m_staticText5, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText51 = wx.StaticText( self.HelloPanel, wx.ID_ANY, u"E", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText51.Wrap( -1 )
		self.m_staticText51.SetFont( wx.Font( 48, 74, 90, 90, False, "Arial Rounded MT Bold" ) )
		self.m_staticText51.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		
		gSizer2.Add( self.m_staticText51, 0, wx.ALL, 5 )
		
		self.m_staticText52 = wx.StaticText( self.HelloPanel, wx.ID_ANY, u"L", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText52.Wrap( -1 )
		self.m_staticText52.SetFont( wx.Font( 48, 74, 90, 90, False, "Arial Rounded MT Bold" ) )
		self.m_staticText52.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		
		gSizer2.Add( self.m_staticText52, 0, wx.ALL, 5 )
		
		self.m_staticText521 = wx.StaticText( self.HelloPanel, wx.ID_ANY, u"L", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText521.Wrap( -1 )
		self.m_staticText521.SetFont( wx.Font( 48, 74, 90, 90, False, "Arial Rounded MT Bold" ) )
		self.m_staticText521.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		
		gSizer2.Add( self.m_staticText521, 0, wx.ALL, 5 )
		
		self.m_staticText5211 = wx.StaticText( self.HelloPanel, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5211.Wrap( -1 )
		self.m_staticText5211.SetFont( wx.Font( 48, 74, 90, 90, False, "Arial Rounded MT Bold" ) )
		self.m_staticText5211.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		
		gSizer2.Add( self.m_staticText5211, 0, wx.ALL, 5 )
		
		self.m_staticText52111 = wx.StaticText( self.HelloPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText52111.Wrap( -1 )
		self.m_staticText52111.SetFont( wx.Font( 48, 74, 90, 90, False, "Arial Rounded MT Bold" ) )
		self.m_staticText52111.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		
		gSizer2.Add( self.m_staticText52111, 0, wx.ALL, 5 )
		
		self.m_staticText52112 = wx.StaticText( self.HelloPanel, wx.ID_ANY, u"W", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText52112.Wrap( -1 )
		self.m_staticText52112.SetFont( wx.Font( 48, 74, 90, 90, False, "Arial Rounded MT Bold" ) )
		self.m_staticText52112.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		
		gSizer2.Add( self.m_staticText52112, 0, wx.ALL, 5 )
		
		self.m_staticText52113 = wx.StaticText( self.HelloPanel, wx.ID_ANY, u"X", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText52113.Wrap( -1 )
		self.m_staticText52113.SetFont( wx.Font( 48, 74, 90, 90, False, "Arial Rounded MT Bold" ) )
		self.m_staticText52113.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		
		gSizer2.Add( self.m_staticText52113, 0, wx.ALL, 5 )
		
		self.m_staticText52114 = wx.StaticText( self.HelloPanel, wx.ID_ANY, u"!", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText52114.Wrap( -1 )
		self.m_staticText52114.SetFont( wx.Font( 48, 74, 90, 90, False, "Arial Rounded MT Bold" ) )
		self.m_staticText52114.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		
		gSizer2.Add( self.m_staticText52114, 0, wx.ALL, 5 )
		
		self.m_staticText52115 = wx.StaticText( self.HelloPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText52115.Wrap( -1 )
		self.m_staticText52115.SetFont( wx.Font( 48, 74, 90, 90, False, "Arial Rounded MT Bold" ) )
		self.m_staticText52115.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		
		gSizer2.Add( self.m_staticText52115, 0, wx.ALL, 5 )
		
		
		self.HelloPanel.SetSizer( gSizer2 )
		self.HelloPanel.Layout()
		gSizer2.Fit( self.HelloPanel )
		main_sizer.Add( self.HelloPanel, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.m_panel8 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel8.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DDKSHADOW ) )
		self.m_panel8.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.m_panel8.SetMinSize( wx.Size( 0,0 ) )
		self.m_panel8.SetMaxSize( wx.Size( 800,30 ) )
		
		main_sizer.Add( self.m_panel8, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.SetSizer( main_sizer )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.MyFrame1OnClose )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def MyFrame1OnClose( self, event ):
		event.Skip()
	

