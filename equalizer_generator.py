inputFilePath = r'C:\Users\David\Desktop\testcurve.txt'

outputFilePath = r'C:\Users\David\Desktop\correctedCurve.txt'

targetLevel = 67.75

responseDictionary = {}

with open(inputFilePath) as file:
	for line in file:
		if not line.startswith('*'):
			(frequency, dB, phase) = line.split()
			frequency = frequency[:-1]
			dB = float(dB[:-1])
			responseDictionary[frequency] = dB

outputFile = open(outputFilePath, 'w')

#outputFile.write('Preamp: 0 dB' + '\n')

outputFile.write('GraphicEQ: ')

for frequency, dB in responseDictionary.items():
	outputFile.write(frequency + ' ' + str(round(targetLevel - dB, 3)) + '; ')
outputFile.write('\n')
	
#outputFile.write('GraphicEQ: 20 -36; 40 2; 20000 -6;')

print('Complete!')