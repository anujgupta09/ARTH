import os
import getpass
import subprocess as sp

########################################################################################
def hadoop():

		###### function of hadoop ######

	def DN():
		NNip=input("enter ip of namenode")
		DNdir=input("enter DN directory name")
		os.system("tput setaf 1")
		print("""\tpre-requisite 2 softwear :
		\tjdk-8u171-linux-x64.rpm & hadoop-1.2.1-1.x86_64.rpm\n\n			
		""")
		os.system("tput setaf 5")

		os.system("systemctl stop firewalld && systemctl disable firewalld && setenforce 0")
		os.system("rpm -ivh jdk-8u171-linux-x64.rpm" )
		os.system("rpm -ivh hadoop-1.2.1-1.x86_64.rpm --force" )
		
		f1=open("/etc/hadoop/core-site.xml","r+")
		f1.truncate(0)
		f1.close()
		f2=open("/etc/hadoop/core-site.xml","w+")
		f2.write("""<?xml version="1.0"?>
	<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

	<!-- Put site-specific property overrides in this file. -->

	<configuration>
	<property>
	<name>fs.default.name</name>
	<value>hdfs://{}:9001</value>
	</property>
	</configuration>""".format(NNip))
		f2.close()

		f3=open("/etc/hadoop/hdfs-site.xml","r+")
		f3.truncate(0)
		f3.close()	

		f4=open("/etc/hadoop/hdfs-site.xml","w+")
		f4.write("""<?xml version="1.0"?>
	<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

	<!-- Put site-specific property overrides in this file. -->

	<configuration>
	<property>
	<name>dfs.data.dir</name>
	<value>{}</value>
	</property>
	</configuration>""".format(DNdir))
		f4.close()
		os.system("mkdir {}".format(DNdir))
		os.system("hadoop-daemon.sh start datanode")
		os.system("jps")
	
	def NN():	
		NNdir=input("enter NN directory name")
		os.system("tput setaf 1")
		print("""\tpre-requisite 2 softwear :
		\tjdk-8u171-linux-x64.rpm & hadoop-1.2.1-1.x86_64.rpm\n\n			
		""")
		os.system("tput setaf 5")

		os.system("systemctl stop firewalld && systemctl disable firewalld && setenforce 0")

		os.system("rpm -ivh jdk-8u171-linux-x64.rpm" )
		os.system("rpm -ivh hadoop-1.2.1-1.x86_64.rpm --force" )
		
		f1=open("/etc/hadoop/core-site.xml","r+")
		f1.truncate(0)
		f1.close()
		f2=open("/etc/hadoop/core-site.xml","w+")
		f2.write("""<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>fs.default.name</name>
<value>hdfs://0.0.0.0:9001</value>
</property>
</configuration>""")
		f2.close()

		f3=open("/etc/hadoop/hdfs-site.xml","r+")
		f3.truncate(0)
		f3.close()	

		f4=open("/etc/hadoop/hdfs-site.xml","w+")
		f4.write("""<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>dfs.name.dir</name>
<value>{}</value>
</property>
</configuration>""".format(NNdir))
		f4.close()
		os.system("mkdir {}".format(NNdir))
		os.system("hadoop namenode -format")
		os.system("hadoop-daemon.sh start namenode")
		os.system("jps")

	def client():
		NNip=input("enter ip of namenode")
		os.system("tput setaf 1")
		print("""\tpre-requisite 2 softwear :
		\tjdk-8u171-linux-x64.rpm & hadoop-1.2.1-1.x86_64.rpm\n\n			
		""")
		os.system("tput setaf 5")

		os.system("systemctl stop firewalld && systemctl disable firewalld && setenforce 0")

		os.system("rpm -ivh jdk-8u171-linux-x64.rpm" )
		os.system("rpm -ivh hadoop-1.2.1-1.x86_64.rpm --force" )
		
		f1=open("/etc/hadoop/core-site.xml","r+")
		f1.truncate(0)
		f1.close()
		f2=open("/etc/hadoop/core-site.xml","w+")
		f2.write("""<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>fs.default.name</name>
<value>hdfs://{}:9001</value>
</property>
</configuration>""".format(NNip))
		f2.close()
		os.system("jps")

		################ calling hadoop functions ############################

	
	os.system("tput setaf 1")
	print("""
	\t\tMenu (hadoop) : 
	\t\tnote(java and hadoop soft required in /root folder)
	\t\tpress 1 : to setup datanode in system
	\t\tpress 2 : to setup namenode in system
	\t\tpress 3 : to setup client in system	
	""")
	os.system("tput setaf 5")
	op=int(input("Enter your choice -->"))

	if op==1:
		DN()
	elif op==2:
		NN()
	elif op==3:#
		client()
