def initialize_db_func(cursor):

    #Database for counter
    cursor.execute("""DROP TABLE IF EXISTS COUNTER""")
    cursor.execute("""CREATE TABLE COUNTER (N INTEGER)""")
    cursor.execute("""INSERT INTO COUNTER (N) VALUES (0)""")

    #Table for GENDER
    cursor.execute("""DROP TABLE IF EXISTS GENDER CASCADE""")
    cursor.execute("""CREATE TABLE GENDER (ID  SERIAL PRIMARY KEY,TYPE character varying(10) NOT NULL )""")
    cursor.execute("""INSERT INTO GENDER ( TYPE) VALUES ('FEMALE' )""")
    cursor.execute("""INSERT INTO GENDER ( TYPE) VALUES ( 'MALE' )""")
    cursor.execute("""INSERT INTO GENDER ( TYPE) VALUES ( 'UNKNOWN' )""")
    #Table for CITY
    cursor.execute("""DROP TABLE IF EXISTS CITY CASCADE""")
    cursor.execute("""CREATE TABLE CITY (ID  SERIAL PRIMARY KEY,CITYNAME character varying(20) NOT NULL )""")
    cursor.execute("""INSERT INTO CITY ( CITYNAME) VALUES ('Istanbul' )""")
    cursor.execute("""INSERT INTO CITY ( CITYNAME) VALUES ( 'Ankara' )""")
    cursor.execute("""INSERT INTO CITY ( CITYNAME) VALUES ( 'Adana' )""")
     #Table for SCHOOL
    cursor.execute("""DROP TABLE IF EXISTS SCHOOL CASCADE""")
    cursor.execute("""CREATE TABLE SCHOOL (ID  SERIAL PRIMARY KEY,SCHOOLNAME character varying(50) NOT NULL )""")
    cursor.execute("""INSERT INTO SCHOOL ( SCHOOLNAME) VALUES ('ITU' )""")
    cursor.execute("""INSERT INTO SCHOOL ( SCHOOLNAME) VALUES ( 'METU' )""")
    cursor.execute("""INSERT INTO SCHOOL ( SCHOOLNAME) VALUES ( 'HACETTEPE UNIVERSITY' )""")
    #Table for user information
    cursor.execute("""DROP TABLE IF EXISTS USERS CASCADE""")
    cursor.execute("""CREATE TABLE USERS (ID SERIAL PRIMARY KEY UNIQUE,
                                          USERNAME VARCHAR(50) UNIQUE NOT NULL ,
                                         NAME VARCHAR(50) NOT NULL,
                                         SURNAME VARCHAR(50) NOT NULL,
                                         MAIL VARCHAR(50) UNIQUE NOT NULL,
                                         GENDER INTEGER  references GENDER(ID),
                                         SCHOOL INTEGER  references SCHOOL(ID),
                                         CITY INTEGER  references CITY(ID))""")

    cursor.execute("""INSERT INTO USERS (USERNAME, NAME, SURNAME, MAIL, GENDER, SCHOOL, CITY) VALUES ('ali',
                                                                                                    'Ali',
                                                                                                    'ERCAN',
                                                                                                    'aliercan@gmail.com',
                                                                                                    2,
                                                                                                    1,
                                                                                                    3)""")
    cursor.execute("""INSERT INTO USERS (USERNAME, NAME, SURNAME, MAIL, GENDER, SCHOOL, CITY) VALUES ('dincer',
                                                                                                    'DINCER',
                                                                                                    'ADANALI',
                                                                                                    'dincertarbil@gmail.com',
                                                                                                    2,
                                                                                                    1,
                                                                                                    2)""")
    cursor.execute("""INSERT INTO USERS (USERNAME, NAME, SURNAME, MAIL, GENDER, SCHOOL, CITY) VALUES ('bsk125',
                                                                                                    'BASAK',
                                                                                                    'KURTUL',
                                                                                                    'baskkurtul@gmail.com',
                                                                                                    1,
                                                                                                    3,
                                                                                                    1)""")
    cursor.execute("""INSERT INTO USERS (USERNAME, NAME, SURNAME, MAIL, GENDER, SCHOOL, CITY) VALUES ('merv',
                                                                                                    'MERVE',
                                                                                                    'DOGAN',
                                                                                                    'mervdgan@gmail.com',
                                                                                                    1,
                                                                                                    2,
                                                                                                    3)""")
    cursor.execute("""INSERT INTO USERS (USERNAME, NAME, SURNAME, MAIL, GENDER, SCHOOL, CITY) VALUES ('sedt01',
                                                                                                    'Sedat',
                                                                                                    'Selman',
                                                                                                    'sedatselmn@gmail.com',
                                                                                                    2,
                                                                                                    2,
                                                                                                    2)""")


    #Table for user login
    cursor.execute("""DROP TABLE IF EXISTS USERLOGIN CASCADE""")
    cursor.execute("""CREATE TABLE USERLOGIN (USERNAME VARCHAR(50)  PRIMARY KEY  references users(username),
                                               PASSWORD VARCHAR(50) NOT NULL,
                                               LASTLOGIN VARCHAR(50))""")

    cursor.execute("""INSERT INTO USERLOGIN (USERNAME, PASSWORD) VALUES ('ali','password')""")
    cursor.execute("""INSERT INTO USERLOGIN (USERNAME, PASSWORD) VALUES ('dincer','password')""")
    cursor.execute("""INSERT INTO USERLOGIN (USERNAME, PASSWORD) VALUES ('bsk125','password')""")
    cursor.execute("""INSERT INTO USERLOGIN (USERNAME, PASSWORD) VALUES ('merv','password')""")
    cursor.execute("""INSERT INTO USERLOGIN (USERNAME, PASSWORD) VALUES ('sedt01','password')""")

    #Table for main
    cursor.execute("""DROP TABLE IF EXISTS PostForView""")
    cursor.execute("""CREATE TABLE PostForView(ID CHAR(20) NOT NULL, FID CHAR(20), POSTID Char(10) )""")
    cursor.execute("""INSERT INTO PostForView (ID, FID, POSTID) VALUES ('2', '5', '1' )""")
    cursor.execute("""INSERT INTO PostForView (ID, FID, POSTID) VALUES ('2', '3', '4' )""")

    #Table for explore
    cursor.execute("""DROP TABLE IF EXISTS hashTag""")
    cursor.execute("""CREATE TABLE hashTag (HASHID CHAR(20) NOT NULL, GRUPNAME CHAR(20) )""")
    cursor.execute("""INSERT INTO hashTag (HASHID, GRUPNAME) VALUES ('2', 'NATURE' )""")
    cursor.execute("""INSERT INTO hashTag (HASHID, GRUPNAME) VALUES ('5', 'FUTBOL')""")
    cursor.execute("""INSERT INTO hashTag (HASHID, GRUPNAME) VALUES ('6', 'NATURE' )""")
    cursor.execute("""INSERT INTO hashTag (HASHID, GRUPNAME) VALUES ('9', 'ART')""")

    #Table for picture-post//not active just trying
    cursor.execute("""DROP TABLE IF EXISTS picPost""")
    cursor.execute("""CREATE TABLE picPost (PicId  SERIAL PRIMARY KEY,Description CHAR(20) )""")
    cursor.execute("""INSERT INTO picPost ( Description) VALUES ('School')""")
    cursor.execute("""INSERT INTO picPost ( Description) VALUES ('With My Friends')""")
    cursor.execute("""INSERT INTO picPost ( Description) VALUES ('Enjoy')""")
    #Table for Profil PICTURE
    cursor.execute("""DROP TABLE IF EXISTS PROFILEPIC CASCADE""")
    cursor.execute("""CREATE TABLE PROFILEPIC (USERID INTEGER PRIMARY KEY references USERS(ID),LINK character varying(255) NOT NULL )""")
    cursor.execute("""INSERT INTO PROFILEPIC (USERID, LINK) VALUES (1,'http://laelith.fr/Cours/Illus/013-avatar-faceprofil.jpg')""")
    cursor.execute("""INSERT INTO PROFILEPIC (USERID, LINK) VALUES (2,'http://laelith.fr/Cours/Illus/013-Me.jpg' )""")
    cursor.execute("""INSERT INTO PROFILEPIC (USERID, LINK) VALUES (3,'http://www.hastane.com.tr/Images/Article/daha-iyi-bir-profil-icin-cene-ucu-estetigi_b.jpg' )""")
    cursor.execute("""INSERT INTO PROFILEPIC (USERID, LINK) VALUES (4,'https://s-media-cache-ak0.pinimg.com/originals/a3/fa/d3/a3fad3bd611a6f08d4ac0fa308cad22c.jpg' )""")
    cursor.execute("""INSERT INTO PROFILEPIC (USERID, LINK) VALUES (5,'http://tamirciarchitects.com/wp-content/uploads/2012/07/profil.jpg' )""")
     #Table for POST table
    cursor.execute("""DROP TABLE IF EXISTS POSTS CASCADE""")
    cursor.execute("""CREATE TABLE POSTS (ID SERIAL PRIMARY KEY UNIQUE,
                                            USERID INTEGER  references USERS(ID),
                                            DATE character varying(50) ,
                                            LINK character varying(255) NOT NULL,
                                            DESCRIPTION character varying(255))""")
    cursor.execute("""INSERT INTO POSTS (USERID, DATE,LINK,DESCRIPTION) VALUES (3,'2016-11-27 16:05:25','http://images.freeimages.com/images/previews/fcb/feeling-down-at-the-park-1432442.jpg','PARK' )""")
    cursor.execute("""INSERT INTO POSTS (USERID, DATE,LINK,DESCRIPTION) VALUES (1,'2016-11-28 17:25:55','http://images.freeimages.com/images/premium/large-thumbs/1870/18706766-hikers-enjoy-the-freedom.jpg','Freedom' )""")
    cursor.execute("""INSERT INTO POSTS (USERID, DATE,LINK,DESCRIPTION) VALUES (3,'2016-11-28 18:34:51','http://images.freeimages.com/images/premium/large-thumbs/1539/15397320-sad-black-man.jpg','Sadness' )""")
    cursor.execute("""INSERT INTO POSTS (USERID, DATE,LINK,DESCRIPTION) VALUES (2,'2016-11-28 22:13:42','http://www.freeimageslive.com/galleries/sports/sportsgames/preview/cricket_ball.jpg','Cricket' )""")
    cursor.execute("""INSERT INTO POSTS (USERID, DATE,LINK,DESCRIPTION) VALUES (3,'2016-11-29 08:45:33','http://www.freeimages.co.uk/galleries/sports/sportsgames/thumbs/extreme_unicycle.jpg','Unicycle' )""")
    cursor.execute("""INSERT INTO POSTS (USERID, DATE,LINK,DESCRIPTION) VALUES (2,'2016-11-29 21:24:11','http://www.freeimageslive.com/galleries/sports/moods%20emotions/preview/beach_sands_breakersP1013474.jpg','Beach' )""")
    cursor.execute("""INSERT INTO POSTS (USERID, DATE,LINK,DESCRIPTION) VALUES (5,'2016-12-02 18:24:25','http://www.photographyblogger.net/wp-content/uploads/2013/04/nature02.jpg','Nature' )""")
    cursor.execute("""INSERT INTO POSTS (USERID, DATE,LINK,DESCRIPTION) VALUES (4,'2016-12-03 21:24:23','http://phoenixrising.me/wp-content/uploads/pixabay-silhouette-woman-meditation.jpg','Meditation' )""")
    cursor.execute("""INSERT INTO POSTS (USERID, DATE,LINK,DESCRIPTION) VALUES (4,'2016-12-04 02:57:22','http://www.freeimageslive.com/galleries/transtech/electronics/pics/03250021.jpg','Tech' )""")
    cursor.execute("""INSERT INTO POSTS (USERID, DATE,LINK,DESCRIPTION) VALUES (1,'2016-12-04 23:28:11','http://www.freeimageslive.com/galleries/transtech/electronics/pics/smtintegratedcircuit2288.jpg','Chip' )""")
    cursor.execute("""INSERT INTO POSTS (USERID, DATE,LINK,DESCRIPTION) VALUES (5,'2016-12-05 21:24:11','http://www.freeimageslive.com/galleries/transtech/objects/pics/injection.jpg','InjectionTime' )""")

    #Table for Hidden Posts
    cursor.execute("""DROP TABLE IF EXISTS HIDDENPOSTS CASCADE""")
    cursor.execute("""CREATE TABLE HIDDENPOSTS (USERID INTEGER  references USERS(ID),
                                            POSTID INTEGER PRIMARY KEY UNIQUE references POSTS(ID))""")
    cursor.execute("""INSERT INTO HIDDENPOSTS (USERID, POSTID) VALUES (3,3)""")

    #Table For Follow
    cursor.execute("""DROP TABLE IF EXISTS FOLLOW CASCADE""")
    cursor.execute("""CREATE TABLE FOLLOW (FOLLOWER  INTEGER references USERS(ID),
                                            FOLLOWING  INTEGER references USERS(ID),
                                            PRIMARY KEY(FOLLOWER,FOLLOWING),
                                            CHECK (FOLLOWING !=FOLLOWER))""")
    cursor.execute("""INSERT INTO FOLLOW (FOLLOWER, FOLLOWING) VALUES (1,2)""")
    cursor.execute("""INSERT INTO FOLLOW (FOLLOWER, FOLLOWING) VALUES (2,3)""")
    cursor.execute("""INSERT INTO FOLLOW (FOLLOWER, FOLLOWING) VALUES (2,1)""")
    cursor.execute("""INSERT INTO FOLLOW (FOLLOWER, FOLLOWING) VALUES (1,3)""")
    cursor.execute("""INSERT INTO FOLLOW (FOLLOWER, FOLLOWING) VALUES (3,2)""")
    cursor.execute("""INSERT INTO FOLLOW (FOLLOWER, FOLLOWING) VALUES (5,2)""")
    cursor.execute("""INSERT INTO FOLLOW (FOLLOWER, FOLLOWING) VALUES (5,3)""")
    cursor.execute("""INSERT INTO FOLLOW (FOLLOWER, FOLLOWING) VALUES (5,4)""")
    cursor.execute("""INSERT INTO FOLLOW (FOLLOWER, FOLLOWING) VALUES (4,2)""")
    cursor.execute("""INSERT INTO FOLLOW (FOLLOWER, FOLLOWING) VALUES (4,1)""")
    cursor.execute("""INSERT INTO FOLLOW (FOLLOWER, FOLLOWING) VALUES (1,5)""")
    cursor.execute("""INSERT INTO FOLLOW (FOLLOWER, FOLLOWING) VALUES (2,4)""")
    cursor.execute("""INSERT INTO FOLLOW (FOLLOWER, FOLLOWING) VALUES (3,5)""")

    cursor.execute("""DROP TABLE IF EXISTS postComments CASCADE;
                        CREATE TABLE postComments
                        (
                            id SERIAL PRIMARY KEY NOT NULL,
                            postId INT NOT NULL,
                            userId INT NOT NULL,
                            comment VARCHAR(255) NOT NULL
                        );

                        CREATE INDEX postc_id ON postComments USING btree (postId);
                        ALTER TABLE ONLY postComments
                            ADD CONSTRAINT fkPostId FOREIGN KEY (postId) REFERENCES posts(id) DEFERRABLE INITIALLY DEFERRED;

                        CREATE INDEX userc_id ON postComments USING btree (userId);
                        ALTER TABLE ONLY postComments
                            ADD CONSTRAINT fkUserId FOREIGN KEY (userId) REFERENCES users(id) DEFERRABLE INITIALLY DEFERRED;

                        DROP TABLE IF EXISTS postLikes CASCADE;
                        DROP TYPE IF EXISTS likeType;
                        CREATE TYPE likeType AS ENUM ('heart', 'thumbs-up', 'thumbs-down', 'frown-o');
                        CREATE TABLE postLikes
                        (
                            id SERIAL PRIMARY KEY NOT NULL,
                            postId INT NOT NULL,
                            userId INT NOT NULL,
                            likeType VARCHAR(255) NOT NULL
                        );

                        CREATE INDEX postl_id ON postLikes USING btree (postId);
                        ALTER TABLE ONLY postLikes
                            ADD CONSTRAINT fkPostId FOREIGN KEY (postId) REFERENCES posts(id) DEFERRABLE INITIALLY DEFERRED;

                        CREATE INDEX userl_id ON postLikes USING btree (userId);
                        ALTER TABLE ONLY postLikes
                            ADD CONSTRAINT fkUserId FOREIGN KEY (userId) REFERENCES users(id) DEFERRABLE INITIALLY DEFERRED;

                        DROP TABLE IF EXISTS interests CASCADE;
                        CREATE TABLE interests
                        (
                            id SERIAL PRIMARY KEY NOT NULL,
                            userId INT NOT NULL,
                            interest VARCHAR(255) NOT NULL
                        );

                        CREATE INDEX useri_id ON interests USING btree (userId);
                        ALTER TABLE ONLY interests
                            ADD CONSTRAINT fkUserId FOREIGN KEY (userId) REFERENCES users(id) DEFERRABLE INITIALLY DEFERRED;

""")
