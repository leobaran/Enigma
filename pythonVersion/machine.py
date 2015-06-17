from rotor import Rotor
import charChecker

class Machine():

	#not very secure, I know...
	secretR1 = "dgnotpubfkacivhlsmrjwyxzeq";
	secretR2 = "lompwdzfsravkejnixtgchyqbu";
	secretR3 = "qkgslyfbphotwuraemnczdijvx";
	secretReflector = "lrufxmntzevkphiqodaywbjgsc";

	r1 = Rotor();
	r2 = Rotor();
	r3 = Rotor();
	r1degree = 0;
	r2degree = 0;
	r3degree = 0;
	reflector = Rotor();
	
	def resetRotorDegrees(self):
		self.r1degree = 0;
		self.r2degree = 0;
		self.r3degree = 0;


	def incrementRotorDegrees(self):
		if(self.r1degree == 26):
			if(self.r2degree == 26):
				if(self.r3degree == 26):
					self.resetRotorDegrees();
				else:
					self.r3degree = self.r3degree + 1;
					self.r2degree = 1;
			else:
				self.r2degree = self.r2degree + 1;
				self.r1degree = 1;
		else:
			self.r1degree = self.r1degree + 1;			
	

	def transformCharacter(self, c, encode):
		if not charChecker.checkIsLetter(c):
			if charChecker.checkCharAcceptable(c):
				return c;
			else:
				return "#";

		r1c = self.r1.getEncodedChar(c, self.r1degree);
		r2c = self.r2.getEncodedChar(r1c, self.r2degree);
		r3c = self.r3.getEncodedChar(r2c, self.r3degree);

		if(encode):
			reflectorC = self.reflector.getEncodedChar(r3c, 0);
		else:
			reflectorC = self.reflector.getDecodedChar(r3c, 0);

		r3dc = self.r3.getDecodedChar(reflectorC, self.r3degree);
		r2dc = self.r2.getDecodedChar(r3dc, self.r2degree);
		r1dc = self.r1.getDecodedChar(r2dc, self.r1degree);
		return r1dc;


	def getTransformedString(self, word, encode):
		if word == "<>":
			self.resetRotorDegrees();
			return "<>";

		newWord = "";
		for char in word:	
			newWord = newWord + self.transformCharacter(char, encode);	
			self.incrementRotorDegrees();
		
		return newWord;
		
	def __init__(self, secretModeFlag):
		if(secretModeFlag):
			self.r1.setSecretAlphabet(self.secretR1);	
			self.r2.setSecretAlphabet(self.secretR2);	
			self.r3.setSecretAlphabet(self.secretR3);	
			self.reflector.setSecretAlphabet(self.secretReflector);	
		