#######################################################################################
def remote():
		os.system("clear")

		ip = input("Enter the remote IP-")
		while True :
			print("""
			Enter your choice:
			Press 1 : to see IP
			Press 2 : to open calender
			Press 3 : to launch new OS with docker 
			Press 4 : to use hadoop service 
			Press 5 : to use webservice
			Press 6 : to manage firewall service 
			Press 7 : to configure yum
			Press 8 : to create partition
			Press 9 : to exit
			
				""")	
			x=input()

			
			if int(x)==1:
				os.system("tput setaf 50")
				os.system("ssh {} ifconfig enp0s3".format(ip))
				os.system("tput setaf 2")
				
			elif int(x)==2:
				os.system("tput setaf 50")
				os.system("ssh {} cal".format(ip))
				os.system("tput setaf 2")
			elif int(x)==3:
				os.system("tput setaf 50")
				os.system("tput setaf 1")
				print("By default OS 'ubuntu:14.04' will be installed")
				os.system("tput setaf 5")
				os.system('ssh {} docker --version'.format(ip))
				os.system('ssh {} yum install docker-ce --nobest'.format(ip))
				os.system('ssh {} systemctl start docker'.format(ip))
				os.system('ssh {} docker pull ubuntu:14.04'.format(ip))
				os.system("tput setaf 1")
				print("This is your 'ubuntu:14.04' OS :::")
				os.system("tput setaf 5")
				os.system('ssh {} docker run -it ubuntu:14.04'.format(ip))
				os.system("tput setaf 2")
			elif int(x)==4:
				os.system("tput setaf 50")
				os.system("ssh {} systemctl stop firewalld".format(ip))
				print("""
				Press 1 : to start namenode 
				Press 2 : to start datanode 
				press 3 : to see cluster report	
				Press 4 : to see the saved files in cluster		
				Press 5 : to read a saved file 
				Press 6 : to see the running nodes
				""")
				y=input()

				#if int(y)==0:
				#	funct = hadoop()
				#	os.system("ssh {} {}".format(ip,funct)
				
				if int(y)==1:
					os.system("tput setaf 50")
					os.system("ssh {} hadoop-daemon.sh start namenode".format(ip))
					os.system("tput setaf 2")
				elif int(y)==2:
					os.system("tput setaf 50")
					os.system("ssh {} hadoop-daemon.sh start datanode".format(ip))
					os.system("tput setaf 2")
				elif int(y)==3:
					os.system("tput setaf 50")
					os.system("ssh {} hadoop dfsadmin -report".format(ip))
					os.system("tput setaf 2")
				elif int(y)==4:
					os.system("tput setaf 50")
					os.system("ssh {} hadoop fs -ls/".format(ip))
					os.system("tput setaf 2")
				elif int(y)==5:
					z=input("Enter the file name:")
					os.system("tput setaf 50")
					os.system("ssh {} hadoop fs -cat /{}".format(ip,z))
					os.system("tput setaf 2")
				elif int(y)==6:	
					os.system("tput setaf 50")
					os.system("ssh {} jps".format(ip))
					os.system("tput setaf 2")


			elif int(x)==5:
				os.system("tput setaf 50")
				print(" Press 1 : to check status of webserver \n Press 2 : to start webserver \n Press 3 : to stop webserver")
				a=input()
				if int(a)==1:
					os.system("tput setaf 50")
					os.system("ssh {} systemctl status httpd".format(ip))
					os.system("tput setaf 2")
				if int(a)==2:
					os.system("tput setaf 50")
					os.system("ssh {} systemctl start httpd".format(ip))
					os.system("tput setaf 2")
					os.system("ssh {} ls /var/www/html".format(ip))
				if int(a)==3:
					os.system("tput setaf 50")
					os.system("ssh {} systemctl stop httpd".format(ip))
					os.system("tput setaf 2")
			

			elif int(x)==6:
				os.system("tput setaf 50")
				print(" Press 1 : to check status of firewall \n Press 2 : to start firewall\n Press 3 : to stop firewall")
				a=input()
				if int(a)==1:
					os.system("tput setaf 50")
					os.system("ssh {} systemctl status firewalld".format(ip))
					os.system("tput setaf 2")
				if int(a)==2:
					os.system("tput setaf 50")
					os.system("ssh {} systemctl start firewalld".format(ip))
					os.system("tput setaf 2")
					#os.system("ls /var/www/html")
				if int(a)==3:
					os.system("tput setaf 50")
					os.system("ssh {} systemctl stop firewalld".format(ip))
					os.system("tput setaf 2")
			elif int(x)==7:
				f1=open("docker123.repo","w+")
				f1.write("[docker]\nbaseurl=http://download.docker.com/linux/centos/7/x86_64/stable\ngpgcheck=0")
				f1.close()
				f=open("anuj123.repo","w+")
				os.system('mv docker123.repo /etc/yum.repos.d/')
				f.write("[dvd1]\nbaseurl=file:///run/media/root/RHEL-8-0-0-BaseOS-x86_64/AppStream\ngpgcheck=0\n[dvd2]\nbaseurl=file:///run/media/root/RHEL-8-0-0-BaseOS-x86_64/BaseOS\ngpgcheck=0")
				f.close()
				os.system('mv anuj123.repo /etc/yum.repos.d/')
				os.system('yum --version && dnf install https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm')



			elif int(x)==8:
				os.system("ssh {} fdisk -l".format(ip))
				os.system("tput setaf 50")
				d=input("Enter the name of drive  --  ")				
				f=input("Enter the name of folder on which you like to mount your partition --")
				#s=input("Enter the size of partition (in Gib) --")
				q='ssh {} echo  -e  "n\n\n\n\n\nw\n" | fdisk {}'.format(ip,d)
				#print(sp.getoutput(q))
				os.system('ssh {} udevadm settle'.format(ip))
				#p=input('Enter the partition number -- ')
				z='ssh {} mkfs.ext4 {}1'.format(ip,d)
				print(sp.getoutput(z))
				os.system("ssh {} mkdir /{} ".format(ip,f))
				os.system('ssh {} mount /{}1 /{}'.format(ip,d,f))	
				os.system("tput setaf 2")		


			
			elif int(x)==9:
				os.system("tput setaf 7")
				exit()
			
							
			else:
				os.system("tput setaf 9")
				print("oops!!!....this choice is not available")
				os.system("tput setaf 2")
			input()
			os.system("clear")
				
