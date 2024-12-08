# K3s Deployment Scenario

## Quick Start

### Step 1: Generate Your SSH Key

> ❗ **Attention**
>
> - Before bringing up the Vagrantfile VMs, make sure to generate an SSH key for secure connections.

```bash
ssh-keygen -t rsa -b 4096 -C "johndoe@example.com" -f ~/.ssh/vagrant-k3s-cluster-sample
```

### Step 2: Set Up Vagrant

1. Start your machines:

   ```bash
   vagrant up
   ```

   > 💡 **Tip**
   >
   > - To avoid downloading the Vagrant box every time, you can save the desired box (e.g., `ubuntu/jammy64`) locally by running:
   >
   >   ```bash
   >   vagrant box add ubuntu/jammy64
   >   ```

2. List the available boxes:

   ```bash
   vagrant box list
   ```

3. Stop all running machines:

   ```bash
   vagrant halt
   ```

4. Destroy your cluster and remove the VMs (including their files):

   ```bash
   vagrant destroy
   ```

5. Connect to a specific machine (e.g., `node2`)

   ```bash
   ssh -i ~/.ssh/vagrant-k3s-cluster-sample vagrant@192.168.33.12
   ```
