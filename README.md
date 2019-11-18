Markov Chain Tweet generator
[![Build Status][travis-image]][travis-url]

<img src="/static/img/gen.png" width="55%"></img>

## Description

tweetGen generates tweets from a any given corpus. The sentences are calculated via a stochastic model describing a sequence of possible events in which the probability of each event depends only on the state attained in the previous event (Markov Chain).

### Prerequisites

What things you need to install the software and how to install them

```bash
- brew
- python 3.4+
```

## Getting Started

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

This also assumes that you have `brew` installed. After cloning the repository in desired directory we run the command `pipenv shell` to initialize and activate our virtual enviornment. Unless specified pipenv will default to whatever virtualenv defaults to. We then allow pipenv to find and install the necessary modules for our server. All modules can be viewed inside the file `Pipfile` under the [packages] section. We then run our PostgreSQL database as a background process, the server uses postgresql's defaults(database name and user `postgre`). We then start running the server on port 8080.

## Running Application

## How to contribute

Fork the current repository and then make the changes that you'd like to said fork. Upon adding features, fixing bugs,
or whatever modifications you've made to the project, issue a pull request to this repository containing the changes that you've made!

## Goals

## Short term goals

## Deployment

## Built With

-   [Flask Micro-Framework](http://flask.palletsprojects.com/en/1.1.x/) - The web framework used
-   [Wordcloud](https://pypi.org/project/wordcloud/) - Dependency

## Authors

-   **Gary Frederick** - _Initial work_ - [imthaghost](https://github.com/imthaghost)

See also the list of [contributors](https://github.com/imthaghost/tweetGen/contributors) who participated in this project.

## Acknowledgments

-   Hat tip to my professor [Alan Davis](https://github.com/neptunius)
-   Great way of understanding Vose Alias Method [Keith Schwarz](http://www.keithschwarz.com/darts-dice-coins/)
