# Parsec Add-on for Kodi (script.parsec)

## Description

This add-on is to launch PARSEC software on a Linux based OSMC (or Kodi) machine like Raspberry Pi or a x86_64 based Ubuntu computer. PARSEC is a interactive streaming software that is fine tuned for gaming. The main goal of a media center add-on like this, is to enable the media center's capability for playing games that are not actually installed on it.

## Requirements

- PARSEC Software (Can be downloaded from [https://parsecgaming.com/downloads/](https://parsecgaming.com/downloads/))
- A minimum of 208MB that is reserved for graphics memory
- OSMC (or Kodi)
- A computer to run all of this :) (tested on a Raspberry Pi 3 B+)


## Installation

### Step 1: Install PARSEC (optional)

- If you have PARSEC installed then you can skip to Step 2

- If you are trying to install PARSEC on a Raspberry Pi

```bash
wget https://s3.amazonaws.com/parsec-build/package/parsec-rpi.deb
sudo dpkg -i parsec-rpi.deb
```

- If you are trying to install PARSEC on an Ubuntu 18.04 LTS or higher on a 
x86_64 based computer

```bash
wget https://s3.amazonaws.com/parsec-build/package/parsec-linux.deb
sudo dpkg -i parsec-linux.deb
```


### Step 2: Install The PARSEC Add-On

```bash
cd addons
wget -O script.parsec.zip https://github.com/ekinkaradag/script.parsec/archive/master.zip
```
- Then open OSMC (or Kodi)
- Navigate to <code>Add-on</code> -> <code>Install from zip file</code>, Enter it
- Choose <code>Home folder</code>, then choose <code>addons</code>
- From there choose <code>script.parsec.zip</code>
- Congratulations! You have successfully installed the add-on
- Now you have to add the Peer ID. Configure the add-on: Add the Peer ID of the host PC.


