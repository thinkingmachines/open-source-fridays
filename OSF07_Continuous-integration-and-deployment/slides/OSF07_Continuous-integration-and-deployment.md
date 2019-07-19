---
theme: metropolis
title: Open Source Fridays
subtitle: Continuous Integration and Deployment (CI/CD) - Putting your software into production
date: Jul 18, 2019
aspectratio: 169
institute: 'Thinking Machines Data Science'
---


# Software -> Prod

Continuous integration is the process of putting software into production:

- Publishing Python libraries in PyPI
- Compiling and distributing software to your users (`apt-get`, `brew install`)
- Building and serving a website

---

## For today, we'll learn/do the following...

- Learn about the continuous integration ecosystem in TM 
- Write a deployment file for an existing open-source/internal project!
- Get **badges** for that project!!

---

![](00_badge.png)


---

## Behind the scenes before your `pip install` 

![](oss_lifecycle.png)

# Considerations when deploying to production

:::::::::::::: {.columns}
::: {.column width="40%"}

**Ideally, it should be...**

* Bug-free
* Working in different machines (reproducible) 
* Always updated 

:::
::: {.column width="60%"}

**However...**

* How can you easily redeploy software when a user found a bug?
* How can you define your environment and test on different machines?
* How can you release your software easily?


:::
::::::::::::::


# Continuous integration

- Simulates the process of installing and running your software in a "clean" computer
- Just a **configuration file** where various steps are specified (by us!) 
- Common CI/CD steps: `install -> test -> publish`
- These configuration files are executed by CI platforms

---

## Common CI/CD platforms we've been using here in TM 

![](ci_cd_platforms.png)


# Continuous integration at TM 


## Geomancer (Drone Cloud)


![](oss_lifecycle.png)

---

## Tiffany (Drone Cloud)

![](oss_golang.png)

--- 

## Spade (Internal Drone)

![](oss_golang_spade.png)

# One file to rule them all

A sample `.drone.yml` file. 

\small

```yaml
kind: pipeline
name: run-tests

steps:
- name: test
  image: python:3.6-stretch
  commands:
  - pip install -r requirements-dev.txt
  - pytest tests/
```

# Task

Our **main goal** is to run a continuous integration job in Drone for a TM repo!

1. Group yourselves into two or three!
    - One person will write the drone config
    - Another person (max 2) will work on writing some tests (atleast 2)
2. Choose one from the following projects
    - Fb-scraper (https://github.com/thinkingmachines/fb-scraper)
    - PizaPy (https://github.com/thinkingmachines/PizaPy)
    - BQUP (https://github.com/thinkingmachines/bqup)

---

3. Go to `drone.thinkingmachin.es` and enable the repository that you chose

![](drone-tm.png)

---

4. Create a Drone file in the root of your repository

As a starter, you can do something like this:

```yaml
kind: pipeline
name: run-tests

steps:
- name: test
  image: python:3.6-stretch
  commands:
  - pip install -r requirements-dev.txt
  - pytest tests/
```

Then add steps as needed. Check the [Drone CI
documentation](https://docs.drone.io/) for more info!

--- 

5. Then, commit and push away!

```shell
$ git commit -m "Add .drone.yml"
$ git push origin master 
```

6. A continuous integration workflow that just install requirements is not
   really useful. It would be nice if we can add some tests!
