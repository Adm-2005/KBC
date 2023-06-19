Q=["1.Who fought with Raavana during Sita's abduction?\n a.Jatayu b.Vasuki \n c.Indra d.Lakshmana",
   "2.Who was India's 2nd President?\n a.Rajendra Prasad          b.Zakir Hussain \n c.Sarvepalli Radhakrishnan d.Giani Zail Singh",
   "3.Who plays Dr. Homi J.Bhabha in the popular series Rocket Boys?\n a.T.M.Karthik b.Rajeev Kachroo \n c.Jim Sarbh      d.Ishwak Singh",
   "4.The king of Vaanars who helped Shri Ram?\n a.Bali     b.Sugreev \n c.Dashrath d.Vibhishan",
   "5.In which year was Bharatiya Janata Party(BJP) founded?\n a.1980 b.1975 \n c.1982 d.1989",
   "6.Which Indian cricketer among these has played most number of test matches?\n a.SR Tendulkar b.MS Dhoni \n c.Rahul Dravid d.Anil Kumble",
   "7.Which Tennis player has most number of Grand Slams?\n a.Roger Federer b.Andy Murray \n c.Rafael Nadal d.Novak Djokovic",
   "8.Which country has the highest life expectancy?\n a.China b.Hong Kong \n c.India d.South Korea",
   "9.Which language has most native speakers?\n a.Spanish b.English \n c.German  d.French",
   "10.In which year was the United Nations established?\n a.1945 b.1932 \n c.1952 d.1949",
   "11.How many minutes are there in a full week?\n a.10,800 b.10,080 \n c.10,008 d.10,000",
   "12.How many faces does a dodecahedron have?\n a.10 b.14 \n c.11 d.12",
   "13.Which planet in our solar system is the hottest?\n a.Earth   b.Mars \n c.Mercury d.Venus",
   "14.Which planet has most number of moons in our solar system?\n a.Jupiter b.Uranus \n c.Saturn  d.Neptune",
   "15.How many dots appear on a pair of dice?\n a.56 b.42 \n c.36 d.48"]
A=["a","c","c","b","a","a","d","b","a","a","b","d","d","c","b"]
levels=[1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,1250000,2500000,5000000,10000000]
j=(0)
for i in range(0,len(Q)):
    print(Q[i])
    a=input("Enter your answer (a-d): \n ")
    if(a==A[i]):
        j=levels[i]
        if(j==10000000):
            print(f"Congratulations. You have won the game!")
            break
        else:
            print(f"Right Answer. You have earned ₹{j}/- \n")
    else:
        if(j<10000):
            print("Wrong answer. You have earned no money.")
            break
        elif(j>=10000 and j<320000):
            print("Wrong Answer. You have earned ₹10,000/-")
            break
        elif(j>=320000 and j<10000000):
            print("Wrong Answer. You have earned ₹3,20,000/-")
            break   
    i=i+1
