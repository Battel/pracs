cinclude<iostream.h>
#include <conio.h>
void main()
{  clrscr();
 cout<<"Name : Kimberly Moniz \n Roll No : 21 \n";
 cout<<"\n Create a simple linear neural network.";
 
float x,bias,weight,Yin,out;

 cout<<"\nEnter the input X : "; cin>>x;
 cout<<"\nEnter the bias : "; cin>>bias;
 cout<<"\nEnter the weight W = "; cin>>weight;

 Yin = (bias + (x*weight ));

 cout<<"\n Yin = bias + x*weight "<<"\n Yin = "<<Yin;

 if(Yin<0) out=0;
 else if((Yin>=0) && (Yin<1))  out=Yin;
 else out=1;
 cout<<"\nY = "<<out;
 getch();
}
