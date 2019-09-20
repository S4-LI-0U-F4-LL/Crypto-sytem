#ttp

p=next_prime(ZZ.random_element(2**160))
Fp = FiniteField(p)

a=Fp(randrange(2**80))
b=Fp(randrange(2**94))

E = EllipticCurve(Fp, [a, b])

G=E.gens()[0]
n=G.order()
def tp1(p,a,b):
	print "la valeur de a",a
	print "la valeur de b",b
	print " le corp ",Fp
	print "la la fonction ",E
	n=E.cardinality()
	print "la valeur de",n
	Points=E.points()
	print "les points",Points
	G = E.gens()[0]
	print"generateur ",G
	d=G.order()
	print"ordre du point  est ",d
	Point=E.random_element()
	print"element aleatoire du groupe  ",Point
	P1=E.point([42,3])
	print "po 1",p1
	P2=E.point([54,6])
	print "po 2 ",P2
	P3=E.point([42,56])
	print "po 3 ",P3
	p4=p1+P2
	print "po 4 ",P4
	p5=2*p1
	print "po 5 ",P1
	p6=p1+P3
	print "po 6",P6

	return plot(E)


def ECDH(p,a,b):
	if E.discriminant() != 0:
		A=randrange(p)
		AG=A*G
		B=randrange(p)
		BG=B*G
		KA=A*BG
		KB=B*AG
	if KA==KB:
		print "cest bon"

	return [AG,BG,KA,KB]

def ECDH_3(p,a,b):

	if E.discriminant() != 0:
		A=randrange(p)
		AG=A*G
		B=randrange(p)
		BG=B*G
		C=randrange(p)
		CG=C*G

		ACG=A*CG
		BAG=B*AG
		CBG=C*BG

		KA=A*CBG
		KB=B*ACG
		KC=C*BAG
	if KA==KB==KC:
		print "cest bon"

	return [ACG,BAG,CBG,KA,KB,KC]



#elgamal
def genkeys():
	alpha=randrange(n)
	H=alpha*G
	return [G,H,E,p,alpha]


def cipher(m,G,H,E,P):
	k=ZZ.random_element(p)
	c1=k*G
	c2=k*H+m 
	return [c1,c2]

def decipher(cipher,alpha):
	return cipher[1]+alpha*cipher[0]



def sign(alpha):
	m=E.random_element()
	k=randrange(n)
	while gcd(k,n) != 1:
		k=randrange(n)

	r0=k*G
	r=Integer(r0[0])
	e=hash(m)
	print"hashage",m
	s=inverse_mod(k,n)*(e+alpha*r)%n
	return [m,r,s]

		
def verify_sign(m,r,s,H):
	e=hash(m)
	print "hashage",e
	w=inverse_mod(s,n)
	u1=e*w%n
	u2=r*w%n
	x=u1*G+u2*H
	v=Integer(x[0])
	return v==r






















