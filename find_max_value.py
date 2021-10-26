# 🚨 Don't change the code below 👇
print('Input a list of student scores')
student_scores = input('Write like this: 91 65 75\n').split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

max_value = 0
for x in student_scores:
  if max_value < x:
    max_value = x
print(f"The highest score in the class is: {max_value}")