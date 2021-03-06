# -*- coding: utf-8 -*-
"""
Created on Fri May 19 16:21:29 2017

@author: Zahra
"""


import numpy as np



from matplotlib import pyplot as plt



#Question 1



def conv(f,n=0):

    

    s=np.zeros(f.size)                              #Array of zeroes with same length as f

    s[n]=1



    s=np.fft.fft(s)



    f=np.fft.fft(f)



    return np.real(np.fft.ifft(f*s))





x=np.arange(-10,10,0.1)



sig=2

cent=0

y=np.exp(-0.5*(x-cent)**2/sig**2)

a=y.size

yshift=conv(y,a/2)



    

plt.plot(x,y)



plt.plot(x,yshift)

plt.show()



#Question 2



def corr(x,y):



    x_new=np.fft.fft(x)



    y_new=np.fft.fft(y)



    return np.real(np.fft.ifft(x_new*y_new))

x=np.arange(-10,10,0.1)



sig=2

cent=0

y=np.exp(-0.5*(x-cent)**2/sig**2)

ycorr=corr(y,y)

plt.plot(x,ycorr)

plt.show()



#Question 3

def conv(f,n=0):

    

    s=0*f                               

    s[n]=1



    s=np.fft.fft(s)



    f=np.fft.fft(f)



    return np.real(np.fft.ifft(f*s))





x=np.arange(-10,10,0.1)



sig=2

cent=0

y=np.exp(-0.5*(x-cent)**2/sig**2)

a=y.size

yshift=conv(y,a/2)



def corr(x,y):



    x_new=np.fft.fft(x)



    y_new=np.fft.fft(y)



    return np.real(np.fft.ifft(x_new*y_new))



ycorr=corr(y,y)



yshiftcorr=corr(yshift,yshift)

plt.plot(x,ycorr)

plt.plot(x,yshiftcorr)

plt.show()



#Question 4

def nowrapconv(x,y):



    xo=np.zeros(2*x.size)       #Array twice the size of x with just zeroes



    xo[0:x.size]=x              #Then set half the values in the array of length 2x to be x







    yo=np.zeros(2*y.size)



    yo[0:y.size]=y



    x_new=np.fft.fft(xo)



    y_new=np.fft.fft(yo)



    h=np.real(np.fft.ifft(x_new*y_new))



    return h[0:x.size]



#Question 5

class Complex:



    def __init__(self,r=0,i=0):



        self.r=0



        self.i=0

        self.r+=r



        self.i+=i



    def copy(self):                             



        return Complex(self.r,self.i)

        

    def __sub__(self,val):

        

        s=self.copy()      

                     

        s.r-=val.r

        

        s.i-=val.i

        

        return s

        

    def __mul__(self,val):

        s=self.copy()



        sr = 0



        si = 0



        sr += s.r*val.r



        si += s.r*val.i



        si += val.r*s.i



        sr += s.i*val.i                         #Mulstiplying two imaginaries gives you a real

        

        s.r=sr

        

        s.i=si

        

        return s

        

    def __div__(self,val):

        s=self.copy()

        conj=Complex(val.r,val.i*(-1))                      #Complex conjugate means taking the negative of the imaginary part

        t=s.__mul__(conj)

        b=s.__mul__(conj)

        s.r=t.r/b.r

        s.i=t.i/b.i

        return s

        



num1 =Complex (6,2)



num2 =Complex(3,10)

print "num2 - num1 is " + repr((num2 - num1).r) + "+i*" +repr((num2 - num1).i)

print "num2 * num1 is ", (num2 * num1).r, "+i*",(num2 * num1).i

print "num2 / num1 is ", (num2 / num1).r, "+i*",(num2 / num1).i



num1=Complex(-3,17)

num2=Complex(4,-21)

print "num2 - num1 is " + repr((num2 - num1).r) + "+i*" +repr((num2 - num1).i)

print "num2 * num1 is ", (num2 * num1).r, "+i*",(num2 * num1).i

print "num2 / num1 is ", (num2 / num1).r, "+i*",(num2 / num1).i