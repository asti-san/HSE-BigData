import sys

current_key = ''
evenFile_set = set()
pt_data = [0.0, 0.0]

for line in sys.stdin:
	antiNucleus, eventFile, Pt = line.split(',')	
	Pt = float(Pt)

	if current_key == '':
		current_key = antiNucleus

	if current_key != antiNucleus:
		# print("pt_data: {0}" .format(pt_data))
		print('{0}\t{1},{2}' .format(current_key, len(evenFile_set), pt_data[0] / pt_data[1]))

		current_key = antiNucleus
		evenFile_set.clear()
		evenFile_set.add(eventFile)
		pt_data = [0.0, 0.0]

	evenFile_set.add(eventFile)
	pt_data[0] += Pt
	pt_data[1] += 1.0

print('{0}\t{1},{2}' .format(current_key, len(evenFile_set), pt_data[0] / pt_data[1]))
