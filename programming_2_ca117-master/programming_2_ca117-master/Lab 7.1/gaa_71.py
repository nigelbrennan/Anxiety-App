class Score(object):
	def __init__(self, goals=0, points=0):
		self.goals = goals
		self.points = points

	def greater_than(self, team):
		pts1 = self.goals * 3 + self.points
		pts2 = team.goals * 3 + team.points
		if pts1 > pts2:
			return 'True'
		else:
			return 'False'

	def less_than(self, team):
		pts1 = self.goals * 3 + self.points
		pts2 = team.goals * 3 + team.points
		if pts1 < pts2:
			return 'True'
		else:
			return 'False'

	def equal_to(self, team):
		pts1 = (self.goals * 3) + self.points
		pts2 = (team.goals * 3) + team.points
		if pts1 == pts2:
			return 'True'
		else:
			return 'False'

def main():

	score1 = Score()
	score2 = Score(3, 9)
	score3 = Score(4, 6)

	print(score1.less_than(score2))
	print(score3.less_than(score1))
	print(score1.greater_than(score2))
	print(score3.greater_than(score2))
	print(score1.greater_than(score1))
	print(score2.greater_than(score1))
	print(score2.equal_to(score1))
	print(score3.equal_to(score2))

if __name__ == '__main__':
	main()
