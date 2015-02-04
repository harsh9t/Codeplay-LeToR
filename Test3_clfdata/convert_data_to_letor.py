import re
fop = open('clef_data/2014data/qrels.training.graded.txt', 'r')
#print fop.read()
wop = open('space_test_write.txt', 'w')
for line in fop:
	if re.match("(.*) 3(.*)", line):
		print >> wop, line,