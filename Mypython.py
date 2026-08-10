#RICHTIG:ERSTE LÖSUNG
from typing import List
matrix = [['10000000', '10000012', '1000000d', '1000000d', '10000002'],
['10000004', '10000011', '10000017', '1000000b', '1000000f'],
['10000016', '1000000d', '10000018', '10000012', '10000011'],
['10000001', '1000000c', '10000008', '10000013', '10000000'],
['10000019', '10000000', '1000000e', '10000003', '10000004']]

def count_clone_soldier(matrix: List[List[str]]):
    """Finde geklonte Soldaten"""
    # Create an empty dictionary to store the count of each soldier ID
    klone_dict = {}
    
    # Iterate over each row in the matrix
    for riehe in matrix :
        # Iterate over each soldier ID in the current row
        for id in riehe :
            # Check if the soldier ID is already present in the clone_count dictionary
            if id in klone_dict :
                # If the soldier ID is already present, increment its count by 1
                klone_dict[id] += 1
            else :
                # If the soldier ID is not present, initialize its count to 1
                klone_dict[id] = 1

    # Iterate over the clone_count dictionary to decrement the count of each soldier ID by 1
    for id in klone_dict : 
        klone_dict[id] -= 1

    # Remove any soldier IDs from the clone_count dictionary whose count is 0 after decrementing
    glutig_klon = {}
    for k,v in klone_dict.items() :
        if v != 0 :
            glutig_klon[k] = v
    return glutig_klon      

    # Return the clone_count dictionary containing the count of each soldier ID
aufruf = count_clone_soldier(matrix)
print(aufruf)

#RICHTIG : ZWEITE LÖSUNG

from typing import List


def count_clone_soldier(matrix: List[List[str]]):
    # Create an empty dictionary to store the count of each soldier ID
    clone_count = {}

    # Iterate over each row in the matrix
    for row in matrix:
        # Iterate over each soldier ID in the current row
        for soldier_id in row:
            # Check if the soldier ID is already present in the clone_count dictionary
            if soldier_id in clone_count:
                # If the soldier ID is already present, increment its count by 1
                clone_count[soldier_id] += 1
            else:
                # If the soldier ID is not present, initialize its count to 1
                clone_count[soldier_id] = 1

    # Iterate over the clone_count dictionary to decrement the count of each soldier ID by 1
    for soldier_id in clone_count:
        clone_count[soldier_id] -= 1

    # Remove any soldier IDs from the clone_count dictionary whose count is 0 after decrementing
    clone_count = {k: v for k, v in clone_count.items() if v != 0}

    # Return the clone_count dictionary containing the count of each soldier ID
    return clone_count


# FALSE 
#from typing import List
#matrix = [['10000000', '10000012', '1000000d', '1000000d', '10000002'],
#['10000004', '10000011', '10000017', '1000000b', '1000000f'],
#['10000016', '1000000d', '10000018', '10000012', '10000011'],
#['10000001', '1000000c', '10000008', '10000013', '10000000'],
#['10000019', '10000000', '1000000e', '10000003', '10000004']]

#def count_clone_soldier(matrix: List[List[str]]):
    # Create an empty dictionary to store the count of each soldier ID
 #   klone_dict = {}
    
    # Iterate over each row in the matrix
  #  for riehe in matrix :
        # Iterate over each soldier ID in the current row
   #     for id in riehe :
            # Check if the soldier ID is already present in the clone_count dictionary
    #        if id in klone_dict :
                # If the soldier ID is already present, increment its count by 1
     #           klone_dict[id] += 1
      #      else :
                # If the soldier ID is not present, initialize its count to 1
       #         klone_dict[id] = 1

    # Iterate over the clone_count dictionary to decrement the count of each soldier ID by 1

    # Remove any soldier IDs from the clone_count dictionary whose count is 0 after decrementing
    #for k, v in list(klone_dict.items()):   # list() erstellt eine Kopie
     #   if v == 1:
      #      del klone_dict[k]               # ✅ Jetzt ok – du iterierst über die Kopie
    #return klone_dict


    # Return the clone_count dictionary containing the count of each soldier ID
#aufruf = count_clone_soldier(matrix)
#print(aufruf)