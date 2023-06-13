Q=["1.Who fought with Raavan during Sita's abduction?",
   "2.Who was the king of bears in Ramayana?",
   "3.Who was Angad's father?",
   "4.The king of Vaanars who helped Shri Ram?"]
A=["Jatayu","Jambavant","Bali","Sugreev"]
j=(0)
for i in range(0,4):
    print(Q[i])
    a=input("Enter your answer : ")
    if(a==A[i]):
        j=j+500
        print("You have earned",j,"rupees.")
    else:
        print("Wrong answer. You have earned no money.")
        break     
    i=i+1
