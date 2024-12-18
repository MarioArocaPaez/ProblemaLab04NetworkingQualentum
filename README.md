# Proyecto: Configuración de un Servidor HTTPS con Flask y Nginx

Este proyecto proporciona un entorno automatizado para desplegar una aplicación web en Python utilizando HTTPS. Está diseñado para configurarse en una máquina virtual mediante **Vagrant** y **Ansible**. El entorno incluye:

1. Una API sencilla desarrollada con Flask (`app.py`).
2. Configuración de un servidor Nginx para servir tráfico HTTPS utilizando certificados SSL autofirmados.
3. Automatización del aprovisionamiento con Ansible (`provision.yml`).

## Contenido
- **`Vagrantfile`**: Configuración de la máquina virtual.
- **`provision.yml`**: Playbook de Ansible para instalar dependencias y configurar HTTPS.
- **`app.py`**: Aplicación en Python que expone una API básica.
- **`README.md`**: Instrucciones para el proyecto.

## Instrucciones
1. Instala **Vagrant** y **VirtualBox** en tu máquina.
2. Clona este repositorio en tu máquina local.
3. Navega al directorio del proyecto y ejecuta:
   ```bash
   vagrant up
   ```
4. Agrega la siguiente entrada a tu archivo `/etc/hosts` (en Linux/Mac) o `C:\Windows\System32\drivers\etc\hosts` (en Windows):
   ```
   192.168.56.10 local.qualentum.org
   ```
5. Abre un navegador y accede a `https://local.qualentum.org` para ver la aplicación funcionando.

## Requisitos
- Vagrant
- VirtualBox
- Ansible
