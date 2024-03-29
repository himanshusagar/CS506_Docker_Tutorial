# COMP SCI 506 Docker End to End Tutorial

Other tutorials in this repo: 
1. Basics Tutorials inside basics folder.
2. MySQL DB tutorial inside db folder. 

# Objective:
To demonstrate developing docker containers for different comporents of web application - Backend and Database.

I will create an example backend application and database for tutorial. CS 506 students may want to use their own application for this. 

# hs_app 

Go inside hs_app folder and look at all the files.

1. Backend has `Dockerfile`, `requirements.txt` and `app.py`. Your backend could very well be in python or JS or some other language. It might also have different set of files but porting it to docker should be similar.
2. MySQL DB is entirely configured using Dockefile.
3. There's extra `phpmyadmin` image which just exists for visual representaion for DB. This is optional though.
   
## Notice:
1. In `docker-compose.yml`, DB's data `/var/lib/mysql` of container is mapped to `/nobackup/$USER/user_data` using named volume. Thus everything inside var folder will be copied automatically to user_data folder. 
2. In `give_perms.sh`, we're creating a folder and giving all permissons(read, write and execute) to all users. After that, we specifically provide access to team members.  
3. In Dockerfile, we install alpine linux packages required by `requirements.txt`. 
 
# Running Application
0. Replace `hsagar2` with your own cs login as we go through various files. 
1. Modify `give_perms.sh` to include your and team members' cs logins. You can also change `user_data` to some other folder name if you'd like. Rest of the stuff stays same. 
2. `bash give_perms.sh` to run shell script.
3. Build image using `docker build -t my-flask-app`
4. Build compose file using `docker compose up .` 
5. Now our setup is running in `cs-team-xx` machine but we need to port forward backend and phpmyadmin to it to be seen on local machine(personal laptop).
6. For backend(flask application) : `ssh -L 8000:cs506-team-00.cs.wisc.edu:8000 hsagar2@cs506-team-00.cs.wisc.edu`
For phpmyadmin (Optional) : `ssh -L 8082:cs506-team-00.cs.wisc.edu:8082 hsagar2@cs506-team-00.cs.wisc.edu`
7. For pruning images : `docker system prune -a` 
8. For pruning images and volumes : `docker system prune -a --volumes` 
