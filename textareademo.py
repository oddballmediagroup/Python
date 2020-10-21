"""
Program: textareademo.py
Author: Tony 10/29/2020
example fr0om pagers 276-277

GUI Based version of the investment.py application from chapter 3
"""
from breezypythongui import EasyFrame
class TextAreaDemo(EasyFrame):
	"""An investment calculator that demonstrates the use of a multi line text area"""
	def __init__(self):
		"""Sets up the window and the widgets"""
		EasyFrame.__init__(self, title = "Investment Calculator")
		# Add the label components
		self.addLabel(text = "Initial amount", row = 0, column = 0)
		self.addLabel(text = "Number of years", row = 1, column = 0)
		self.addLabel(text = "Interest rate in %", row = 2, column = 0)
		#add the entry field components
		self.amount = self.addFloatField(value = 0.0, row = 0, column = 1)
		#add the text area component
		self.outputArea = self.addTextArea(text = "", row = 4, column = 0, columnspan = 2, width = 50, height = 15)
		#add the button component
		self.compute = self.addButton(text = "Compute", row = 3, column = 0, columnspan = 2, command = self.compute)
		#event handling method
	def compute(self):
		"""computes the investment schedule based on the inputs and outputs the schedule"""
		# accept the inputs
		startBalance = self.amount.getNumber()
		years = self.period.getNumber()
		rate = self.rate.getNumber() / 100
		#if any input is a zero, have the function do nothing
		if startBalance == 0 or rate == 0 or years == 0:
			self.outputArea.setText("Make sure non of the 3 fields have a value of zero!")
			return
		# initialize the acculator variable for the interest
		totalInterest = 0.0
		# set the header for the table
		result = "%4s%18s%10s%16s" % ("Year", "Starting Balance", "Interest" "Ending Balance")
		# compute and append the results for each year
		for year in range(1, years + 1):
			interest = startBalance * rate
			endBalance = startingBalance +  interest
			result += "%4d%18.2f%10.2f%16.2f" % (year, startBalance, interest, endBalance)
			startBalance = endBalance
			totalInterest += interest
			# end of the for loop
		# display the totals for the entire investment period
		result += "Ending balance: $%0.2f" % endBalance
		result += "Total interest earned: $%0.2f" % totalInterest
		#output the result variable while preserving read-only status
		self.outputArea["state"] = "normal"
		self.outputArea.setText(result)
		self.outputArea["state"] = "disabled"
#definition of the main fuction
def main():
	TextAreaDemo().mainloop()
#global call to the main function
main()
