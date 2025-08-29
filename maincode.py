import tkinter as tk
import mysql.connector as sql
import matplotlib.pyplot as plt
import matplotlib.image as img
window=tk.Tk()
movie_code=0
try:     
    conn=sql.connect(host='localhost',user='root',passwd='') #establishing connection with mysql
    if conn.is_connected(): 
        #checking if it is connected to mysql or not
        print('Login successful.')
    else:
        print('Login unsuccessful.')  
    print('_________________________________________')
    print('WELCOME TO SHOWTIME.COM')
    c=conn.cursor()
    c.execute('create database if not exists movie;')
    c.execute('use movie;')
    c.execute('create table if not exists movielist(sno int primary key, name varchar(50), rating float(3,2), genre varchar(20), language varchar(10), synopsis varchar(500));')
    c.execute('delete from movielist;')
    c.execute('insert into movielist values(101,"Oppenheimer",8.6,"Biography Drama", "English", "During World War II, Lt. Gen. Leslie Groves Jr. appoints physicist J. Robert Oppenheimer to work on the top-secret Manhattan Project. Oppenheimer and a team of scientists spend years developing and designing the atomic bomb. Their work comes to fruition on July 16, 1945, as they witness the worlds first nuclear explosion, forever changing the course of history.");')
    c.execute('insert into movielist values(102,"Barbie",7.4,"Adventure Comedy", "English", "Barbie and Ken are having the time of their lives in the colorful and seemingly perfect world of Barbie Land. However, when they get a chance to go to the real world, they soon discover the joys and perils of living among humans.");')
    c.execute('insert into movielist values(103,"Across The Spiderverse",8.8,"Animation Action", "English", "Miles Morales catapults across the Multiverse, where he encounters a team of Spider-People charged with protecting its very existence. When the heroes clash on how to handle a new threat, Miles must redefine what it means to be a hero.");')
    c.execute('insert into movielist values(104,"Gadar 2",6.2,"Action Drama", "Hindi", "During the Indo-Pakistani War of 1971, Tara Singh returns to Pakistan to bring his son, Charanjeet, back home.");')
    c.execute('insert into movielist values(105,"Tranformers: Rise of the Beast",6.1,"Action Sci-Fi", "English", "Optimus Prime and the Autobots take on their biggest challenge yet. When a new threat capable of destroying the entire planet emerges, they must team up with a powerful faction of Transformers known as the Maximals to save Earth.");')
    c.execute('insert into movielist values(106,"Mission Impossible: The Dead Reckoning",8.0,"Thriller Adventure", "English", "IMF team must track down a terrifying new weapon that threatens all of humanity if it falls into the wrong hands. With control of the future and the fate of the world at stake, a deadly race around the globe begins. Confronted by a mysterious, all-powerful enemy, Ethan is forced to consider that nothing can matter more than the mission -- not even the lives of those he cares about most.");')
    c.execute('insert into movielist values(107,"Adipurush",3.1,"Action Adventure", "Hindi", "Raghav, the prince of the Ikshvaku dynasty from Kosala, tries to rescue his wife, Janaki, from the demon king Lankesh.");')
    c.execute('insert into movielist values(108,"Kerala Story",7.2,"Drama", "Hindi", "Shalini Unnikrishnan leads an ordinary life as a college student in Kerala until her identity, relationships, dreams and faith dissipate in the abyss of religious terrorism.");')
    c.execute('insert into movielist values(109,"IB71",7.3,"Action Thriller", "Hindi", "Indian intelligence officers embark on a high-stakes mission to counter two enemy nations conspiracy. If things go sideways, they must think on their feet to avoid a disaster.");')
    c.execute('insert into movielist values(110,"RRR",7.8,"Action Drama", "Telugu", "A fearless revolutionary and an officer in the British force, who once shared a deep bond, decide to join forces and chart out an inspirational path of freedom against the despotic rulers.");')
    conn.commit()

    def display(): # full list of movies
      print('_________________________________________')
      c.execute('select sno, name from movielist;')
      data=c.fetchall()
      print('CODE\t MOVIE')
      for i in data:
          print(i[0],'\t',i[1])
      print()
      print('Enter 100 to return to Main Menu') 
      try:
          n=int(input('Enter Movie Code: ' ))
          if n==100:
              mainmenu()
          elif n>100 and n<111:
              global movie_code
              movie_code=n
              movie()
          else:
              print('Please check the code you have entered.')
              display()
              
      except Exception as e:
          print('Invalid Movie Code. Retry.')
          display()
 
    def searchg(): #search by genre
      print('_________________________________________')
      print()
      print("Genres Available: \n 1.Action \n 2.Adventure  \n 3.Animation \n 4.Biography  \n 5.Comedy \n 6.Drama \n 7.Sci-Fi \n 8.Thriller\n 9.Go Back to Main Menu")
      try:
          genre=int(input('Enter the Genre Number: '))
          if genre==9:
              mainmenu()
          else: 
              d={1:'Action', 2:'Adventure', 3:'Animation', 4:'Biography', 5:'Comedy', 6:'Drama', 7:'Sci-Fi', 8:'Thriller'}
              g=d[genre]
              str1="select sno,name from movielist where genre like '%"+g+"%';" 
              c.execute(str1)
              data=c.fetchall()
              print('_________________________________________')
              print('CODE\t MOVIE')
              for i in data:
                  print(i[0],'\t',i[1])
              print()
              print('Enter 100 to return to Main Menu.')
              
              try: 
                  n=int(input('Enter Movie Code: ' ))
                  if n==100:
                      mainmenu()
                  elif n>100 and n<111:
                      global movie_code
                      movie_code=n
                      movie()
                  else:
                   print('Please check the code entered.')
                   searchg()
              except:
                  print('Invalid Movie Code. Retry.')
                  searchg()
          
      except Exception as e:
          print('Enter a valid Genre Number.')
          searchg()
        
    def searchl(): #search by language
      print('_________________________________________')
      print()
      print('Languages Available: \n 1.English \n 2.Hindi \n 3.Telugu\n 4.Go Back to Main Menu')
      try:
          language=int(input('Enter the Language:'))
          if language==4:
              mainmenu()
          else: 
              d={1: 'English',2:'Hindi',3:'Telugu'}
              l=d[language]
              str1="select sno,name from movielist where language like '%"+l+"%';" 
              c.execute(str1)
              data=c.fetchall()
              print('_________________________________________')
              print('CODE\t MOVIE')
              for i in data:
                  print(i[0],'\t',i[1])
              print()
              print('Enter 100 to return to Main Menu')
              
              try: 
                  n=int(input('Enter Movie Code: ' ))
                  if n==100:
                      mainmenu()
                  elif n>100 and n<111:
                      global movie_code
                      movie_code=n
                      movie()
                  else:
                      print('Please check the code entered.')
                      searchl()
              except:
                  print('Invalid Movie Code. Retry.')
                  searchl()
                  
      except Exception as e:
          print('Enter a valid Language')
          searchl()
  
    
    def searchn(): #search by matching name
        print('_________________________________________')
        print()
        try: 
            name=input('Enter Name of Movie: ')
            str1='select sno,name from movielist where name like "%'+name+'%" ;'
            c.execute(str1)
            data=c.fetchall()
            if data!=[]:
                print('_________________________________________')
                print('CODE\t MOVIE')
                for i in data:
                    print(i[0],'\t',i[1])
                print()
                print('Enter 100 to return to Main Menu') 
                try: 
                    n=int(input('Enter Movie Code: ' ))
                    if n==100:
                        mainmenu()
                    elif n>100 and n<111:
                        global movie_code
                        movie_code=n
                        movie()
                    else:
                        print('Please check the code entered.')
                        searchn()
                except:
                    print('Invalid Movie Code. Retry.')
                    searchn()
            else:
                print('Sorry, that movie is not avaiable.')
                mainmenu()
                
        except Exception as e:
            print('Not found. Please retry.')
            searchn()
            
    def searchr():#highest rated to lowest rated
        print('_________________________________________')
        print()
        try:
            c.execute('select sno,name,rating from movielist order by rating desc')
            data=c.fetchall()
            print('CODE\tRATING\t MOVIE')
            for i in data:
                print(i[0],'\t',i[2],'\t',i[1])
            print()
            print('Enter 100 to return to Main Menu')
            try: 
                n=int(input('Enter Movie Code: ' ))
                if n==100:
                    mainmenu()
                elif n>100 and n<111:
                    global movie_code
                    movie_code=n
                    movie()
                else:
                    print('Please check the code entered.')
                    searchr()
            except:
                print('Invalid Movie Code. Retry.')
                searchr() 
        except:
            print('Invalid, retry.')
            searchr()
    
    
    def mainmenu(): #master menu containing all search functions and exit
        print('_________________________________________')
        print()
        try:
            print('What would you like to do?\n 1.Full list of Movies\n 2.Search Movies by Genre\n 3.Search Movies by Language\n 4.Search Movie By Rating\n 5.Search Movie by Name\n 6.Exit')
            choice=int(input('Enter your choice: '))
            if choice==1:
                display()
            elif choice==2:
                searchg()
            elif choice==3:
                searchl()
            elif choice==4:
                searchr()
            elif choice==5:
                searchn()
            elif choice==6:
                print('Thank you for using Showtime.com')
            else:
                mainmenu()
        except:
            print('Invalid entered. Try again.')
            mainmenu()
    
    #dictionary containing all the reviews of the movies, sorted by code
    reviews_dict={101:["One of the most anticipated films of the year for many people, myself included, Oppenheimer largely delivers. Much of it's great.", "Oppenheimer is - with no doubt- going to be one of the best movies in the history. Amazing cinematography, Exceptional acting and terrifying Soundtracks", "The whole movie feels like a trailer. It's full of stitched up short hurried conversation. Every single dialogue is 'important' and before you can even process it, they abruptly cut it and start the next scene. It's just very hard to keep up."],
             102:["Wow. I did not see this masterpiece coming. Greta Gerwig took Barbie, and made a movie that tackles some really tough social issues....well? It's crazy. The story is very mature, thinker of a plot. Once you're done laughing your butt off, you'll get really emotional.", "Margot does the best with what she's given, but this film was very disappointing to me. It was marketed as a fun, quirky satire with homages to other movies. It started that way, but ended with over-dramatized speeches and an ending that clearly tried to make the audience feel something, but left everyone just feeling confused.", "It pains me to say it, but I enjoyed this movie so much more then I was expecting to, musical numbers, humour, there truly is something for the whole family to enjoy."],
             103:["Spider-Man: Across the Spider-Verse is fantastic! Deftly juggles deeply heartfelt character beats with crazy multiverse content, just packed with so many delightful easter eggs.", "The animation, flow of everything, genius character development, and action were all electrifying! This is one of the best Spider-Man adaptions deserving of the high ratings entirely.", "The animation, flow of everything, genius character development, and action were all electrifying! This is one of the best Spider-Man adaptions deserving of the high ratings entirely."],
             104:["Undoubtedly Sunny Deol was very nice but I found the movie very annoying and specially the acting of the actress Ameesha Patel the new actress and the son. They definitely try to make some scenes emotional but they fail to do so and I really hate the writing of the writers.", "Despite having a mediocre plot, the film manages to engage the audience due to its nostalgic feel and action sequences. Director Anil Sharma wasn't able to match the expectations of the first part, but still, he managed to deliver a one-time watch action drama film.", "I was sure within the first half an hour of the movie that it was quite overly hyped - the story and acting was par poor. If you are Sunny Deol fan - then you wont regret watching it. Otherwise this movie does not have anything new."],
             105:["It's an ok movie. The lead up is solid, not great but not terrible either, but this movie really shines at the end. Watching the Transformers come together and fight is epic, and if you have a good sound system, it's even better.","Transformers: Rise of the Beasts has become an entertaining film, but it is really nowhere near high quality. That is absolutely not due to the effects, because they are very good, but story-wise it is all very weak and at times even a bit childish.", "Transformers is all about it's CGI, Action pieces and the emotions between the autobots and humans. And this movie has done that perfectly well. Action & CGI is terrific in this film. Background score justifies the film with proper sound effects whenever the action is going on."],
             106:["It is another great big screen action film that we have come to expect. It feels huge the whole time, however I must say I while the set pieces were stellar, the hand to hand combat scenes were not great and a big step down from the last film (Fallout).", "I must say I'm disappointed by the overuse of deus ex machina as a scriptwriting trope. I'm still trying to head-canon a few instances to somehow believe what happened, and of course that repeatedly pulled me out of the story", "Absolutely superb! Cruise, McQuarrie and co have accomplished this, delivering the best spy/ action thriller in years. It is a next level masterclass of a film, with everything you would expect from an Mission Impossible film and more."],
             107:["Adipurush is merely a Bollywood-ised version of one of the most epic tales that ever existed. If you keep the story aside for it's largely known to all, the execution turns out to be a messy blend of over-the-top CGI and passable VFX, and making it worse are the intentionally funny dialogues that sound misplaced in a sensitive and mythological story.", "Ravan and his brothers look younger than Lord Ram which is stupid..... Movie is bad.... The vision and the portrayal of characters which we have seen doesn't fit here. Even though I am all for allowing multiple interpretation, here it doesn't come well.", "Adipurush, a much-anticipated film starring Prabhas, Saif Ali Khan, and Kriti Sanon, fails to live up to the expectations of its viewers. Despite a promising premise and a talented cast, the movie falls short in multiple aspects, leaving the audience unsatisfied and disillusioned."],
             108:["Adah Sharma nailed the show!!! The background music could have been better though. The other supporting characters were bringing the best in Adah Sharma.", "No doubt it's one of those stories which will surely open your eyes, it'll give you a goosebumps while showing the mirror to the society.", "Very intriguing story, really heart wrenching story...... A must-see film. Apart from the story it's a fantastic movie with outstanding direction and acting."],
             109:["It's must a watch film. Vidyut and other actors acted very well. Storyline is good but screenplay looks loose at many points.", "Wow. What a well told story. I was pleasantly surprised and loved every bit of the movie. I would advise anyone who loves a thriller, to please go and watch this movie. Left the theater with a lot of pride for our untold Heroes. The film gives you the patriotic feeling without hyping on it and also with no sloganeering.", "A finely directed spy thriller with remarkable finesse and restraint, IB71 is a film based on a phenomenal real-life mission executed by our secret services, and after watching this film, it fills you with pride. By not revealing all the cards at once and dumbing down everything by dumping information in the form of narration, the film retains a sense of urgency and suspense."],
             110:["A tightrope walk between complete silliness & beautiful sincerity, it has entertainment value dripping from every colorful pore: insane action, enveloping dialogue, sprawling yet intimate storytelling, elaborate dancing", "This movie is a masterpiece, combines some extraordinary drama, stunning stunts and action, great photography and absolutely beautiful music. Given that this is a Bollywood movie, an overall cheesy direction and dialogues and acting won't exactly be Oscar worthy. But none of it made me not enjoy this movie.", "This was an incredible film. The dancing scene at the party was incredible. Overall this is definitely one of the best films of the year combining action, comedy, romance, dancing and great storytelling."]}
    
    def review(): #function to leave a review for the movie chosen
        print('_________________________________________')
        print()
        rev=input('Leave your review: ')
        print('Thank you for leaving a review!')
        movie_review=reviews_dict[movie_code]
        movie_review.append(rev)
        reviews_dict[movie_code]=movie_review
        movie()
        
    def movie(): # movie page
        com="select * from movielist where sno="+str(movie_code)+";"
        c.execute(com)
        data=c.fetchone()
        sno, name, rating, genre, language, synopsis=data
        print('_________________________________________')
        print('\n----------------',name.upper(),'----------------')
        print('Code: ',sno, '\nRating: ',rating,'\nGenre: ',genre, '\nLanguage: ',language)
        print()
        print('MOVIE SYNOPSIS: ')
        print(synopsis)
        print()
        print('REVIEWS: ')
        reviewsdisplay=reviews_dict[movie_code]
        for i in reviewsdisplay:
            print(i)
            print()
        print('What would you like to do? \n1.Proceed to booking \n2.Leave a review \n3.Main Menu')
        x=int(input('Enter your choice: '))
        if x==1:
            pickaseat()
        elif x==2:
            review()
        else:
            mainmenu()
        
    picked_seats=[]
    def booking(x): #saving the seats booked by user
        print ('You picked: '+str(x))
        picked_seats.append(x)
 
    def movieposterselect(code): #to display the movie poster on the ticket
            posters={101:"D:\\Python\\oppenheimer.jpg", 102:"D:\\Python\\barbie.jpg", 103:"D:\\Python\\spiderverse.jpg", 104:"D:\\Python\\gadar2.jpeg", 105:"D:\\Python\\transformers.jpg", 106:"D:\\Python\\mipartone.jpg", 107:"D:\\Python\\adipurush.jpg", 108:"D:\\Python\\keralastory.jpeg", 109:"D:\\Python\\ib71.jpg", 110:"D:\\Python\\rrr.jpg"}
            for i in posters:
                if code==i:
                    return posters[i] 
    def ticket(): #final ticket generation 
        global movie_code
        print('\n--------------------- TICKET ---------------------') 
        print('ADMIT',len(picked_seats),'\n') 
        c.execute('select curdate();')
        for i in c:
            print('Date: ',end='')
            print(i[0],'\n') 
        string="select name from movielist where sno="+str(movie_code)+";"
        c.execute(string)
        data=c.fetchone()
        movie_name=data[0]
        print('Movie: ',movie_name,'\n')
        
        print('Seats: ',end='')
        for i in picked_seats:
            print(i, end=' ')
        print() 
        Image=img.imread(movieposterselect(movie_code))
        plt.axis('off')        # displaying the image
        plt.imshow(Image)
        print()
        print('---------------------------------------------------')
        print('Thank you for using Showtime.com! Enjoy your movie :)')
        
    def payment(): #confirming the booking payment
        print('_________________________________________')
        print() 
        if picked_seats==[]:
            print('You did not pick any seats.\nThank you for using Showtime.com !')
        else:
            amount=len(picked_seats)*250
            print('Your total comes to Rupees',amount,'/-')
            
            che=input('Would you like to confirm your payment? Y or N: ')
            if che.lower()=='y':
                print('\nPayment Successful!')
                print(str(amount),'has been deducted from account balance.')
                print('Generating Ticket...')
                ticket()
            elif che.lower()=='n':
                print()
                print('Your booking has been removed. Thank you for your patronage!\nPlease use Showtime.com again!')
            else:
                print('That was Invalid. Try Again.')
                payment() 
    def pickaseat(): #user is allowed to pick their seats 
        print('_________________________________________')
        print()
        print('Click on the seats you want to book') 
        window.title('Pick Your Seats') 
        screen=tk.Label(window, height=2, width=65, text='SCREEN',fg='white', bg='black')
        screen.grid(row=10,column=0, columnspan=15) 
        num=65
        for i in range(1,9):
            for j in range(1,16):
                seat=chr(num)+str(j)
                b = tk.Button(window, height=3, width=5, command=lambda m=seat, i=i, j=j:[booking(m),change(i,j,m)],text=seat)
                b.grid(row=i-1,column=j-1)
            num=num+1 
            confirm=tk.Button(window,command=window.destroy,text='Confirm Seats',bg='red')
        confirm.grid(row=12,column=16) 
        def change(row, column, name):
            b=tk.Button(window,height=3, width=5, bg='green', fg='white', text=name)
            b.grid(row=row-1, column=column-1) 
        window.mainloop()
        print()
        payment() 
    mainmenu()
    print('_________________________________________') 
except Exception as e:
    print(e)
    print('A problem has occured on our ni, Please Try Again Later')
