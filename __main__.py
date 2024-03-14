import os
import sys

from main_operations import *



def main():
   insert_record('Skyline Serenade',10)
   insert_record('Midnight Symphony',15)
   insert_record('Starlight Sonata',12)
   insert_record('Sonata' , 15)
   insert_record('Moonlit Melodies',10)
   insert_record('Oceanic Overture',2)
   insert_record('Twilight Tango',3)
   insert_record('Aurora Anthem',5)
   insert_record('Raindrop Rhapsody',6)
   insert_record('Stellar Serenade',4)
   insert_record('Sunset Sonata',2)

   delete_record('Serenade',5)
   update_copies_in_records('black',20)
   update_copies_in_records('Serenade',15)
   delete_record('Serenade',5)



   update_name('Serenade' , 'Serenade 2')




   print_all_records()
   calculate_records_num()
   
   


if __name__ == '__main__':
    external_param = sys.argv[1]
    os.environ["file_name"] = external_param
    main()
