from random import shuffle

def shuffleString(string):
	lst=list(string)
	shuffle(lst)
	return(''.join(lst))

def removeDuplicates(string):
	lst=[]
	for i in string:
		if i in lst:
			continue
		else:
			lst.append(i)
	return(''.join(lst))

def shuffleAndRemoveDuplicates(string):
	return(shuffleString(removeDuplicates(string)))

bridgeCharas='ァアィイゥウェエォオカガキギクグケゲコゴサザシジスズセゼソゾタダチヂッツヅテデトドナニヌネノハバパヒビピフブプヘベペホボポマミムメモャヤュユョヨラリルレロヮワヲン'

bridgeCharas+='ぁあぃいぅうぇえぉおかがきぎくぐけげこごさざしじすずせぜそぞただちぢっつづてでとどなにぬねのはばぱひびぴふぶぷへべぺほぼぽまみむめもゃやゅゆょよらりるれろゎわをん'

bridgeCharas=shuffleAndRemoveDuplicates(bridgeCharas)

latinAlphabetLower='qwertyuiopasdfghjklzxcvbnm'
indianNumerals='1234567890'
latinAlphabetUpper=latinAlphabetLower.upper()
alphaNumeric=latinAlphabetLower+latinAlphabetUpper+indianNumerals
standardSymbols='!@#$%^&*()_+-={}[]|\:";<>?,./'+"'"
standardKeyboard=shuffleAndRemoveDuplicates(standardSymbols+alphaNumeric)

greekAlphabet='ΑαΒβΓγΔδΕεΖζΗηΘθΙιΚκΛλΜμΝνΞξΟοΠπΡρΣσςΤτΥυΦφΧχΨψΩω'
ukranianAlphabet='АаБбВвГгҐґДдЕеЄєЖжЗзИиІіЇїЙйКкЛлМмНнОоПпРрСсТтУуФфХхЦцЧчШшЩщЬьЮюЯя'

cipherTextCharas=shuffleAndRemoveDuplicates(alphaNumeric)+shuffleAndRemoveDuplicates(standardSymbols)+shuffleAndRemoveDuplicates(greekAlphabet)+shuffleAndRemoveDuplicates(ukranianAlphabet)

print("Bridging characters:\n"+bridgeCharas+'\n')
print("Cipher text characters:\n"+cipherTextCharas+'\n')
