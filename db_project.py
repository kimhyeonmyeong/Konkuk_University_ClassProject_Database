# -*- coding: utf-8 -*-
import csv
import pymysql

"""
conn = pymysql.connect( host = 'localhost', user='root', password = 'gusaud123', db='db_201814117')    
curs = conn.cursor()
sql = "insert into User(UserID, Age, Gender, Occupation, Zipcode) values (%s, %s, %s, %s, %s)"
f = open('C:\\Users\\USER\\.spyder-py3\\u.user.tsv', 'r', encoding = 'utf-8')
rd = csv.reader(f, delimiter = '|')

#for line in rd:
    #print(line[0], line[1], line[2], line[3], line[4])
    
for line in rd:
    curs.execute(sql, (line[0], line[1], line[2], line[3], line[4] ))
    

conn.commit()
conn.close()
f.close()

#f.close()

conn = pymysql.connect( host = 'localhost', user='root', password = 'gusaud123', db='db_201814117')    
curs = conn.cursor()
sql = "insert into Movie(MovieID , MovieTitle, Releasedate, IMDbURL) values (%s, %s, %s, %s)"
f = open('C:\\Users\\USER\\.spyder-py3\\u.item.tsv', 'r', encoding = 'utf-8')
rd = csv.reader(f, delimiter = '|')

#for line in rd:
    #print(line[5], line[23]  )

    
for line in rd:
    curs.execute(sql, (line[0], line[1], line[2], line[4] ))


conn.commit()
curs.close()
conn.close()

f.close()



conn = pymysql.connect( host = 'localhost', user='root', password = 'gusaud123', db='db_201814117')    
curs = conn.cursor()
sql = "insert into Movie_Genre(MovieID, Movietitle, MovieGenre) values (%s, %s, %s)"
f = open('C:\\Users\\USER\\.spyder-py3\\u.item.tsv', 'r', encoding = 'utf-8')
rd = csv.reader(f, delimiter = '|')

list_genre = ['unknown', 'action', 'adventure', 'animation', 'children', 'comedy', 'crime', 'documentary',
              'drama', 'fantasy', 'film-noir', 'horror', 'musical', 'mystery', 'romance', 'sci-fi', 'thriller',
              'war', 'western']

list_make_g = [' ' for _ in range(19)];


num = 0

for line in rd:
    for i in range(5, 24):
        
        if(line[i] == '1'):
            list_make_g[num]= list_genre[num]
        num += 1

    num =  0
    genre = ' '.join(list_make_g).split()
    genre = ','.join(genre)
    #print(genre)
    curs.execute(sql,(line[0], line[1], genre))
    list_make_g = [' ' for _ in range(19)];


        
#for line in rd:
    #curs.execute(sql, (line[0], line[1], line[2], line[4] ))


conn.commit()
conn.close()
curs.close()
f.close()




conn = pymysql.connect( host = 'localhost', user='root', password = 'gusaud123', db='db_201814117')    
curs = conn.cursor()
sql = "insert into User_Movie_Rating(UserID, MovieID, Rating) values (%s, %s, %s)"
f = open('C:\\Users\\USER\\.spyder-py3\\u.data.tsv', 'r', encoding = 'utf-8')
rd = csv.reader(f, delimiter = '\t')


num = 0

#for line in rd:
    #print(line[0], line[1], line[2])

    
for line in rd:
    curs.execute(sql, (line[0], line[1], line[2]))


        
#for line in rd:
    #curs.execute(sql, (line[0], line[1], line[2], line[4] ))


conn.commit()
conn.close()
curs.close()
f.close()

"""

#사용자 입력 함수들
def show_menu():
    
    print("*************")
    print("*1: 영화검색 *")
    print("*2: 종료하기 *")
    print("*************")
    
    print("원하는 기능을 선택하세요")

def genre_input():
    
    print("************************************")
    print("*      영화 장르를 입력해주세요      *")
    print("*  (반영하기 싫다면 x를 입력하세요)  *")
    print("*   _______검색가능 장르___________ *")
    print("*  ┃Action  Adventure  Animation ┃ *")
    print("*  ┃Children\'s Comedy  Crime     ┃ *")
    print("*  ┃Documentary  Drama  Fantasy  ┃ *")
    print("*  ┃Film-Noir  Horror   Musical  ┃ *")
    print("*  ┃Mystery   Romance   Sci-Fi   ┃ *")
    print("*  ┃Thriller    War     Western  ┃ *")
    print("*  ￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣ *")
    print("************************************")
    genre_i = input("입력:" ) 
    return genre_i
    
