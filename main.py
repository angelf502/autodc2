#!/usr/bin/python3
import os
import subprocess
import time

def firewall_rules():
    yes_option = os.system("firewall-cmd --add-port=53/tcp --permanent;firewall-cmd --add-port=53/udp --permanent;firewall-cmd --add-port=88/tcp --permanent;firewall-cmd --add-port=88/udp --permanent; \
firewall-cmd --add-port=135/tcp --permanent;firewall-cmd --add-port=137-138/udp --permanent;firewall-cmd --add-port=139/tcp --permanent; \
firewall-cmd --add-port=389/tcp --permanent;firewall-cmd --add-port=389/udp --permanent;firewall-cmd --add-port=445/tcp --permanent; \
firewall-cmd --add-port=464/tcp --permanent;firewall-cmd --add-port=464/udp --permanent;firewall-cmd --add-port=636/tcp --permanent; \
firewall-cmd --add-port=1024-5000/tcp --permanent;firewall-cmd --add-port=3268-3269/tcp --permanent")

    os.system("firewall-cmd --reload")

def ask_user():
    user_input = input("Â¿Quiere que se configuren las reglas de Firewall (S/N)?\n->RecomendaciÃ³n si estÃ¡ en un entorno controlado (virtualizado) puede usar o no las reglas de Firewall\n\n->Si estÃ¡ en un entorno real deje las reglas de Firewall\n\n---->> ")
    if user_input == "S":
        firewalls = firewall_rules()
    elif user_input == "N":
        os.system("systemctl stop firewalld && systemctl disable firewalld")
    else:
        print("Ponga una opciÃ³n valida")

def hostnames():
    seleccion = input("Â¿Desea cambiar el nombre del equipo (S/N)? ")
    if seleccion == "S":
        os.system("hostnamectl set-hostname Test")
        print("\nEl equipo a cambiado de nombre a 'Test'")
        os.system("hostname")
    elif seleccion == "N":
        print("\n[+] Seguimos con las configuraciones...")
        print("\nEstar atento a su hostname para que las configuraciones sean correctas...\n")

def instalattion():
    hostname = subprocess.run("hostname", shell=True)
    print("\n", hostname)
    time.sleep(2)
    hostnAme1 = hostnames()
    os.system("sudo sed -i '7i SELINUX=disabled' /etc/selinux/config")
    os.system("sudo sed -i '8d' /etc/selinux/config")
    time.sleep(2)
    os.system("sudo echo '192.168.1.1 test.redes.local' >> /etc/hosts")
    os.system("sudo yum install update -y > /dev/null && sudo yum upgrade -y > /dev/null")
    os.system("sudo yum install epel-release -y > /dev/null")
    os.system("sudo yum install  perl gcc libacl-devel libblkid-devel gnutls-devel readline-devel python-devel gdb pkgconfig krb5-workstation zlib-devel setroubleshoot-server libaio-devel setroubleshoot-plugins\
policycoreutils-python libsemanage-python setools-libs-python setools-libs popt-devel libpcap-devel sqlite-devel libidn-devel libxml2-devel libacl-devel libsepol-devel libattr-devel keyutils-libs-devel\
cyrus-sasl-devel cups-devel bind-utils libxslt docbook-style-xsl openldap-devel pam-devel bzip2 vim wget -y > /dev/null")
    os.system("sudo yum install attr bind-utils docbook-style-xsl gcc gdb krb5-workstation \
libsemanage-python libxslt perl perl-ExtUtils-MakeMaker \
perl-Parse-Yapp perl-Test-Base pkgconfig policycoreutils-python \
python-crypto gnutls-devel libattr-devel keyutils-libs-devel \
libacl-devel libaio-devel libblkid-devel libxml2-devel openldap-devel \
pam-devel pop-devel python-devel readline-devel zlib-devel systemd-devel -y > /dev/null")
    os.system("wget https://download.samba.org/pub/samba/stable/samba-4.6.0.tar.gz")
    os.system("tar -zxvf samba-4.6.0.tar.gz")
    time.sleep(3)
    os.system("cd samba-4.6.0/")
    time.sleep(1)
    os.system("cd samba-4.6.0/ && ./configure --enable-debug --enable-selftest --with-ads --with-systemd --with-winbind")
    time.sleep(3)
    print("\n[*] Este paso tomarÃ¡ mucho tiempo...\n\n")
    time.sleep(3)
    os.system("cd samba-4.6.0/ && make && make install")
    os.system("sudo echo 'search redes.local' >> /etc/resolv.conf")
    os.system("sudo echo 'nameserver 192.168.1.1' >> /etc/resolv.conf")
    os.system("sudo systemctl stop libvirtd.service && systemctl status libvirtd.service && sudo systemctl disable libvirtd.service")
    time.sleep(2)
    print("[Realm]: Poner el nombre de dominio\n[Domain]: Poner solo el dominio principal\n[DNS Forwarder]: Poner la IP del servidor y si hay mas separarlos por comas ','\n")
    time.sleep(5)
    os.system("export PATH=/usr/local/samba/bin/:/usr/local/samba/sbin/:$PATH && samba-tool domain provision --use-rfc2307 --interactive")
    time.sleep(2)
    os.system("sudo sed -i '2d' /etc/krb5.conf")
    time.sleep(3)
    os.system("export PATH=/usr/local/samba/bin/:/usr/local/samba/sbin/:$PATH && samba-tool domain provision --use-rfc2307 --interactive")
    asks = ask_user()
    rules = firewall_rules()
    print("\n", asks, "\n")
    time.sleep(3)
    print("\n", rules, "\n")
    time.sleep(5)
    os.system("clear")
    print('[Unit]\nDescription= Samba 4 Active Directory\nAfter=syslog.target\nAfter=network.target\n\n[Service]\nType=forking\nPIDFile=/usr/local/samba/var/run/samba.pid\nExecStart=/usr/local/samba/sbin/samba\n\n[Install]\nWantedBy=multi-user.target')
    print("\n[*] Copie y pegue estas lineas, pongalas en vi /etc/systemd/system/samba.service")
    time.sleep(9)
    os.system("(echo [Unit]; echo Description= Samba 4 Active Directory; echo After=syslog.target; echo After=network.target; echo ; echo [Service]; echo Type=forking; echo PIDFile=/usr/local/samba/var/run/samba.pid; echo ExecStart=/usr/local/samba/sbin/samba; echo ; echo [Install]; echo WantedBy=multi-user.target) >> /etc/systemd/system/samba.service")
    time.sleep(2)
    print("\n\n[*] En cuanto termine el script haga lo anterior indicado\n")
    os.system("sudo systemctl enable samba")
    os.system("sudo systemctl start samba")
    time.sleep(3)
    print("\n\n[*] Ahora puede probar lo siguiente para comprobar\n->host -t SRV _ldap._tcp.tu-dominio.com\n->host -t SRV _kerberos._udp.tu-dominio.com\n->host -t A nombreservidor.tu-dominio.com\n\n[*] Primero compruebe y  haga cambios necesarios en el direccionamiento IP\n\n")
    print("\n\n[+] Debe reiniciar el equipo")
    time.sleep(2)

def menu():
    time.sleep(1)
    print("1 -> Instalar todo por defecto (Debe cambiar algunos parametros como la direccion IP)")
    time.sleep(1)
    print("\n2 -> Salir")
    choose = input("\n--> ")

    if choose == "1":
        instalattion()
    if choose == "2":
        exit()

if __name__ == "__main__":
    menu()