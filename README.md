# Installation pre-requisites and instructions on how to use Spearmint and MongoDB

# Install Xcode

xcode-select --install

# Homebrew

[Homebrew page] (http://brew.sh)

# Homebrew for MacOS X

```sh
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

# Linuxbrew for Ubuntu

```sh
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Linuxbrew/install/master/install)"
```

# add brew command to your $PATH

```sh
PATH=~/.linuxbrew/bin:$PATH
```

# Spearmint

[Spearmint on GitHub](https://github.com/HIPS/Spearmint)

# Install Spearmint

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


```sh
mkdir -p ~/work/spearmint
cd ~/work/spearmint
mkdir mongodb
mongod --logpath mongodb/mongod.log --dbpath mongodb
```


#Run Spearmint

```sh
python ~/%PATH_TO%/main.py ~/%PATH_TO_CODE%/
ls ~/%PATH_TO_OUTPUT%/output
```
