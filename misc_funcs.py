def health_colorer(percentage):
	if percentage >= 70:
		return '\033[32m'
	if percentage >= 30 and percentage <69:
		return '\033[33m'
	else:
		return '\033[31m'