How to run sql locally:

```bash
# database
docker run -it -e MYSQL_ROOT_PASSWORD=on -v sql_database:/var/lib/mysql mysql
# attacker
docker run -it -e MYSQL_ROOT_PASSWORD=on mysql /bin/bash
mysql -h 172.17.0.2
use dolbydb
```
