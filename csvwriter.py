import csv


class CSVWriter:
	def __init__(self, filename: str = 'samples.csv'):
		self.fieldnames = ['provider_name', 'affiliation', 'address', 'tel', 'distance']
		self.filename = filename
		self.writer = csv.DictWriter(open(self.filename, mode='w', newline=''), self.fieldnames)
		self.writeheader()
	

	def __str__(self):
		return self.filename

	__repr__: str = __str__


	def writeheader(self) -> None:
		self.writer.writeheader()

	
	def writerow(self, row) -> None:
		self.writer.writerow(row)
