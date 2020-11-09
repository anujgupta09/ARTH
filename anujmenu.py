import os
import getpass

os.system("tput setaf 3 && clear")

print("*******************************************************************************")
print("YOU are using Operating System -->",os.name)
print("*******************************************************************************\n\nWelcome to my Menu this is a python project to automate some repititive process\n\n")

########################################################################################

# note: to add options 
# 1. create correct function for it add it below
# 2. update in menu() function 
# 3. update in whileloop() function 

############## functions for all options ###############################################

def authentication():
	hardcodedpass="anujgupta"
	while True:
		passwd=getpass.getpass("ENTER password to continue -->")

		if passwd != hardcodedpass:
			os.system("tput setaf 1")
			print("\nSorry :( incorrect password try again\n")
			os.system("tput setaf 3")
		if passwd == hardcodedpass:
			break

def menu():
	os.system("tput setaf 1")
	
	print("""
	\t\tMENU --:
	\t\tpress 1 : to run automated date command
	\t\tpress 2 : to exit from this automated menu softwear
	\t\tpress 3 : to see menu again
	\t\tpress 4 : to run cal
	\t\tpress 5 : to make a Note
	\t\tpress 6 : to config yum with epel &cd(aapstream&baseos)
	\t\tpress 7 : to trnsfer me to othr sys. in /root drive
	\t\tpress 8 : to configure httpd
	\t\tpress 9 : to create partition
	\t\tpress10 : to setup docker
	\t\tpress11 : to see code on the fly
	\t\tpress12 : to setup hadoop
	""")

def yum():
	f1=open("docker123.repo","w+")
	f1.write("[docker]\nbaseurl=http://download.docker.com/linux/centos/7/x86_64/stable\ngpgcheck=0")
	f1.close()
	f=open("anuj123.repo","w+")
	os.system('mv docker123.repo /etc/yum.repos.d/')
	f.write("[dvd1]\nbaseurl=file:///run/media/root/RHEL-8-0-0-BaseOS-x86_64/AppStream\ngpgcheck=0\n[dvd2]\nbaseurl=file:///run/media/root/RHEL-8-0-0-BaseOS-x86_64/BaseOS\ngpgcheck=0")
	f.close()
	os.system('mv anuj123.repo /etc/yum.repos.d/')
	os.system('yum --version && dnf install https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm')

def transferme():
	ip=input("enter destination ip address ")
	os.system('scp anujmenu.py {}:/root'.format(ip))
	os.system('echo redhat')

def httpd():
	print("if yum configured already then go ahead else select option '6' 	first")
	os.system('yum install httpd')
	os.system('systemctl start httpd && systemctl enable httpd')

def partition():
	os.system('fdisk -l')
	os.system('tput setaf 1')
	p=input("\nenter name of partition :-\n")
	os.system('tput setaf 5')
	os.system('fdisk {}'.format(p))
	os.system('lsblk && udevadm settle')
	os.system('mkfs.ext4 {}'.format(p))
	f=input('\nenter folder name\n')
	os.system('mkdir /{}'.format(f))
	os.system('mount {} /{}'.format(p,f))

def docker():
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

def hadoop():

		###### function of hadoop #######################################

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
	
	def NN():	
		NNdir=input("enter DN directory name")
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
	elif op==3:
		client()

def whileloop():
	while True:
		os.system("tput setaf 2")
		ch = input("Enter ur choice :")  # taking input from user
		os.system("tput setaf 5")
			
		#options	

		if int(ch) ==1:
			os.system('date')

		elif int(ch) ==2:
			os.system('tput setaf 7')
			os.system('clear')
			exit()

		elif int(ch) ==3:
			menu()

		elif int(ch) ==4:
			os.system('cal')

		elif int(ch) ==5:
			os.system('mkdir /note && cd /note')
			os.system('gedit note.txt')

		elif int(ch) ==6:
			yum()

		elif int(ch) ==7:
			transferme()
			
		elif int(ch) ==8:
			httpd()

		elif int(ch) ==9:
			partition()

		elif int(ch) ==10:
			docker()
		
		elif int(ch) ==11:
			os.system("gedit anujmenu.py")
		elif int(ch) ==12:
			hadoop()

		else:
			os.system('tput setaf 1')		
			print('\nplease choose from options provided\n')
			menu() ## to prevent exit from menu.py if wrong option choosed 

################ calling functions #####################################################


authentication()
menu()
whileloop()

########################################################################################

