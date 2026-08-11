#ERSTE Lösung
import json

with open("user_study.json") as f :
    data = json.load(f)

def count():
    """
    Calculate the number of courses and users in the JSON file.
    JSON file is located at ~/project/user_study.json
    
    Returns:
        count_user(int): Total number of users.
        count_course(int): Total number of courses.
    """
    course_set = set()
    user_set = set()
    for record in data :
        user_id = record["user_id"]
        course = record["course"]
        course_set.add(course)
        user_set.add(user_id) 
    count_user = len(user_set)
    count_course = len(course_set)
    # TODO: implement this function
    # Note: Do not change the existing code

    return count_user, count_course


if __name__ == "__main__":
    # Print the number of unique user IDs and course names
    count_user, count_course = count()
    print(f"The file contains {count_user} users and {count_course} courses")

#Zweite Lösung

#import json


#def count():
 #   """
  #  Calculate the number of courses and users in the JSON file.
   # JSON file is located at ~/project/user_study.json

#    Returns:
 #       count_user(int): Total number of users.
  #      count_course(int): Total number of courses.
   # """

 #   count_user = 0
  #  count_course = 0

 #   with open("user_study.json", "r") as f:
  #      data = json.load(f)

 #   count_user_set = set()  # Create an empty set to store unique user IDs
    count_course_set = set()  # Create an empty set to store unique course names

 #   for i in data:
   #     count_user_set.add(i["user_id"])  # Add each user ID to the set
    #    count_course_set.add(i["course"])  # Add each course name to the set
#
 #   count_user = len(count_user_set)
    count_course = len(count_course_set)

  #  return count_user, count_course


#if __name__ == "__main__":
    # Print the number of unique user IDs and course names
 #   count_user, count_course = count()
  #  print(f"The file contains {count_user} users and {count_course} courses")
