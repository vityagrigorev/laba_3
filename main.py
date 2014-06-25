import sys
import BigInt 

def PrintStart():

	print"Enter the input parameters:\n"
	print"\n<name of program> <filename A> <operation>\n<filename B> <result filename C> [b] [filename with module]\n\n"
	print"Parametr: \n"
	print"\"-b\" - binfile\n"
	print"Operations: \n"
	print"\+,-,*,/,%,^\n"
	sys.exit(-1)

print"Program TCHMK.\n"
if len(sys.argv) < 5 or len(sys.argv) > 7:
	PrintStart();



fileA = sys.argv[1]
operation = sys.argv[2]
fileB =sys.argv[3]
fileC = sys.argv[4]
bin = False

if len(sys.argv) == 6:

	 if sys.argv[5] == "-b":
		 bin  = True;
if len(sys.argv) == 7:
	
	fmodule = sys.argv[6];

print"fileA :",fileA;
print"operation :",operation;
print"fileB :",fileB;
print"fileC :",fileC;
print"bin :",bin;

if len(sys.argv) == 7:
	print"fmodule: ",fmodule;

a = BigInt.BigInt()
b = BigInt.BigInt()
c = BigInt.BigInt()
mod = BigInt.BigInt()

if bin == True:
	a.getFrom_bin(fileA)
	b.getFrom_bin(fileB)
	if len(sys.argv) == 7:
		mod.getFrom_bin(fmodule)
else:
	a.getFrom_txt(fileA)
	b.getFrom_txt(fileB)
	if len(sys.argv) == 7:		
		mod.getFrom_txt(fmodule)

if operation == "+":
	c = a + b;
elif operation == "-":
	c = a - b;
elif operation == "*":
	c = a * b;
elif operation == "/":
	c = a / b;
elif operation == "%":
	c = a % b;
elif operation == "^":
	c = BigInt.Pow(a, b, mod)
else:
	PrintStart()

print"a = ",a
print"b = ",b
print"c = ",c

if bin == False:
	c.saveTo_txt(fileC)
else:
	c.saveTo_bin(fileC)

