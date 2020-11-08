import o
import getpass

os.system("tput setaf 3 && clear")

print("*******************************************************************************")
print("YOU are using Operating System -->",os.name)
print("*******************************************************************************\n\nWelcome to my Menu this is a python project to automate some repititive process\n\n")

passis="anujgupta"
while True:
	passwd=getpass.getpass("ENTER password to continue -->")

	if passwd != passis:
		os.system("tput setaf 1")
		print("\nSorry :( incorrect password try again\n")
		os.system("tput setaf 3")
	if passwd == passis:
		break

# menu to choose from

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
	\t\tpress 7 : to transfer me to other system in / drive
	\t\tpress 8 : to configure httpd
	\t\tpress 9 : to create partition
	\t\tpress10 : to setup docker
	\t\tpress11 : to see code on the fly 
	""")
	#os.system("tput setaf 2")
menu()

# while loop to set code for options

while True:
	os.system("tput setaf 2")
	ch = input("Enter ur choice :")
	os.system("tput setaf 5")
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
		f1=open("docker123.repo","w+")
		f1.write("[docker]\nbaseurl=http://download.docker.com/linux/centos/7/x86_64/stable\ngpgcheck=0")
		f1.close()
		f=open("anuj123.repo","w+")
		os.system('mv docker123.repo /etc/yum.repos.d/')
		f.write("[dvd1]\nbaseurl=file:///run/media/root/RHEL-8-0-0-BaseOS-x86_64/AppStream\ngpgcheck=0\n[dvd2]\nbaseurl=file:///run/media/root/RHEL-8-0-0-BaseOS-x86_64/BaseOS\ngpgcheck=0")
		f.close()
		os.system('mv anuj123.repo /etc/yum.repos.d/')
		os.system('yum --version && dnf install https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm')

	elif int(ch) ==7:
		ip=input("enter destination ip address ")
		os.system('scp menu.py {}:/'.format(ip))
		os.system('echo redhat')
		
	elif int(ch) ==8:
		print("if yum configured already then go ahead else select option '6' 	first")
		os.system('yum install httpd')
		os.system('systemctl start httpd && systemctl enable httpd')
	elif int(ch) ==9:
		os.system('fdisk -l')
		p=input("\nenter name of partition :-\n")
		os.system('fdisk {}'.format(p))
		os.system('lsblk && udevadm settle')
		os.system('mkfs.ext4 {}'.format(p))
		f=input('\nenter folder name\n')
		os.system('mkdir /{}'.format(f))
		os.system('mount {} /{}'.format(p,f))

	elif int(ch) ==10:
		print("By default OS 'ubuntu:14.04' will be installed")
		os.system('docker --version')
		os.system('yum install docker-ce --nobest')
		os.system('systemctl start docker')
		os.system('docker pull ubuntu:14.04')
		os.system('docker run -it ubuntu:14.04')
	
	elif int(ch) ==11:
		os.system("gedit menu.py")

	else:
		os.system('tput setaf 1')		
		print('\nplease choose from options provided\n')

