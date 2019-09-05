# TM Open-Source Fridays 

[![Build Status](https://cloud.drone.io/api/badges/thinkingmachines/open-source-fridays/status.svg)](https://cloud.drone.io/thinkingmachines/open-source-fridays)

This repository contains all materials for OSF!

**What is OSF?** [Open-source fridays](https://opensourcefriday.com/) is a
biweekly workshop for learning the ins and outs of open-source software
development. It aims to skill you up as an open-source contributor!


## Target Audience

This is intended for someone who wants to get started in open-source or learn
basic software engineering skills as they work in TM. We do not expect any
software engineering experience (although they will certainly help) as we go
through most of these workshops, so feel free to join along!

## Recommended Approach

It would be better to join the in-person Open-Source Fridays (OSFs) so that we
can better guide you with the materials. On the other hand, it is possible to
follow these tutorials on your own, we're making sure that each lesson is
self-contained and appropriate to the declared skill-level.


#### Difficulty

- :octocat: : perfect for beginners with no prior software development experience.
- :octocat: :octocat: : requires completion of atleast one OSF session.
- :octocat: :octocat: :octocat: : requires completion of atleast two OSF sessions.

## Topics

| # | Topic                                    | Description                                                                                                                                                                                                  | Difficulty                    |
|---|------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------|
| 1 | [Writing your first Pull Request](https://github.com/thinkingmachines/open-source-fridays/tree/master/OSF01_Your-first-pull-request/)          | Pull Requests (PRs) are vital to participate in open-source. In this workshop, you'll learn how the open-source workflow works and then make your first pull request!                                        | :octocat:                     |
| 2 | Reviewing other's code                   | Reviewing and reading others' code is an important skill in open-source. In this workshop, we'll teach you how to review others' code as we help port old stories into the new TM website!                   | :octocat:                     |
| 3 | TM Code standards and pre-commits        | We follow a certain code standard in Thinking Machines. To enforce that, we recommend the use of pre-commits. Today, you'll learn about the pre-commit workflow and set-up pre-commits in your computer.     | :octocat:                     |
| 4 | [Structuring your repository](https://github.com/thinkingmachines/open-source-fridays/tree/master/OSF04_Structuring-your-repository)              | If you have an idea in mind (automating workflows, simplifying scripts, etc.), then we'd recommend you to follow through this workshop so that you can structure your repository effectively!                | :octocat: :octocat:           |
| 5 | [Writing tests and modularizing your code](https://github.com/thinkingmachines/open-source-fridays/tree/master/OSF05_Writing-tests) | Writing tests to check the code you've written is integral to maintaining open-source code. In this workshop, you'll learn how to make your code "test-friendly", and write tests to check if they're right! | :octocat: :octocat: :octocat: |
| 6 | [Documenting your projects](https://github.com/thinkingmachines/open-source-fridays/tree/master/OSF06_Documenting-your-projects) | Documentation is one of the best ways we can contribute to open-source projects. Every project will always need some documentation help! In this workshop, you'll learn how to set-up Sphinx docs for your Python project, and learn best practices when writing docs | :octocat: :octocat: :octocat: |
| 7 | [Continuous Integration and Deployment](https://github.com/thinkingmachines/open-source-fridays/tree/master/OSF07_Continuous-integration-and-deployment) | Let's start putting everything together we've learned so far and build a pipeline that takes our open-source projects from development to production! | :octocat: :octocat: :octocat: |

## Compiling the slides 

All slides are generated straight from Markdown using
[Pandoc](https://pandoc.org/) and [LaTeX
Beamer](https://www.overleaf.com/learn/latex/Beamer) with the [metropolis
theme](https://ctan.org/pkg/beamertheme-metropolis). You can always view the
generated slides from the links above, but if you wish to **compile from
source**, you'd need the following dependencies:

- LaTeX installation (Texlive for Linux, MikTeX for Windows, MacTex for MaxOS)
- FiraSans font (if not installed, the default Computer Modern Sans is used)
- Pandoc 2.7.1 and above

To compile all slides, simply run the following:

```shell
make build-all
```

You can opt to compile a single slide by passing its title (i.e., directory name):

```shell
make build TITLE=OSF05_Writing-tests
```

If you wish to make a new slide deck, simply pass the deck title again:

```shell
make new TITLE=OSF0X_My-new-title
```

## Others

Found any bugs or documentation errors? Want to improve OSF's content? Then
open up a [Pull
Request](https://help.github.com/en/articles/creating-a-pull-request)! If you
don't know how to, then check our first OSF topic!

Lastly, if you have any questions, then feel free to post on our #opensource
Slack channel, or just approach
[@ljvmiranda921](https://github.com/ljvmiranda921),
[@marksteve](https://github.com/marksteve), or
[@jgtiu](https://github.com/jgtiu)!

## License

MIT License (c) 2019, Thinking Machines Data Science
