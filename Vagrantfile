NODES = 3 # Number of nodes
CUSTOM_SSH_KEY_FILE_PATH = File.expand_path("~/.ssh/vagrant-k3s-cluster-sample")
BASE_VAGRANT_BOX = "ubuntu/jammy64"

Vagrant.configure("2") do |config|
  # Prevent Vagrant from inserting its own key
  config.ssh.insert_key = false

  (1..node_count).each do |i|
    config.vm.define "node#{i}" do |node|
      node.vm.box = BASE_VAGRANT_BOX
      node.vm.hostname = "node#{i}"

      node.vm.network "private_network", ip: "192.168.33.#{10+i}"

      node.vm.provider "virtualbox" do |vb|
        vb.name = "node#{i}"
        vb.memory = 2048 # Memory in MiB
        vb.cpus = 1 # Number of CPU cores
      end

      node.vm.provision "file", source: "#{CUSTOM_SSH_KEY_FILE_PATH}.pub", destination: "/tmp/vagrant-key.pub"
      node.vm.provision "shell", inline: <<-SHELL
        mkdir -p /home/vagrant/.ssh
        cat /tmp/vagrant-key.pub >> /home/vagrant/.ssh/authorized_keys
        
        chown -R vagrant:vagrant /home/vagrant/.ssh
        chmod 700 /home/vagrant/.ssh
        chmod 600 /home/vagrant/.ssh/authorized_keys
      SHELL
    end
  end
end
