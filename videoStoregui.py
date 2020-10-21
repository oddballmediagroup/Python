from breezypythongui import EasyFrame
from tkinter.font import Font
  
class VideoStore(EasyFrame):
 
    """Application window for the Total Charges calculator."""
 
    def __init__(self):
        """Sets up the window and the widgets."""
        EasyFrame.__init__(self, title = "Total Charges Calculator")
        self.setBackground('red')

        # variables and constants
        self.newRental=3.0
        self.oldRental=2.0

        font = Font(family = "monospace", size = 10, slant = "italic")
        self.addLabel(text = "New Rental cost is $%d."%(self.newRental),font=font, background='red',
                      row = 0, column = 0)
 
        self.addLabel(text = "Old Rental cost is $%d."%(self.oldRental),font=font, background='red',
                      row = 1, column = 0)

        self.addLabel(text = "New Rented Videos",font=font, background='red',
                      row = 2, column = 0)
        self.newVideos = self.addIntegerField(value = 0,
                                              row = 2,
                                              column = 1)
        self.newVideos.focus_force()
        self.addLabel(text = "Old Rented Videos",font=font, background='red',
                      row = 3, column = 0)
        self.oldVideos = self.addIntegerField(value = 0,
                                              row = 3,
                                              column = 1)

        # The command button
        self.b=self.addButton(text = "Compute", row = 4, column = 0,
                       columnspan = 2, command = self.computeTax)
        self.b['font']=font
        # Label and field for the Total Charges
        self.r = self.addLabel(text = "The customer is renting %d new videos. And %d old video(s)."%(self.newVideos.getNumber(),self.oldVideos.getNumber()),
                      font=font, background='red', row = 5, column = 0)
        self.totalCost = self.addLabel(text = "The total charge is: $%d."%(0),
                      font=font, background='red', row = 6, column = 0)
  
    # The event handler method for the button
    def computeTax(self):
        """Obtains the data from the input fields and uses
        them to compute the Total Charges, which is sent to the
        output field."""
        #Calculation phase 
        totalCost = (self.newRental * self.newVideos.getNumber()) + (self.oldRental * self.oldVideos.getNumber())
        self.r['text']="The customer is renting %d new videos. And %d old video(s)."%(self.newVideos.getNumber(),self.oldVideos.getNumber())
        self.totalCost['text']="The total charge is: $%d."%(totalCost)
        self.newVideos.focus_force()
 
#Instantiate and pop up the window.
VideoStore().mainloop()
