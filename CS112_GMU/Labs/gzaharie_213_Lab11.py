class Student:
	def __init__(self,name,score,birth_date):
		self.name = name
		self.score = score
		self.birth_date = birth_date
		
	def get_grade(self):
		if self.score >=90:
			return "A"
		elif self.score >= 80:
			return "B"
		elif self.score >= 70:
			return "C"
		elif self.score >=60:
			return "D"
		else:
			return "F"
			
	def age(self):
		lst = self.birth_date.split('-')
		age = 2022 - int(lst[2])
		return age