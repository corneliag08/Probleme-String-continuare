s=input("Introdu numele,prenumele:")
s1=s.split()
if ((s1[1]==s1[1].title())and (s1[0]==s1[0].title())):
    print("Numele și prenumele este corect")
else:
    print("Nu este corect")