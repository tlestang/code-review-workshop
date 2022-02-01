- [Code Review](#orgb43a79d)
- [Returns on investement](#org54a0b82)
- [Good practices](#org4f7ff08)
- [Getting started with code review](#org7e50dcf)


<a id="orgb43a79d"></a>

# Code Review

-   Discussion over a piece of code. Typically between the author and a reviewer who provides feedback on code quality and/or functionality.
-   Code review is fairly common in the software industry and open source communities.
-   Code review is beneficial at different levels:
    
    -   Increased code quality (.e.g readability)
    -   Knowledge transfer and mentoring
    -   Team awareness and group ownership of the project.
    -   Reduction of bus factor
    
    Overall code review benefits both individuals and a team's productivity and wellbeing.
-   Code review can take different forms,
    -   Synchronous (live) discussion.
    -   Asynchronous discussion (email or development platforms like GitHub).
    -   One to one (1 author and 1 reviewer)
    -   Many to one
    -   Many to many
    -   &#x2026;
-   Code reviews are performed throughout a project, on small changes, as opposed to larger end-of-work reviews.


<a id="org54a0b82"></a>

# Returns on investement

-   Improved code quality.
    
    -   Readability is difficult to self-assess. How can you tell if your code is readable?
    -   Feedback on design decisions. Particularly important if you are writing a library.
    -   Catch sight of gotchas: performance, language idioms, design flaws, corner cases. "Second pair of eyes effect".
    
    Code reviews are excellent at assessing readability. Few researchers submit a paper or grant proposal without several rounds of feedback by colleagues. Should code be different? If you think that no one will read your code or reuse it, think again.
-   Learning and knowledge transfer.
    
    -   Montoring and disseminiation of best practices from more experienced to less experienced.
    -   Even two researchers with similar programming experience can learn a lot from comparing their different approaches.
    -   Less experienced researchers are valuable reviewers. They are an excellent benchmark of readability and are rewarded with mentored exposure to more advanced practices.
    
    Regular code reviews within a resaerch group can quickly level the group up and raise less experienced member's condifence.
-   Collaboration
    -   Regular code reviews means regular interactions and discussions between members of a research team or community. This reinforce group awareness, trust and cohesion. Beyond productivity as a group, it makes work nicer.
    -   Opportunities to "talk code", instead of focusing on the science. Experimentalists discuss their tools all the time, research software developers can talk about theirs too. This in turn impacts the science.
    -   Improved software sustainability. Typical timescale of research software is 3 years (or duration of a PhD/post-doc contract). Code reviews help spreading ownership of the code and transfer it to new arrivals.


<a id="org4f7ff08"></a>

# Good practices

-   Small code reviews, often.
    -   reviewing code demands strong focus.
    -   if your code is reviewed regularly, you *have* to keep it in a tidy state. I.e. you have to keep readers in mind.
-   Acknowledge the code author's responsability.
    -   Submit small and coherent set of changes.
    -   Ensure good layout of the code.
    -   Self-review, write tests.
    -   Provide context to the reviewer.
-   Start with a discussion.
    -   Levels of experience should be acknowledged and expectations set before the review starts. A reviewer will look at the code differently whether they look for bugs or performance issues.
        -   Author is a begineer programmer and reviewer is experienced. Author thinks that code is slow but both agree that review should focus on readability.
        -   Author and reviewers are colleagues with similar level of programming experience. Author's code is performing surprinsigly badly. Both afree that they should have a look at performance and refrain from spending too much time on discussing language idioms and functionalities.
    -   Be sure you understand the other person's context and mindset before reviewing code or engaging with feedback.
-   Take difference of perspectives into account, at all times.
    -   A "reasearcher who codes" will have a different perspective than a Research Software Engineer.
    -   Adapting your feedback or explanations to the other's perspective is key to a succesful code review. Experienced programmers must force themselves to "state the obvious". Less experienced programmers must accept that some comments may seem pointless at first sight.
-   The code is under review, not its author.
    -   As a reviewer, acknowledge that author put himself in a vulnerable position by openning their work for feedback.
    -   "You should rename this function" vs "This function could (should?) be renamed" vs "This function's name didn't help me understand what it does". A reviewer is better off raising questions for the author to reach their own conlusions, rather than expressing a judgement.
    -   Authors must accept negative criticism of their code, or suggestion of alternatives.
    -   If reviewer's feedback is deemed unfair or aggressive by the author, it is their prerogative to disengage from the review process.


<a id="org7e50dcf"></a>

# Getting started with code review

-   Find reviewers
    -   In your research group
    -   In your lab
    -   In your institution (code review club or network)
    -   Ask your PI!
-   Choose a code to review
    -   Lower your expectations
    -   Aim for 45 minutes max for a reviewer, rule of thumb 200 LOC.
    -   Likely the whole codebase won't be reviewed. Pick a part that you are not confident about (or very confident if you wish to challenge your assumptions). Pick a part that is representative of your programming practices.
    -   The reviewer can help choosing the code to review.
-   Start with a conversation
    -   If needed, introduce yourself, your background and relevant experience.
    -   State any expectations for the review process.
    -   As the author, provide reviewer with scientific and academic context. Example: this is a heavily numerical module that fits within a larger ecosystem. I have been working on this for the past couple of days. Example: This is a script that simplifies my own persnal experimental setup, I wrote it 2 years ago from another student's script.
    -   Come up with a benefit or goal for the review.
-   Decide on the form and agree to a plan
    -   prefer live discussion if possible. It makes it easier to identify the other person's mindset and build trust.
    -   Give the reviewer some time to make their own independent ideas. For instance they receive the code in advance.
    -   Small code reviews, often. If agreement to review a large codebase, agree on a series of meetings.
-   Engage in code reviews on a weekly basis. Make it part of your and your group's routine.