def occupation_input():
    
    print("**************************************")
    print("*    귀하의 직업을 입력해주세요        *")
    print("*  (반영하기 싫다면 x를 입력하세요)    *")
    print("*   _______검색가능 직업_____________ *")
    print("*  ┃Administer  Artist  Doctor     ┃ *")
    print("*  ┃Educator Engineer Entertainment┃ *")
    print("*  ┃Executive Healthcare Homemaker ┃ *")
    print("*  ┃Lawyer   Librarian  Marketing  ┃ *")
    print("*  ┃None     Other     Programmer  ┃ *")
    print("*  ┃Retired   Salesman    Scientist┃ *")
    print("*  ┃Student  Technician   Writer   ┃ *")
    print("*  ￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣ *")
    print("**************************************")
    occ_i = input("입력:" )
    return occ_i


def rating_input():
    
    
    print("**************************************")
    print("*  원하는 평점(평균)범위를 입력하세요   *")
    print("*  (반영하기 싫다면 x를 입력하세요)    *")
    print("*   _________영화 평점 범위__________ *")
    print("*  ┃                               ┃ *")
    print("*  ┃  입력하신 평점(평균)의          ┃ *")
    print("*  ┃  Min ~ Max 사이의 영화를 검색  ┃ *")
    print("*  ┃                               ┃ *")
    print("*  ┃                               ┃ *")
    print("*  ┃                               ┃ *")
    print("*  ┃                               ┃ *")
    print("*  ￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣ *")
    print("**************************************")
    Min_i = input("Min(1~5) or x:" )
    Max_i = input("Max(1~5) or x:" )
    
    if Min_i == 'x':
        Min_i = 0
    else:
        Min_i = float(Min_i)
    
    if Max_i == 'x':
        Max_i = 5
    else:
        Max_i = float(Max_i)
        
    return Min_i, Max_i
    


def sorting_input():
    
    print("**************************************")
    print("*    원하는 검색 정렬을 입력하세요     *")
    print("*    (필수 입력입니다.)               *")
    print("*   _________영화 평점 범위__________ *")
    print("*  ┃                               ┃ *")
    print("*  ┃  1. 영화 제목순으로 검색하기    ┃ *")
    print("*  ┃  2. 평균 평점순으로 검색하기    ┃ *")
    print("*  ┃  3. Vote 순으로 검색하기       ┃ *")
    print("*  ┃     (영화당 평점 매긴 사람 수)  ┃ *")
    print("*  ┃                               ┃ *")
    print("*  ┃                               ┃ *")
    print("*  ￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣ *")
    print("**************************************")
    Order_i_n = int(input("(1~3)입력:" ))
    
    while True:
        
        if Order_i_n == 1:
            order_i = 'MovieTitle'
            return order_i
            break;
        elif Order_i_n == 2:
            order_i = 'avg(rating)'
            return order_i
            break;
        elif Order_i_n == 3:
            order_i = 'Vote'
            return order_i
            break;
        else:
            print("1~3 정수 값을 다시 입력하세요")
            Order_i_n = int(input("(1~3)입력: "))
            
            
# 검색 조건에 따른 동작 함수들     
def genre_occ_x(Min_i, Max_i, order_i):

    conn = pymysql.connect( host = 'localhost', user='root', password = 'gusaud123', db='db_201814117')    
    curs = conn.cursor()
    
    
    sql = """select r.MovieID, g.Movietitle, g.MovieGenre, avg(rating) as AVG_rating, COUNT(distinct r.userid) as Vote
    from Movie m, User u, User_movie_Rating r, Movie_Genre g
    where m.movieid = r.movieid AND r.movieid= g.movieid AND m.movieid = g.movieid
    AND r.userid = u.userid
    Group by movieid
    HAVING avg(rating) >= %f AND avg(rating) <= %f
    Order by %s desc""" %(Min_i, Max_i, order_i)
        
      
    curs.execute(sql)
    row = curs.fetchone()
    
    while row:
         print("MOVIEID, MOVIETITLE, MOVIEGENRE, AVG_RATING, VOTE")
         print(row)
         row = curs.fetchone()
     
     
    conn.commit()
    curs.close()
    conn.close()

def genre_x_occ_o(occ_i, Min_i, Max_i, order_i):

    conn2 = pymysql.connect( host = 'localhost', user='root', password = 'gusaud123', db='db_201814117')    
    curs2 = conn2.cursor()
    
    
    sql = """select u.UserID,u.Occupation, r.MovieID, g.Movietitle, g.MovieGenre, avg(rating) as AVG_rating, COUNT(distinct r.userid) as Vote
    from Movie m, User u, User_movie_Rating r, Movie_Genre g
    where m.movieid = r.movieid AND r.movieid= g.movieid AND m.movieid = g.movieid
    AND r.userid = u.userid AND u.userid IN (select userid from user where user.Occupation ='%s')
    Group by movieid
    HAVING avg(rating) >= %f AND avg(rating) <= %f
    Order by %s desc """ %(occ_i, Min_i, Max_i, order_i)
                 
    curs2.execute(sql)
    row = curs2.fetchone()
    
    while row:
         print("USERID, U.OCCUPATION, MOVIEID, MOVIETITLE, MOVIEGENRE, AVG_RATING, VOTE")
         print(row)
         row = curs2.fetchone()
     
     
    conn2.commit()
    curs2.close()
    conn2.close()


