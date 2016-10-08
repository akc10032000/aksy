

                                    _______
                                   /      /
                                  / ???? /
                                 / ___  /
                                /_/  /_/ S K Y

Asky is a simple program which helps its user prepare for exams. It doesn't
solve maths but does a good job at helping one prepare for objective type
questions. What makes Asky different from other similar programs is its
simplicity; preparing a question/answer session is a matter of creating two
files.

One down point of Asky, for inexperienced *nix users, is that it uses
RegEx to match the user given answer and the correct answer. Actually, this
feature let's Asky ask unlimited kinds of questions, such as MCQs,
Case-in/sensitives, etc., without creating a special case.

    TOC

1. Installing Asky
2. Using Asky
3. Creating custom QA-pairs
4. Thanks

    1. Installing Asky

Very simple. Clone Asky from GitHub (https://github.com/akc10032000/asky/), extract all files and in the main directory run python3 setup.py install as root, like this:

    $ sudo python3 setup.py install
    
    2. Using Asky

Asky is used from the command line. To run Asky, do this:

    $ asky questions_file answers_file

You need to supply two files, collectively called a QA-pair. An example
QA-pair is provided with Asky, so you can do this which will work.

    $ aksy Q A

    3. Creating custom QA-pairs

The example QA-pair included is fairly self-explanatory, but still here is an
informal tutorial for n00bs (just kidding!).

A Q file contains questions which will be displayed on screen while an A file
contains answers to the questions in the Q file which the user is expected to
enter. The answers in the A file are in the form of RegEx and if the user's
answer matches the RegEx, the user given answer is correct.

Note: The first line in the A file is the answer to the question in the first
line of the Q file, same rule applies for the second, third and following
lines.

    4. Thanks

Thanks for using Asky. If you have any suggestion, request, complain, etc.,
drop me a mail at akc10032000 [ __AT__ ] gmail [__DOT__] [ __COM__ ].
