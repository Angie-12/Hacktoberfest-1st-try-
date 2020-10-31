print("Title of program: Post-exam/encouragement bot")
print()
while True:
  description = input("How do you feel after the post exam activities?")

  list_of_words = description.split()

  feelings_list = []
  encouragement_list = []
  counter = 0
  
  for each_word in list_of_words:
    
    if each_word == "bored":
      feelings_list.append("bored")
      encouragement_list.append("google a joke lah, or go eat food, or find something else that you like to do. You can always revise too!")
      counter += 1
    if each_word == "results":
      feelings_list.append("results")
      encouragement_list.append("they do not define you. If you did well, keep up the good work and don't be complacent. If you didn't, try harder! You will get there! I believe in you!")
      counter += 1
    if each_word == "tired":
      feelings_list.append("tired")
      encouragement_list.append("you are stronger than you think, pick yourself up after a break okay?")
    if each_word == "enjoying":
      feelings_list.append("enjoying")
      encouragement_list.append("share the fun with others, it'll make you happier that way as well :D")
      counter += 1
    if each_word == "lazy":
      feelings_list.append("lazy")
      encouragement_list.append("You can relax for a while but remember to plan your time wisely.")
      counter += 1
    if each_word == "excited":
      feelings_list.append("excited")
      encouragement_list.append("Me too! I'm so happy for you! Have fun!")
      counter += 1
    if each_word == "sad":
      feelings_list.append("sad")
      encouragement_list.append("Don't be sad, you can still meet up with your classmates in the future")
      counter += 1
    if each_word == "happy":
      feelings_list.append("happy")
      encouragement_list.append("Yay! Remember to stay positive!")
      counter += 1
    if each_word == "worried":
      feelings_list.append("worried")
      encouragement_list.append("Don't be too stressed out, I'm sure you can do it ! Worrying after a stressfulis suffering twice!")
      counter += 1
    if each_word == "relieved":
      feelings_list.append("relieved")
      encouragement_list.append("Same! Enjoy yourslef after the stressful exams")
      counter += 1
     
  if counter == 0:
    
      output = "Sorry I don't really understand. Please use different words?"

  elif counter == 1:
    
      output = "It seems that you are feeling quite " + feelings_list[0] + ". However, do remember that "+ encouragement_list[0] + "! Hope you feel better :)"  

  else:

    feelings = ""    
    for i in range(len(feelings_list)-1):
      feelings += feelings_list[i] + ", "
    feelings += "and " + feelings_list[-1]
    
    encouragement = ""    
    for j in range(len(encouragement_list)-1):
      encouragement += encouragement_list[i] + ", "
    encouragement += "and " + encouragement_list[-1]

    output = "It seems that you are feeling quite " + feelings + ". Please always remember "+ encouragement + "! Hope you feel better :)"

  print()
  print(output)
  print()

  

