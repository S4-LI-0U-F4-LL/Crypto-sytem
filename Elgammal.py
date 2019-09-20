#generation des cles
def genkeys(t):
	p=next_prime(ZZ.random_element(2**t))
	n=p-1
	g=randrange(2**t/4)
	while power_mod(g,n,p)!=1:
		g=randrange(p-1)

	a=randrange(2**t/2)
	h=power_mod(g,a,p)
	return [g,h,p,a]

def encrypt(text,g,h,p):
	k=randrange(2**256)
	liste=[]
	c1=power_mod(g,k,p)
	for char in text:
		liste.append( (ord(char)*power_mod(h,k,p))%p )
	return [liste,c1]
	pass