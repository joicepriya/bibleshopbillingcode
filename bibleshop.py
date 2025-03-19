import datetime


print("###############JESUS BIBLE SHOP###################")

def thinks_order():
    try:

    
        f=open("menu.txt","r")
        menu=f.read()
        print(menu)
        
            
        church_thinks=menu.split(",")
        print(church_thinks)

        one_rosary=50
        one_bible=500
        one_prayerbook=200
        one_hollywater=100
        one_jesusphoto=200
        one_calander=50
        one_mothermarysaree=600
        one_crossdoller=60
        one_candle=5
        one_candlestand=250
        one_mothermaryphoto=300
        one_statue=1000
        one_songCD=100  

        your_order=input("enter your order: ")
        datetime_date=datetime.datetime.now()
            
        if your_order in menu:
            print(f"{your_order} book is available")
            quality=int(input(f"how many {your_order} you want: "))
            
            if your_order=="candle":
                total=one_candle*quality
                print(total)

            if your_order=="bible":
                total=one_bible*quality
                print(total)

            if your_order=="prayerbook":
                total=one_prayerbook*quality
                print(total)


            if your_order=="candle":
                total=one_candle*quality
                print(total)

            if your_order=="hollywater":
                total=one_hollywater*quality
                print(total)

            if your_order=="rosary":
                total=one_rosary*quality
                print(total)

            if your_order=="jesusphoto":
                total=one_jesusphoto*quality
                print(total)

            if your_order=="calandre":
                total=one_calander*quality
                print(total)

            if your_order=="bibleverse":
                total=one_bibleverse*quality
                print(total)

            if your_order=="mothermarysaree":
                total=one_mothermarysaree*quality
                print(total)

            if your_order=="bibleverse":
                total=one_bibleverse*quality
                print(total)

            if your_order=="crossdoller":
                total=one_crossdoller*quality
                print(total)

            if your_order=="candlestand":
                total=one_candlestand*quality
                print(total)

            if your_order=="mothermaryphoto":
                total=one_mothermaryphoto*quality
                print(total)

            if your_order=="statue":
                total=one_statue*quality
                print(total)

            if your_order=="songsCD":
                total=one_songsCD*quality
                print(total)

            x_time=datetime_date.strftime("%d,%M,%Y time:%H,%M,%S")   
            f=open("bill.txt","w")
            f.write(f"your total bill is {total}\n generated bill on {x_time}")
            
            print("bill generater sucessfully")       

        else:
            print(f"{your_order} is not found")
    except:
        print("this file is not available")        

thinks_order()
    

