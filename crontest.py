from crontab import CronTab

cron = CronTab(user='karthik') 
job  = cron.new(command='python /home/karthik/Latest/Agni-1/clean1.py')
job.minute.every(1)
job.enable()
cron.write( 'output.tab' )
