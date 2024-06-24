s='1'
for n in range (1,31):
       M,T,E = [],[],[s[0]]
       # generate E and M
       nrep=1      # number of repeats
       for i in range(0,len(s)-1):
               if (s[i] != s[i+1]):
                   E.append(s[i+1])
                   M.append(nrep)
                   nrep=1
               else: nrep=nrep+1
       M.append(nrep)
       # generate T
       for k in range(len(M)):
           T.append(repr(M[k]))
           T.append(E[k])
       s="".join(T)
       # print s,      # if you want to see the string
       print (len(s))