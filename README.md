# Run test tasks
#### The first two tasks are designed as manage.py commands.
#### Link to the third task: [Third](#Third)
## First
Write a program that takes 4 inputs, where each input consists of 2 numbers in the format x,y. You are required to print a two-dimensional array having x rows and y columns for each input. The elements of the arrays should be whole numbers starting from 1 and incrementing by 1.    
    
Run task `python manage.py arrs`
## Second
Write a program that will accept a sequence of comma-separated transaction passwords and will check them according to the criteria. 
1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
3. At least 1 letter between [A-Z]
4. At least 1 character from [*#+@]
5. Minimum length of transaction password: 4
6. Maximum length of transaction password: 6
7. No space is allowed    

Passwords that match the criteria are to be printed, each separated by a comma.

Run task `python manage.py banks`
## Third
Create a small, working Django site that serves a simple activity feed list with 3 filters:

1. My posts
2. Me and the posts of everyone I’m tracking (note: use an asymmetric relationship, meaning, “Even if I track you, you may or may not track me”.)
3. Everybody’s posts
                        
You can serve `html`, `json`, or `xml`, but there’s no need to groom the output for aesthetics, i.e., don’t spend time on positioning, css, etc. **The goal is to get the backend working**. Create sample data with the admin site; no need for POST or PUT endpoints here. And feel free to pull in whatever Python or Django packages you want. If you do such, please provide a `requirements.txt` with your app code.
                        
To get you started, here’s a Django `models.py` for a basic social network with the asymmetric “tracking” mentioned above.

###### Link: https://softformance-vladrunk-test.herokuapp.com/
   
Access *login:pass* :
   - vladrunk:42    
   - alena_yaloma:42
   - andy_str:42
   - howard_lovecraft:42
   - guido_van_rossum:42