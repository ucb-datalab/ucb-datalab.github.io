---
layout: page
title: Home / Schedule
description: Course topics, lectures, and assignments schedule.

permalink: /
nav_order: 1
published: true
---

# Astronomy Data Science Lab

*Spring 2026*

## Overview

This course consists of three data-centric laboratory experiments that draw on a variety of tools used by professional astronomers. Students will learn to procure and clean data (drawn from a variety of world-class astronomical facilities), assess the fidelity/quality of data, build and apply models to describe data, learn statistical and computational techniques to analyze data (e.g., Bayesian inference, machine learning, parallel computing), and effectively communicate data and associated scientific results.  This class will make use of data from facilities such as Kepler, Gaia, the Sloan Digital Sky Survey, and the Hubble Space Telescope to explore the structure and composition of the Milky Way, stars, and galaxies throughout the local and distant Universe. There is a heavy emphasis software development in the Python language, statistical techniques, and high-quality communication (e.g., written reports, oral presentations, and data visualization). 

## Schedule

{% for module in site.modules %}
  {{ module }}
{% endfor %}