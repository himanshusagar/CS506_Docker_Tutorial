NO_BACKUP_DIR="/nobackup/$USER/user_data"
mkdir $NO_BACKUP_DIR
chmod 0777 $NO_BACKUP_DIR
setfacl -dm u:hsagar2:rwx $NO_BACKUP_DIR # team member 1 cs login
setfacl -dm u:SOMEUSER2:rwx $NO_BACKUP_DIR # team member 2 cs login
setfacl -dm u:SOMEUSER3:rwx $NO_BACKUP_DIR # team member 3 cs login....and so on.