#######################################################################################
os.system("tput setaf 3")

print("Welcome to my application")

os.system("tput setaf 2")

passwd = getpass.getpass("Enter the password!!..")

if passwd  == "arth":

	os.system("clear")
	user = input("Where do you want to login?(local/remote)--")

	if user == "local" :
		while True :			
			print("""
			Enter your choice:
			Press 1 : to see IP
			Press 2 : to open calender
			Press 3 : to use docker 
			Press 4 : to use hadoop service 
			Press 5 : to use webservice
			Press 6 : to manage firewall service 
			Press 7 : to configure yum
			Press 8 : to create partition
			Press 9 : to exit
			Press 10: to login to remote user
			      """)	

			x=input()

			if int(x)==1:
				os.system("tput setaf 50")
				os.system("ifconfig enp0s3")
				os.system("tput setaf 2")
			elif int(x)==2:
				os.system("tput setaf 50")
				os.system("cal")
				os.system("tput setaf 2")
			elif int(x)==3:
				os.system("tput setaf 1")
				print("By default OS 'ubuntu:14.04' will be installed")
				os.system("tput setaf 5")
				os.system('docker --version')
				os.system('yum install docker-ce --nobest')
				os.system('systemctl start docker')
				os.system('docker pull ubuntu:14.04')
				os.system("tput setaf 1")
				print("This is your 'ubuntu:14.04' OS :::")
				os.system("tput setaf 5")
				os.system('docker run -it ubuntu:14.04')
                        
			elif int(x)==4:

				

				os.system("tput setaf 50")				
				os.system("systemctl stop firewalld")
				print("""
				Press 0 : to configure hadoop cluster
				Press 1 : to start namenode 
				Press 2 : to start datanode 
				press 3 : to see the saved files in cluster
				Press 4 : to see cluster report				
				Press 5 : to read a saved file 
				Press 6 : to see the running nodes
					""")
				y=input()

				if int(y)==0:
					hadoop()
				

				elif int(y)==1:
					os.system("tput setaf 50")
					os.system("hadoop-daemon.sh start namenode")
					os.system("tput setaf 2")
				elif int(y)==2:
					os.system("tput setaf 50")
					os.system("hadoop-daemon.sh start datanode")
					os.system("tput setaf 2")
				elif int(y)==3:
					os.system("tput setaf 50")
					os.system("hadoop dfsadmin -report")
					os.system("tput setaf 2")
				elif int(y)==4:
					os.system("tput setaf 50")
					os.system("hadoop fs -ls/")
					os.system("tput setaf 2")
				elif int(y)==5:
					z=input("Enter the file name:")
					os.system("tput setaf 50")
					os.system("hadoop fs -cat /{}".format(z))
					os.system("tput setaf 2")
				elif int(y)==6:	
					os.system("tput setaf 50")
					os.system("jps")
					os.system("tput setaf 2")

			elif int(x)==5:
				os.system("tput setaf 50")
				print(" Press 1 : to check status of webserver \n Press 2 : to start webserver \n Press 3 : to stop webserver")
				a=input()
				if int(a)==1:
					os.system("tput setaf 50")
					os.system("systemctl status httpd")
					os.system("tput setaf 2")
				elif int(a)==2:
					os.system("tput setaf 50")
					os.system("systemctl start httpd")
					os.system("tput setaf 2")
					os.system("ls /var/www/html")
				elif int(a)==3:
					os.system("tput setaf 50")
					os.system("systemctl stop httpd")
					os.system("tput setaf 2")
			elif int(x)==6:
				os.system("tput setaf 50")
				print(" Press 1 : to check status of firewall \n Press 2 : to start firewall \n Press 3 : to stop firewall")
				a=input()
				if int(a)==1:
					os.system("tput setaf 50")
					os.system("systemctl status firewalld")
					os.system("tput setaf 2")
				elif int(a)==2:
					os.system("tput setaf 50")
					os.system("systemctl start firewalld")
					os.system("tput setaf 2")
					os.system("ls /var/www/html")
				elif int(a)==3:
					os.system("tput setaf 50")
					os.system("systemctl stop firewalld")
					os.system("tput setaf 2")			
			
			elif int(x)==7:
				f1=open("docker123.repo","w+")
				f1.write("[docker]\nbaseurl=http://download.docker.com/linux/centos/7/x86_64/stable\ngpgcheck=0")
				f1.close()
				f=open("anuj123.repo","w+")
				os.system('mv docker123.repo /etc/yum.repos.d/')
				f.write("[dvd1]\nbaseurl=file:///run/media/root/RHEL-8-0-0-BaseOS-x86_64/AppStream\ngpgcheck=0\n[dvd2]\nbaseurl=file:///run/media/root/RHEL-8-0-0-BaseOS-x86_64/BaseOS\ngpgcheck=0")
				f.close()
				os.system('mv anuj123.repo /etc/yum.repos.d/')
				os.system('yum --version && dnf install https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm')



			elif int(x)==8:
				os.system("fdisk -l")
				os.system("tput setaf 50")
				d=input("Enter the name of drive  --  ")				
				f=input("Enter the name of folder on which you like to mount your partition --")
				#s=input("Enter the size of partition (in Gib) --")
				q='echo  -e  "n\n\n\n\n\nw\n" | fdisk {}'.format(d)
				print(sp.getoutput(q))
				os.system('udevadm settle')
				#p=input('Enter the partition number -- ')
				z='mkfs.ext4 {}1'.format(d)
				print(sp.getoutput(z))
				os.system("mkdir /{} ".format(f))
				os.system('mount /{}1 /{}'.format(d,f))	
				os.system("tput setaf 2")		


			elif int(x)==9:
				os.system("tput setaf 7") 
				exit()

			elif int(x)==10:
				os.system("tput setaf 9")
				remote()
				os.system("tput setaf 2")
				
			else:   
				os.system("tput setaf 9")
				print("oops!!!....this choice is not available")	
				os.system("tput setaf 2")


			input()
			os.system("clear")

	elif user ==  "remote" :
		
			remote()
			input()
			os.system("clear")
#os.system("exit")

	else :
		print("Please input the correct user....")


else:
	os.system("tput setaf 9")
	print("wrong password")
os.system("tput setaf 7")


