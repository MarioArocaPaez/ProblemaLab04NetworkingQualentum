Vagrant.configure("2") do |config|
    config.vm.box = "ubuntu/bionic64" 
  
    # Configuración de red
    config.vm.network "private_network", ip: "192.168.56.10"
  
    # Configuración del nombre del host
    config.vm.hostname = "local.qualentum.org"
  
    # Provisión con Ansible
    config.vm.provision "ansible" do |ansible|
      ansible.playbook = "provision.yml"
    end
  
    # Redirección del puerto 443
    config.vm.network "forwarded_port", guest: 443, host: 443
  end
  