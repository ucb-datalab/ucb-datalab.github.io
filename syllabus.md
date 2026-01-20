---
layout: page
title: Syllabus
description: >-
    Course policies and information.
nav_order: 3
---

# Syllabus
{:.no_toc}

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

---

## Overview

This course consists of three data-centric laboratory experiments that draw on a variety of tools used by professional astronomers. Students will learn to procure and clean data (drawn from a variety of world-class astronomical facilities), assess the fidelity/quality of data, build and apply models to describe data, learn statistical and computational techniques to analyze data (e.g., Bayesian inference, machine learning, parallel computing), and effectively communicate data and associated scientific results.  This class will make use of data from facilities such as Kepler, Gaia, the Sloan Digital Sky Survey, and the Hubble Space Telescope to explore the structure and composition of the Milky Way, stars, and galaxies throughout the local and distant Universe. There is a heavy emphasis software development in the Python language, statistical techniques, and high-quality communication (e.g., written reports, oral presentations, and data visualization). 

This course satisfies the [<b>Data Science Major requirement</b> for "Computational & Inferential Depth"](https://cdss.berkeley.edu/dsus/academics/majorrequirements#section-el--2) and the the <a href="https://astro.berkeley.edu/programs/undergraduate-program/astrophysics-major">laboratory requirement for the <b>Astronomy Major</b></a>. 

## Course Philosophy

This class is effectively an introduction to astronomical research from a data-centric perspective. The labs are designed to be challenging, yet manageable mini-research projects. They will be time-consuming. Often when doing research, you will not have all the necessary technical skills to complete a project. It is normal to have to learn new skills along the way. A main aim of this class is to provide exposure to those skills, in a setting that requires you to think and act like a researcher, but with extra guidance and resources. You should also get used to asking questions that seem basic (sometimes embarrassingly so) in hindsight, and working in open and collaborative environments.

The weekly lectures will provide you with broad background, but are not intended to teach all the nitty-gritty technical skills you need. Much like real research, these are skills you learn on your own, in groups, and/or in consultation with an advisor. Ask questions via Ed Discussion and office hours, particularly with the GSIs.

Research is fun, but challenging. It usually does not progress linearly, and you often have to take a few steps backward before ultimately moving forward. *Ultimately, we want you to succeed in this class. We know that Berkeley can at times be an overwhelming place. If you find yourself struggling to keep up, please come talk to us, we’re here to help you succeed.*

## Course Goals

- Introduce and motivate a range of analysis techniques and data pipelining
- Gain practical, in-depth experience with real, open-ended astronomical challenges
- Build reproducible, well-tested, well-documented software
- Learn to work with open data and code in an open science environment
- Hone presentation and visualization skills
- Develop skills applicable to careers in academia and industry

## Prerequisites

- This class assumes that you have completed **introductory astrophysical instruction** (ASTRON 7A and 7B, or higher such as ASTRON 160/161) as well as knowledge of calculus (including Math 53) and **linear algebra** (MATH 54 or PHYSICS 89).
- You should have **proficiency or fluency in the Python programming language**. This class heavily emphasizes software development, and is *not* the place to learn Python for the first time.

## Lecture

There are two live lectures per week, held on **Tuesdays and Thursdays from 2:00–3:30 PM in Campbell Hall 131**. Attendance and engagement with lectures is important, though not mandatory but can contribute towards your partcipation grade. Please have your computer ready for interactive demos and to work on your labs in class. In-class materials will be posted on the course website within 24 hours whenever possible.

## Office Hours

See the [calendar](/sp26/calendar) for the regular office hours schedule and check the Ed discussion page for any changes.

## Communication

- Our preferred method of communication is through the class **Ed Discussion** site linked on the top of this page. 

    - Ed is a formal, academic space. We must demonstrate appropriate respect, consideration, and compassion for others. Please be friendly and thoughtful; our community draws from a wide spectrum of valuable experiences. For further reading, please reference [Berkeley’s Principles of Community](https://diversity.berkeley.edu/principles-community) and the [Berkeley Campus Code of Student Conduct](https://conduct.berkeley.edu/code-of-conduct/).

    - Ed is your primary platform for asking questions about the class. It is monitored daily by course staff, so questions posted to Ed will likely receive the fastest response.

    - You will automatically be enrolled in the course if you are enrolled on bCourses. If there are any issues being enrolled on Ed please reach out via email or before/after lecture to the TA. 

- All assignments will be submitted via Gradescope which is also linked at the top of the page.

- Email is okay for logistical or sensitive items (e.g., scheduling a meeting time with an instructor), but Ed Discussion is preferred.

## Readings

- [“Statistics, Data Mining, and Machine Learning in Astronomy: A Practical Python Guide for the Analysis of Survey Data”](http://a.co/i3fnkw4) by Željko Ivezić et al.

- [“An Introduction to Modern Astrophysics”](https://www.amazon.com/Introduction-Modern-Astrophysics-Bradley-Carroll-dp-1108422160/dp/1108422160/ref=mt_hardcover?_encoding=UTF8&me=&qid=) by Bradley W. Carroll & Dale A. Ostlie

- [“Foundations of Astrophysics”](https://www.amazon.com/Foundations-Astrophysics-Barbara-S-Ryden/dp/0321595580/ref=sr_1_1?crid=VMVWRPQ07B5T&keywords=ryden+and+peterson&qid=1576537687&s=books&sprefix=ryden,stripbooks,177&sr=1-1) by Barbara Ryden & Bradley Peterson

- Lab instructions and topical handouts linked on the class webpage.

## Computing Resources

{: .note }
Some of the labs are computationally intensive. Each student will be given access to [Datahub](https://astro.datahub.berkeley.edu) and the [Savio HPC cluster](/sp26/resources/savio) to execute their code. 

We are committed to ensuring that every student in our department is able to engage in our courses without incurring undue financial burdens.

If you are in need of a personal laptop or other technology to complete academic work this semester, the [Student Technology Equity Program](https://studenttech.berkeley.edu/step) (STEP) can provide need-based loans for a variety of hardware to Berkeley students. Applications are now open for the Spring 2026 semester. We encourage you to apply as soon as possible as it will take 1-2 weeks for the application to be processed.

If you are in need of shorter term access to technology, Berkeley Library offers first come, first serve laptop lending. These loans are only available for up to 14 days, so they are not a solution for a full semester, but can help for moments where you may need short term access to a computer, including the waiting period before your STEP loan is approved. See [here](https://www.lib.berkeley.edu/about/device-lending-policy) for the checkout form and a complete list of offerings.

## Grading

Grading Breakdown:

| Category      | Weight | Details |
| :-----------: | :----: | :------ |
| Lab Reports   | 60%    | 3.5 lab reports |
| Checkpoints   | 25%    | 10 checkpoints & presentations; lowest checkpoint score dropped |
| Participation | 15%    |         |

### Lab Reports

Lab are to be submitted as a written report formatted on LaTeX for Labs 1-3 or 
as polished, executable Jupyter Notebook for Lab 0. All code files are to be
submitted for the full length labs as well, those this will not be run by course
staff. Labs are before specified due date/time on Gradescope which is typically 
at 11:59 PM on the date listed on the [course schedule](/sp26/schedule).

Collaborate (talk, draw pictures, analyze data) with your lab mates, but you 
**MUST** implement separately (your own equations, code, plots, writing)

Labs:
- Lab 0: Stellar Clusters: Introduction to ADQL and Gaia Data *[50 points]*
- Lab 1: Galactic Dust and RR Lyrae Stars *[100 points]*
- Lab 2: Modeling Stellar Spectra *[100 points]*
- Lab 3: Galaxy Morphology with Convolutional Neural Networks *[100 points]*

Most of the labs will have some form of extra credit that can be attempted, but 
the primary focus should be the required components. The grading for the full 
length labs (1-3) is split into 4 parts as follows:
- **Technical Components (~50% of raw score):** This section is graded on a 
majority of technical components that make up the analysis of the lab. For full
credit on this section, anaylsis must be thorough and include discussion of any 
issues or choices along the way. This should be in the style of a research 
paper; we don't want to see the code, but what decisions went into it. The lab
instructions highlight some questions in magenta. If your report discusses all 
of these questions, you will hit all of the technical components expected in the
rubric. *This is where you can earn extra credit.*
- **Report Componets (25% of raw score):** This section is graded on whether or
not your report reads as a cohesive paper. We don't want to see a step-by-step
walkthrough of what you did (e.g., First, I downloaded the data, then I cleaned
it using ABC. Finally, I analyzed it using XYZ method.). Instead it should
follow a lab report structure discussing the data, methods, and results while 
also including a introduction to the topics and a discussion of your results. A
big part of this section of the grade is your discussion of uncertainties, so 
make sure you are thorough in explaining why your results may or may not differ
from what you expect.
- **Figures (~20% of raw score):** This section is graded on the quality of your 
figures (i.e., legibility, clarity, etc.), not the accuracy. 
- **Code Submission (5% of raw score):** This section is graded purely on
completion. Submit your code to the respective Gradescope assignment for full 
credit on this section.

#### Slip Days & Late Policy

Each person is allocated 8 "slip days" for the semester. These are days you can 
use to turn in a lab report late without any penalty by submitting the [Slip Day 
Form](https://forms.gle/vmep1eGW7iGsm1RJ7) which can also be found in a pinned 
Ed post. **You must submit your slip day form no more than 24 hours after you 
turn in the assignment.** You can allocate them as you see fit throughout the 
semester, though ***we will not allow changes to the number of slip days applied 
once grades for that lab are posted***. If you want to change the number of days 
you decide to use before the lab grades are posted, simply resubmit the Slip Day 
Form and the most recent submission will be used.

**NO** extensions for labs will be granted beyond the 8 slip days except for 
demonstrated extenuating circumstances communicated to the course staff. Once 
all slip days are used, then late lab grading policy is -10% x raw score x 
number of days late. 
- For example, a lab submitted 2 days late with no slip days used that got a 
raw score of 90 points would be reduced by -0.10 x 90 x 2 = -18 pt, yielding a 
total of 72 points for the lab.
- The late point deducted score can be found on bCourses and the raw score can 
be found on Gradescope.

Each unused slip day at the end of the semester is worth 0.25% extra credit 
toward your final class grade. 

### Checkpoints

- Short assessments to gauge your understanding and completion of individual checkpoints to be submitted on Gradescope. Graded on completion though all questions must be appropriately answered and some effort towards completion must be shown. These are designed to be a self-assessment on whether you are on track with the lab material, so please complete them even if you have not gotten to the deliverable listed in the lab instructions. **(10% of total grade)**
    - The lowest score of these short assessments will be dropped in your final grade calculation.
- Short presentations to be given during class in groups of 3-5 members. Details on the format and expectations will be given during class. **(15% of total grade)**

### Participation

- Participation can take many forms including asking questions during lecture, leading group discussion, participating in presentations, posting questions AND answers to others questions on Ed Discussion, attending office hours, and more.
- The key is for you to be actively engaged in the class.
- *Historically, those with low class participation scores are unable to get an A in this class.*

## Class Conduct

*This is a work-intensive class.* You are going to spend significant time on your own in the lab with minimal supervision. At all times, you are expected to abide by the [UC Berkeley Code of Conduct](https://sa.berkeley.edu/code-of-conduct), acting with respect to your peers, GSIs, and instructor. Should you experience any form of harassment or discrimination, we maintain a [list of resources](https://astro.berkeley.edu/department-resources/reporting-harassment) that can help you decide how to respond. GSIs and instructors are non-confidential reporters; we have a legal obligation to act on any reports of harassment. Please know that we take our responsibility seriously.

## Collaboration Policy (don't cheat)

This is a collaborative class. To repeat what is written previously in the syllabus: while you should talk with others about the labs and we strongly encourage collaboration, **we require that you write your code, solutions, and reports individually.**

## Use of AI

You are not allowed to use AI (e.g., Gemini, ChatGPT) to generate submitted material (i.e. checkpoints and labs) for this class. Such use of AI will result in a zero and, depending on the situation, may also be considered grounds for academic misconduct. You may use AI in other ways outlined in the [department AI use policy](/sp26/ai-policy). You must make an “AI declaration of use” statement at the end of your lab report outlining in detail what tools were used and how to answer specific questions. When in doubt, ask for clarification from the instructors.

## DSP Accomodations

UC Berkeley is committed to creating a learning environment that meets the needs of its diverse student body including students with disabilities. If you anticipate or experience any barriers to learning in this course, please feel welcome to discuss your concerns with me.

If you have a disability, or think you may have a disability, you can work with the [Disabled Students' Program](dsp.berkeley.edu) (DSP) to request an official accommodation. The [Disabled Students' Program](dsp.berkeley.edu) (DSP) is the campus office responsible for authorizing disability-related academic accommodations, in cooperation with the students themselves and their instructors. If you have already been approved for accommodations through DSP, please meet with the course instructors so we can develop an implementation plan together. Note that per University policy, we can only provide DSP accommodations if an official letter is provided by the DSP office.

## Waitlisted Students

If you are on the waiting list, you must still do all coursework and complete labs and homework by the deadlines. We will not be offering extensions if you are admitted into the course later. So it is your responsibility to stay up to date on the assignments. You are welcome to attend lectures while you are on the waiting list. Rooms may feel a little crowded in the first week.

{: .important }
Unfortunately, doing all the work is **not** a guarantee of enrollment. You will only be enrolled if there is space in the course. Enrollment will proceed by CalCentral.

## [Syllabus PDF](https://github.com/ucb-datalab/course_materials_sp2026/blob/main/Astro_128_256_syllabus_Fall2026.pdf)