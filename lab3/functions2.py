movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

#ex 1
def imdb(d):
    if d>5.5:
        return True
    
for i in movies:
    print(imdb(i["imdb"]))
   
#ex 2
def imdb_above_5_5(movie):
    if movie["imdb"] > 5.5:
        return movie


for movie in movies:
    print(imdb_above_5_5(movie))

#ex 3
def rm(s):
    m= []
    for movie in movies:
        if movie["category"] == s:
            m.append(movie["name"])
    return m

s = input()
print(rm(s))

#ex 4
def av(d):
    s = 0
    for i in movies:
        s+= i["imdb"]
    return s / len(movies)


s1= av(movies)
print(s1)

#ex 5 
def rm(s1):
    s2=0
    s3=0
    for i in movies:
        if s1==i["category"]:
            s2+=i["imdb"]
            s3+=1
    return s2/s3

s1 = input()
print(rm(s1))