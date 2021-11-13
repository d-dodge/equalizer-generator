import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('givenTargetLevel', help='Arbitrary average db level to normalize response to')
parser.add_argument('givenInputFile', help='Input File')
parser.add_argument('givenOutputFile', help='Output File')
args = parser.parse_args()

inputFilePath = os.path.abspath(args.givenInputFile)

outputFilePath = os.path.abspath(args.givenOutputFile)

targetLevel = float(args.givenTargetLevel)

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