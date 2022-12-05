from datetime import date
from datetime import datetime

def main():
    ## DATE OBJECTS
    # Get today's date from the simple today() method from the date class
    today_date = date.today()
    print ("Today's date is ", today_date)


    t = datetime.time(datetime.now())
    print ("The current time is ", t)
  
  
if __name__ == "__main__":
    main()