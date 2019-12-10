<h1 align="center">Welcome to tweetGen</h1>
<a href="https://www.google.com/search?q=twitter+icon&source=lnms&tbm=isch&sa=X&ved=0ahUKEwingJCUgvPlAhWYsp4KHWpXBVYQ_AUIEigB&biw=1440&bih=788#imgrc=4-NyAF10t5J6BM:"><img src="/static/img/icon.png" title="Twitter Icon"></a>
<p>
    <a href="https://www.npmjs.com/package/readme-md-generator">
    <img alt="downloads" src="https://img.shields.io/github/contributors/imthaghost/ghostChat?color=green" target="_blank" />

  </a> 
  
  <img alt="Version" src="https://img.shields.io/badge/version-1.0-blue.svg?cacheSeconds=2592000" />
  <a href="#" target="_blank">
    <img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-yellow.svg" />
  </a>
   <a href="https://github.com/imthaghost/gitmoji-changelog">
    <img src="https://img.shields.io/badge/changelog-gitmoji-brightgreen.svg" alt="gitmoji-changelog">
  </a>
  
</p>

> tweetGen generates tweets from any given corpus. The sentences are calculated via a stochastic model describing a sequence of possible events in which the probability of each event depends only on the state attained in the previous event (Markov Chain).

> The live version can be found at http://24.6.36.157:5000

![Word Generation](/static/img/gen.gif)

### 💻 Prerequisites

What things you need to install the software and how to install them

```bash

- python 3.4+
```

## 🚀 Getting Started

The python modules were configured in a virtual enviornment with `pipenv`:

#### macOS Mojave 10.0+

```bash
# (if you have pipenv installed skip this step)
brew install pipenv
# clone repository
git clone https://github.com/imthaghost/tweetGen
# active the virtual enviornment
pipenv shell
# install modules into virtual environment
pipenv install
# start server
python3 app.py
```

> This also assumes that you have `brew` installed. After cloning the repository in desired directory we run the command `pipenv shell` to initialize and activate our virtual enviornment. Unless specified pipenv will default to whatever virtualenv defaults to. We then allow pipenv to find and install the necessary modules for our server. All modules can be viewed inside the file `Pipfile` under the [packages] section. We then start running the server on port 8080.

#### apt systems Ubuntu, Debian, Mint, Etc

```bash
# install pipenv
sudo pip install pipenv
# clone repository
git clone https://github.com/imthaghost/tweetGen
# active the virtual enviornment
pipenv shell
# install modules into virtual environment
pipenv install
# start flask server
python3 app.py
```

## How to contribute

Fork the current repository and then make the changes that you'd like to said fork. Upon adding features, fixing bugs,
or whatever modifications you've made to the project, issue a pull request to this repository containing the changes that you've made!

## Built With

-   [Flask Micro-Framework](http://flask.palletsprojects.com/en/1.1.x/) - The web framework used
-   [Wordcloud](https://pypi.org/project/wordcloud/) - Dependency

## Contributors

-   **Gary Frederick** - _Author_ - [imthaghost](https://github.com/imthaghost)

See also the list of [contributors](https://github.com/imthaghost/tweetGen/contributors) who participated in this project.

## Acknowledgments

-   Hat tip to my professor [Alan Davis](https://github.com/neptunius)
-   Great way of understanding Vose Alias Method [Keith Schwarz](http://www.keithschwarz.com/darts-dice-coins/)
