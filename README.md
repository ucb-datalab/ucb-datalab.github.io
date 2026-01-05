# ASTRON 128 Class Site

[![Pages Deployment](https://github.com/berkeley-cdss/berkeley-class-site/actions/workflows/jekyll.yml/badge.svg)](https://github.com/berkeley-cdss/berkeley-class-site/actions/workflows/jekyll.yml)
[![Run rspec tests](https://github.com/ucb-datalab/ucb-datalab.github.io/actions/workflows/rspec.yml/badge.svg)](https://github.com/ucb-datalab/ucb-datalab.github.io/actions/workflows/rspec.yml)

Based on a template for UC Berkeley class websites (with a focus on EECS/CS/DS courses).

## Installation

### Install Ruby and Bundler
**The berkeley-class-site template requires Ruby 3.3.7 or higher and bundler >= 2.6**
Install Ruby before continuing. You can check your Ruby version by running:

```bash
ruby --version
bundle --version
```

Prerequisites:

- You have everything that [Jekyll requires](https://jekyllrb.com/docs/installation/)
- You have installed [Bundler](https://bundler.io/): Run `gem install jekyll bundler`

Install dependencies:

```
cd YOUR_REPO
bundle install
```

## Usage

To run the site locally, run:

```
bundle exec jekyll serve
```

Note that if you alter `_config.yml`, you will need to rerun the above command to see the changes reflected.

Search throughout the repository for TODO items called `TODO(setup)` and complete them to customize the site for your course.

## Updating Material

Import your course schedule as `schedule.csv` and run the script `setup_schedule.py`. Make sure your imported schedule follows the same format as the [template](). The script will setup the schedule on the home page and ensure links are released on the provided schedule.

<!-- ## Deployment

The easiest way to deploy your site is with [GitHub Pages](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/about-github-pages-and-jekyll). -->

## License

[MIT](LICENSE)
