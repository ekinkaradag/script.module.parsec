# <u>Parsec Add-on for Kodi (script.parsec)</u>

## <u>Description</u>

This add-on is to launch Parsec software on a Linux based OSMC (or Kodi) machine like Raspberry Pi or a x86_64 based Ubuntu computer. Parsec is a interactive streaming software that is fine tuned for gaming. The main goal of a media center add-on like this, is to enable the media center's capability for playing games that are not actually installed on it.
<br>
<br>

## <u>Requirements</u>

- Parsec Software must be installed on both the client and the host (Can be downloaded from [https://parsecgaming.com/downloads/](https://parsecgaming.com/downloads/))
- A minimum of 208MB that is reserved for graphics memory
- OSMC (or Kodi)
- A computer to run all of this :) (tested on a Raspberry Pi 3 B+)
<br>
<br>

## <u>Installation</u>

### <u>Step 1: Install Parsec (required)</u>


- If you have already installed Parsec then you can skip to Step 2

<br>
<br>

- If you are trying to install Parsec on a Raspberry Pi

```bash
cd ~
wget https://s3.amazonaws.com/parsec-build/package/parsec-rpi.deb
sudo dpkg -i parsec-rpi.deb
```
<br>

- If you are trying to install Parsec on an Ubuntu 18.04 LTS or higher on a 
x86_64 based computer

```bash
cd ~
wget https://s3.amazonaws.com/parsec-build/package/parsec-linux.deb
sudo dpkg -i parsec-linux.deb
```


### <u>Step 2 - Method 1: Install The Parsec Add-On</u>

- If you do not have access to device's terminal, please choose Method 2 instead.
- Open terminal of the device (either via SSH or directly)
<br>
<br>

```bash
cd ~/addons
wget -O script.parsec.zip https://github.com/ekinkaradag/script.module.parsec/archive/master.zip
```
<br>

- Then open OSMC (or Kodi)
- Navigate to <code>Add-on</code> -> <code>Install from zip file</code>, Enter it
- Choose <code>Home folder</code>, then choose <code>addons</code>
- From there choose <code>script.module.parsec.zip</code>
- Congratulations! You have successfully installed the add-on.
- Now you have to add the Peer ID. Configure the add-on: Add the Peer ID of the host PC (Not necessary but advised)
<br>
<br>

### <u>Step 2 - Method 2: Install The Parsec Add-On</u>

- First of all you need a USB thumb drive (FAT32 formated drives are advised) 
- Download the latest version of the addon from https://github.com/ekinkaradag/script.module.parsec/releases
- Copy the downloaded zip file to USB thumb drive (Remember your USB thumb drive's name).
- Then open OSMC (or Kodi)
- Navigate to <code>Add-on</code> -> <code>Install from zip file</code>, Enter it
- Choose your USB thumb drive (Highlighted with its name)
- From there find and choose <code>script.module.parsec.zip</code>
- Congratulations! You have successfully installed the add-on.
- Now you have to add the Peer ID. Configure the add-on: Add the Peer ID of the host PC (Not necessary but advised)
<br>
<br>

## Helpful Links

- [Adding Xbox One / One S / 360 Controller to Raspberry Pi](https://pimylifeup.com/xbox-controllers-raspberry-pi/)

- [Adding PS4 Controller to Raspberry Pi](https://pimylifeup.com/raspberry-pi-playstation-controllers/) (Some people reported that PS4 Controller works just fine without doing anything.)

- [Setting up Parsec Software on Raspberry Pi](https://support.parsecgaming.com/hc/en-us/articles/115002699012-Setting-Up-On-Raspberry-Pi-Raspbian)



