#generatiion des clee 

def genkey(t):
	p=next_prime(ZZ.random_element(2**t))
	q=next_prime(ZZ.random_element(2**t))
	n=p*q

	phi=(p-1)*(q-1)
	e=ZZ.random_element(phi)
	while gcd(e,phi) !=1 :
		e=ZZ.random_element(phi)
	pgcd,u,v=xgcd(e,phi)
	d = Integer(mod(u, phi))
	return [e,d,n]

	return(genkey())

#chiffrement

def cipher(text,key_pub,n):
	liste=[]
	for char in text:
		liste.append( power_mod(ord(char),key_pub, n))
	
	return liste

#dechiffrement

def decipher(c,key_priv,n):
	liste=[]
	for i in c:
		liste.append( power_mod(i,key_priv, n))
	return liste


#signature

def sign(text,key_priv,n):
	liste=[]
	for char in text:
		liste.append( power_mod(ord(char),key_priv, n))
	pass
	return liste


#verify_sign
def convert(text):
	liste=[]
	for char in text:
		liste.append(ord(char))
		pass
	pass
	return liste

def verify_sign(m,sign,key_pub,n):
	liste=[]
	for i in sign:
		liste.append(power_mod(i,key_pub, n))
	print liste
	if liste==m:
		print('singature OK')
	else:
		print('signature pas OK')













