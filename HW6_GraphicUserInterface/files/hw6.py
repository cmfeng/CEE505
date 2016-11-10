'''
Changming Feng
Student #:1568037
UW ID:cmf927
'''

import wx
import Graph

class MyAppWindow(wx.Frame):
    '''
    This is an application to find the shortes path between chosen airports
    '''


    def __init__(self, title='Flight Search'):
        '''
        Constructor
        '''
        #import the database
        
        wx.Frame.__init__(self, None, 100, title, size=(640,480))
        #caution on the Graph.Graph! need the first Graph to import from the Graph file
        self.database = Graph.Graph('Graph.db')
        
        #set menu bar
        filemenu = wx.Menu()
        filemenu.Append(200,"&Quit","Quit the Application")
        filemenu.Append(201, "&About", "About the Application")
        
        menubar = wx.MenuBar()
        menubar.Append(filemenu,"&File")
        self.SetMenuBar(menubar)
        
        #populate both ComboBoxes
        l=self.database.getAirportCodes()
        
        self.cmb1 = wx.ComboBox(self, 10,  choices=l)
        self.cmb2 = wx.ComboBox(self, 20,  choices=l)
        
        #text before combobox
        self.txt1=wx.StaticText(self, 21, label='Departure: ')
        self.txt2=wx.StaticText(self, 22, label='Destination: ')
        #textctrl
        self.text=wx.TextCtrl(self, 30, style=wx.TE_READONLY|wx.TE_MULTILINE)
        #button
        self.button1 = wx.Button(self, 40, label='search')
        self.button2 = wx.Button(self, 50, label='Reset View')
        
        # sizers for all 
        #sizer for the first line
        hsizer1 = wx.BoxSizer(wx.HORIZONTAL)
        hsizer1.Add(self.txt1, 1, wx.ALIGN_CENTER)
        hsizer1.Add(self.cmb1, 1, wx.ALIGN_CENTER)
        #sizer for the second line
        hsizer2 = wx.BoxSizer(wx.HORIZONTAL)
        hsizer2.Add(self.txt2, 1, wx.ALIGN_CENTER)
        hsizer2.Add(self.cmb2, 1, wx.ALIGN_CENTER)
        #sizer for the third line
        hsizer3 = wx.BoxSizer(wx.HORIZONTAL)
        hsizer3.Add(self.button1, 1, wx.ALIGN_CENTER)
        #sizer for the forth line
        hsizer4=wx.BoxSizer(wx.HORIZONTAL)
        hsizer4.Add(self.text, 1, wx.EXPAND)
        #sizer for the fifth line
        hsizer5=wx.BoxSizer(wx.HORIZONTAL)
        hsizer5.Add(self.button2, 1, wx.ALIGN_CENTER)
        #sizer for vertical arrangement
        vbox1 = wx.BoxSizer(wx.VERTICAL)
        vbox1.Add(hsizer1, 1, wx.ALIGN_LEFT)
        vbox1.Add(hsizer2, 1, wx.ALIGN_LEFT)
        vbox1.Add(hsizer3, 3, wx.ALIGN_CENTER)
        vbox1.Add(hsizer4, 8, wx.EXPAND)
        vbox1.Add(hsizer5, 3, wx.ALIGN_CENTER)
        
        self.SetSizer(vbox1)
        
        #event control
        wx.EVT_BUTTON(self, 40, self.onSearch)
        wx.EVT_BUTTON(self, 50, self.onResetview)
        wx.EVT_MENU(self, 200, self.onQuit)
        wx.EVT_MENU(self, 201, self.onAbout)
        wx.EVT_TEXT(self, 10, self.onClear)
        wx.EVT_TEXT(self, 20, self.onClear)
        
        self.Show()
    
    def onSearch(self, e):
        departure=self.cmb1.GetValue()
        destination=self.cmb2.GetValue()
        if departure==destination:
            self.text.SetValue('error message: departure airport matches the destination.')
        else:
            self.text.SetValue(self.database.findShortestPath(departure, destination))
    def onResetview(self, e):
        self.Center()
        fullSize = wx.DisplaySize()
        self.SetSize((fullSize[0]/2, fullSize[1]/2))
    
    def onQuit(self, e):
        self.Close()
        
    def onAbout(self, e):
        wx.MessageBox('This is an application to find the shortest path between two selected airport.', 'about', style=wx.OK)
    #clear the text box when a new selection happens on either combobox
    def onClear(self, e):
        self.text.Clear()  
        
        
        

myApp = wx.App()
myFrame = MyAppWindow()
myApp.MainLoop()