print("Answer number 1")
def TowerOfHanoi( x, from_rod, to_rod, middle_rod):
	if x == 0:
		return
	TowerOfHanoi(x-1, from_rod, middle_rod, to_rod)
	print("Move disk",x,"from rod",from_rod,"to rod",to_rod)
	TowerOfHanoi(x-1, middle_rod, to_rod, from_rod)
x = 3
TowerOfHanoi(x, 'A', 'C', 'B')
