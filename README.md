# Instalación
Este script configura samba (active directory) en distibuciones CentOS 7

```
git clone https://github.com/angelf502/autodc2
cd autodc2/
python3 main.py
```
# Vista
![DC](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi7I4ElABINPMkQINPllLPnLWEF7by91KjK_jq4aN0ej-kd5ZojDubUjaZsaevuYDA18ymgj9yi4Rbfo7nJ3uEFTfjBYErYXQNrbh2tfL9cg6p8P8psXHweigtGXOdfigPuVwDEtQIFyzaPyOEDm5TIrFAfs4L3QV9YGWYPC1IU5od8Y3zgvGwwpULqNA/s722/5.JPG)

Unido como administrador al dominio podemos hacer configuraciones como GPO´s desde windows, podríamos usar RSAT para poder administrarlo graficamente.

![DC-C](https://blogger.googleusercontent.com/img/a/AVvXsEg9x6vL-JHqX_o8gn9EBx6sm15A6ronaRwih7TrZYXN_SOQZfMKQMWScETIr4NLrXLtsuJOdJ7ufRPqTsYpO6mwoxuew5dZceuA5j7oA0YPgTVG0XXmT_9I4ynQVAwbv5rxcrWVSUao7ACiaGoWRzqzoOSvcxixMlBHwoQhZfMmHKGORadkLKSF5D67kA)

# Servicios
- **Samba**: Es un conjunto de herramientas que se utilizan para compartir entre redes mixtas de Windows y Linux.
![1](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhVVN6m-ZE3Ha3dO85XZK-9iPrFTxO4ilFL8Fg5EDQC9UetsRvmZEK7YrI6sWfrjmOBf6BoCCfaPAo267XOaq9F0IHorYMKJZyUyx5xsYAY53NOMNc0vCTZ6_Atbg6cYlq6sQ7iGyptscFRREHCfZsuVCzqnA-Nxjp5osHKAOdwi9X6wu2OwM6eyAhYRA/s704/6.JPG)

- **krb5-config**: Contiene información de configuración de Kerberos, incluidas las ubicaciones de los KDC y los servidores de administración para los dominios de Kerberos de interés.

![2](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgDggZv7cKYGdZA8ao1gs1CtT2EquQpRutWLpdLMs-u984iZoEN5VLGzhk9UtWVmrAX3ivJHkxUQCI6d1x8WHdJE8jat3RMyc5NAcT3uVxONAVCrdfkHDrQkwaRmEq4YwEaralZvJQP54QHQAYxNglhP9OmtpF6RKdbCIB2MGstB129VnSc8lXrqji6BQ/s683/7.JPG)

# Aspectos a tener en cuenta
- El script finaliza y es necesario reiniciar el equipo, luego de esto debemos aprovisionar la herramienta de samba:
```
export PATH=/usr/local/samba/bin/:/usr/local/samba/sbin/:$PATH
samba-tool domain provision --use-rfc2307 --interactive
```
- Comprobar que la dirección IP, hostname y dominio coincidan con los archivos de /etc/hosts y /etc/resolv.conf.
- Del lado de Windows como cliente, comprobar que tengan misma zona horaria, que haya comunicación bidireccional y comprobar firewalls en el equipo (Windows).
