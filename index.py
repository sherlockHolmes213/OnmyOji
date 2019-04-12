import wx
import configData
class RadioButtonFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, 'Radio Example', 
                size=(400, 800))
        panel = wx.Panel(self, -1)
        radio = dict()
        textInfo = dict()
        for i in configData.wareConfigData["wareType"]:
            radio[int(i-1)] = wx.RadioButton(panel,-1,configData.wareConfigData["wareName"][i],pos=(20, 50+(30*i)))
            textInfo[int(i-1)]= wx.TextCtrl(panel, -1, "", pos=(80, 50+(30*i)))
        # radio1 = wx.RadioButton(panel, -1, "Elmo", pos=(20, 50), style=wx.RB_GROUP)
        # radio2 = wx.RadioButton(panel, -1, "Ernie", pos=(20, 80))
        # radio3 = wx.RadioButton(panel, -1, "Bert", pos=(20, 110))
        # text1 = wx.TextCtrl(panel, -1, "", pos=(80, 50))
        # text2 = wx.TextCtrl(panel, -1, "", pos=(80, 80))
        # text3 = wx.TextCtrl(panel, -1, "", pos=(80, 110))
        self.texts = {"Elmo": textextInfot[0], "Ernie": textInfo[1], "Bert": textInfo[2]}
        for eachText in [textInfo[1], textInfo[2]]:
            eachText.Enable(False)
        for eachRadio in [radio[0], radio[1], radio[2]]:
            self.Bind(wx.EVT_RADIOBUTTON, self.OnRadio, eachRadio)
        self.selectedText = textInfo[0]

    def OnRadio(self, event):
        if self.selectedText:
            self.selectedText.Enable(False)
        radioSelected = event.GetEventObject()
        text = self.texts[radioSelected.GetLabel()]
        text.Enable(True)
        self.selectedText = text

if __name__ == '__main__':
    app = wx.PySimpleApp()
    RadioButtonFrame().Show()
    app.MainLoop()             
