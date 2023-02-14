import pyttsx3



n=input("Enter a number")
dic ={
      "1":"ones",
      "2": "twos",
      "3":"threes",
      "4":"Fours",
      "5":"Fives",
      "6":"Sixes",
      "7":"Sevens",
      "8":"Eights",
      "9":"Nines",
      "10":"Tens"

}

txt=""
for i in range (1,11):
    mul= i*int(n)
    txt +=  str(i)+" " +dic[n]+ " are "+ str(mul)+"\n"
    print(txt)
    #1 nines are 9

engine=pyttsx3.init()
engine.say(txt)
engine.runAndWait()