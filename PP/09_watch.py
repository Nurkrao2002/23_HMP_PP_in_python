class Watch:
    fp="Flipkart"
    az="Amazon"          # fp and az are class variables
    
    def __init__(self,wname,wcolor):    #wname means watchname , wcolor: watch clolor
        self.wname=wname
        self.wcolor=wcolor             # wname and wcolor are instance variables

    def purchase(self):
        print("You have Purchased "+self.wname+" from Flipkart/Amazon")
    
    def color(self):
        print("You have Choosen "+self.wcolor+" a nice color")