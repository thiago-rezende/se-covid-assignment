# Software Engineering Assignment
![license-badge] ![python-badge] ![pipenv-badge]
<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/thiago-rezende/se-covid-assignment">
    <img src="https://github.com/thiago-rezende/se-covid-assignment/raw/main/.github/logo.png" alt="Logo" width="100" height="100">
  </a>

  <h3 align="center">Software Engineering Assignment</h3>
  <p align="center">
    Dead Simple Covid-19 Propagation Simulation
    <br />
    <a href="https://github.com/thiago-rezende/se-covid-assignment/issues">Report Bug</a>
    ·
    <a href="https://github.com/thiago-rezende/se-covid-assignment/issues">Request Feature</a>
    .
    <a href="https://github.com/thiago-rezende/se-covid-assignment/actions">Continuous Integration</a>
  </p>
</div>

# Libraries Included
 - [NumPy][numpy-url]
 - [Matplotlib][matplotlib-url]

# Project structure
```
 .
 ├── .github                         # Repository stuff.
 ├── main.py                         # Application entry point.
 ├── horus                           # Horus package.
 |    └── application.py             # Application class.
 ├── Pipenv                          # Pipenv file.
 └── Pipfile.lock                    # Pipenv lock file.
```

# Instructions
> Clone the repo
```sh
  git clone https://github.com/thiago-rezende/se-covid-assignment.git
  cd se-covid-assignment
```

> Install pipenv
```sh
  pip install pipenv
```

> Install dependencies
```sh
  pipenv install
```

> Run the application
```sh
  pipenv run python main.py
```

<!-- Links -->
[python-url]: https://www.python.org/
[matplotlib-url]: https://matplotlib.org/
[numpy-url]: https://numpy.org/

<!-- Badges -->
[license-badge]: https://img.shields.io/github/license/thiago-rezende/se-covid-assignment?style=flat-square
[pipenv-badge]: https://img.shields.io/badge/Pipenv-2020.11-blueviolet.svg?style=flat-square
[python-badge]: https://img.shields.io/github/pipenv/locked/python-version/thiago-rezende/se-covid-assignment?style=flat-square