def genre_o_occ_x(genre_i, Min_i, Max_i, order_i):

    conn3 = pymysql.connect( host = 'localhost', user='root', password = 'gusaud123', db='db_201814117')    
    curs3 = conn3.cursor()
    
    
    sql = """select r.MovieID, g.Movietitle, g.MovieGenre, avg(rating) as AVG_rating, COUNT(distinct r.userid) as Vote
    from Movie m, User u, User_movie_Rating r, Movie_Genre g
    where m.movieid = r.movieid AND r.movieid= g.movieid AND m.movieid = g.movieid AND g.movieid IN (select movieid from movie_genre where moviegenre like '%%%s%%')
    AND r.userid = u.userid
    Group by movieid
    HAVING avg(rating) >= %f AND avg(rating) <=%f
    Order by %s desc """ %(genre_i, Min_i, Max_i, order_i)
                
    
    curs3.execute(sql)
    row = curs3.fetchone()
    
    while row:
         print("MOVIEID, MOVIETITLE, MOVIEGENRE, AVG_RATING, VOTE")
         print(row)
         row = curs3.fetchone()
     
     
    conn3.commit()
    curs3.close()
    conn3.close()
    
def genre_o_occ_o(genre_i, occ_i, Min_i, Max_i, order_i):

    conn4 = pymysql.connect( host = 'localhost', user='root', password = 'gusaud123', db='db_201814117')    
    curs4 = conn4.cursor()
    
    
    sql = """select u.UserID, u.Occupation, r.MovieID, g.Movietitle, g.MovieGenre, avg(rating) as AVG_rating, COUNT(distinct r.userid) as Vote
    from Movie m, User u, User_movie_Rating r, Movie_Genre g
    where m.movieid = r.movieid AND r.movieid= g.movieid AND m.movieid = g.movieid AND g.movieid IN (select movieid from movie_genre where moviegenre like '%%%s%%')
    AND r.userid = u.userid AND u.userid IN (select userid from user where user.occupation = '%s')
    Group by movieid
    HAVING avg(rating) >= %f AND avg(rating) <=%f
    Order by %s desc""" %(genre_i, occ_i, Min_i, Max_i, order_i)
                    
        
    curs4.execute(sql)
    row = curs4.fetchone()
    
    while row:
         print("USERID, U.OCCUPATION, MOVIEID, MOVIETITLE, MOVIEGENRE, AVG_RATING, VOTE")
         print(row)

         row = curs4.fetchone()
     
     
    conn4.commit()
    curs4.close()
    conn4.close()
    
#메인 구역
while True:
    
    show_menu()

        
    menuNum= int(input("입력(1~2): "))
    
    if menuNum == 1:
        #사용자 입력 함수들로부터 장르,직업,평점,정렬조건등을 받는다.
        genre_i = genre_input()
        occ_i = occupation_input()
        Min_i, Max_i = rating_input()
        order_i = sorting_input()
        
        if genre_i == 'x' and occ_i =='x':
            genre_occ_x(Min_i, Max_i, order_i)
            
        elif genre_i == 'x' and occ_i != 'x':
            genre_x_occ_o(occ_i, Min_i, Max_i, order_i)

        elif genre_i != 'x' and occ_i =='x':
            genre_o_occ_x(genre_i, Min_i, Max_i, order_i)

        else:
            genre_o_occ_o(genre_i, occ_i, Min_i, Max_i, order_i)        
    
    #프로그램 종료    
    elif menuNum == 2:
        break;
    else:
        print("1,2 중에서 입력해주세요")

"""
conn = pymysql.connect( host = 'localhost', user='root', password = 'gusaud123', db='db_201814117')    
curs = conn.cursor()

a='comedy'
b='doctor'
c= 1
d= 4
e = 'Vote'

sql = select u.UserID, u.Occupation, r.MovieID, g.Movietitle, g.MovieGenre, avg(rating) as AVG_rating, COUNT(distinct r.userid) as Vote
from Movie m, User u, User_movie_Rating r, Movie_Genre g
where m.movieid = r.movieid AND r.movieid= g.movieid AND m.movieid = g.movieid AND g.movieid IN (select movieid from movie_genre where moviegenre like '%%%s%%')
AND r.userid = u.userid AND u.userid IN (select userid from user where user.Occupation = '%s')
Group by r.movieid
HAVING avg(rating) >= %d AND avg(rating) <=%d
Order by '%s' desc %(a,b,c,d,e)

#for line in rd:
    #print(line[0], line[1], line[2], line[3], line[4])
    
curs.execute(sql)
row = curs.fetchone()

while row:
     print(row)
     row = curs.fetchone()
     
     
conn.commit()
curs.close()
conn.close()

"""
