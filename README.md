# Installation pre-requisites and instructions on how to use Spearmint and MongoDB

# Install Xcode

```sh
xcode-select --install
```

# Homebrew

[Homebrew page] (http://brew.sh)

# Homebrew for MacOS X

Copy and paste the following in your terminal

```sh
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

# Linuxbrew for Ubuntu

[Linuxbrew page](http://linuxbrew.sh/)

Copy and paste the following in your terminal

```sh
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Linuxbrew/install/master/install)"
```

add brew command to your $PATH

```sh
PATH=~/.linuxbrew/bin:$PATH
```

# Spearmint

[Spearmint on GitHub](https://github.com/HIPS/Spearmint)

# Install Spearmint and MongoDB

```sh
mkdir ~/src
cd ~/src
git clone https://github.com/HIPS/spearmint
pip install ./spearmint
brew install mongodb
pip install pymongo
pip install scipy
```

# Run MongoDB
In one terminal

```sh
mkdir -p ~/work/spearmint
cd ~/work/spearmint
mkdir mongodb
mongod --logpath mongodb/mongod.log --dbpath mongodb
```
leave running

#Run Spearmint

Open a second terminal

```sh
python ~/%PATH_TO%/main.py ~/%PATH_TO_abyss.py%/
ls ~/%PATH_TO_OUTPUT%/output
```
