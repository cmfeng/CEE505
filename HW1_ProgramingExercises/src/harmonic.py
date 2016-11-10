def harmonic(n):#only works for n>1, not n=0
    if n==0:
        print "invalid input"
    else:
        a=[]
        b=[]
        i=1
        a.append(1)
        b.append(a[0])
        print '{0} {1:.6f} {2:.6f}'.format(i, a[i-1], b[i-1])
        i=2
        while i<=n:
            a.append(1.0/i)
            b.append(b[i-2]+a[i-1])
            print '{0} {1:.6f} {2:.6f}'.format(i, a[i-1], b[i-1])
            i+=1
harmonic(16)
#what dose the 0, 1, 2 in  '{0} {1:.6f} {2:.6f}' mean?
