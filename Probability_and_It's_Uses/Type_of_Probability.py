#------------------------Marginal Probability----------------------------------

#total number of students
total=105

#Students attended Online training
students_trained=45

# The probability that a candidate has undergone Online training
edu_training=students_trained/total
print("The probability that a candidate has undergone Online training is ",round(edu_training,2))


#-----------------------Joint probability--------------------------------------

#students with Online training having good salary
good_sal_edu=30

#students without Online training having good salary
good_sal=5

#Finding the probability that a candidate has attended Online training and
# also has good package
student_good_sal=good_sal_edu/total

print("The probability that a candidate has attended Online training and also has good "
      "package ",student_good_sal)



#------------------------Conditional Probability-------------------------------

#Total no. of students without Online training
student_without_training=60

#Students getting good salary without training
student_without_training_good_sal=5

print("The probability of students getting good package without Online training "
      "is ",student_without_training_good_sal/student_without_training)