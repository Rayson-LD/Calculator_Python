import math
import wx
import pyttsx3

engine = pyttsx3.init()
rate = engine.getProperty('rate')                         
engine.setProperty('rate', 150)
class MyFrame(wx.Frame) :
    def __init__(self) :  
        wx.Frame.__init__(self,None,pos=wx.DefaultPosition, size=wx.Size(500,500),style=wx.MAXIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION | wx.MINIMIZE_BOX| wx.CLOSE_BOX | wx.CLIP_CHILDREN,title="Calculator")
        panel= wx.Panel(self)
        my_sizer = wx.BoxSizer(wx.VERTICAL)
        lbl1=wx.StaticText(panel,label="Enter the first digit",size = wx.Size(400,30))
        lbl2=wx.StaticText(panel,label="Enter the second digit :",size = wx.Size(400,30))
        lbl3=wx.StaticText(panel,label="Enter the operation :",size = wx.Size(400,30))
        note=wx.StaticText(panel,label="Note : Enter Only Integer value ",size = wx.Size(400,70))
        self.txt1 = wx.TextCtrl(panel,style= wx.TE_PROCESS_ENTER,size=(400,30))
        self.txt2 = wx.TextCtrl(panel,style= wx.TE_PROCESS_ENTER,size=(400,30))
        self.txt3 = wx.TextCtrl(panel,style= wx.TE_PROCESS_ENTER,size=(400,30))
        self.txt1.SetFocus()
        self.txt2.SetFocus()
        self.txt3.SetFocus()
        self.txt1.SetHint("Enter the first digit")
        self.txt2.SetHint("Enter the second digit ")
        self.txt3.SetHint("Enter the operation + : Add , - : Subtract ,* : Multiply ,/ : Divide\n")
        self.btn = wx.ToggleButton(panel,-1,"Calculate") 
        self.btn.Bind(wx.EVT_TOGGLEBUTTON,self.OnEnter)
        my_sizer.Add(lbl1, 0,wx.ALL,5)
        my_sizer.Add(self.txt1,0,wx.ALIGN_CENTER)
        my_sizer.Add(lbl2, 0,wx.ALL,5)
        my_sizer.Add(self.txt2,0,wx.ALIGN_CENTER)
        my_sizer.Add(lbl3, 0,wx.ALL,5)
        my_sizer.Add(self.txt3,0,wx.ALIGN_CENTER)
        my_sizer.Add(note,0,wx.ALL,5)
        my_sizer.Add(self.btn,0,wx.ALIGN_CENTER)
        panel.SetSizer(my_sizer)
        self.Show()
    def OnEnter(self, event) :
        input1= int(self.txt1.GetValue())
        input2 = int(self.txt2.GetValue())
        oper = self.txt3.GetValue()
        if  oper == "+" :
            result = input1 + input2  
        elif oper== "-":
            result = input1 - input2 
        elif oper == "*" :
            result = input1 * input2
        elif oper == "/" :
            result = input1/input2
        else :
            print("Error")
        print("Your Answer is " + str(result))
        engine.say("Your Answer is "+ str(result))
        engine.runAndWait()
          
if  __name__ == "__main__" :
    app = wx.App(True)
    frame = MyFrame()
    app.MainLoop()    



 


       
