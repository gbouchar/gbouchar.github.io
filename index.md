---
layout: index
title:  Welcome!
cmeta:  "Homepage of Guillaume Bouchard, researcher in machine learning, natural language processing, artificial intelligence"
---

<a href="img/GuillaumeBouchardChamechaude.jpg" style="cursor: default">
    <img id="portrait" src="img/GuillaumeBouchard.jpg"
        alt="Guillaume at the top of Chamechaude in Chartreuse montains, France"/>
</a>
I'm Guillaume Bouchard, Founder and Director of [Bloomsbury-AI][bai], an early-stage company that enables everybody to teach what they know to the computer through a written conversation. I'm also associate researcher in the [Machine Reading team][uclmr] at  [University College London][ucl] (UCL). Previously, I worked 11 years at [Xerox Research Centre Europe][xrcegb] in Grenoble, France. I'm passionate about [Machine Learning][ml]
and [Natural Language Processing][nlp] (NLP). Since many years, my unique goal is to replace programming languages with natural language, as shown in these videos: [Playfair AI summit 2015 (20 minutes)][videobai] and [Entrepreneur First Demo Day 2016 (5 minutes)][videoefdd]. 

My research interests are closely related to the mathematical modelling of the world, especially when this helps to 
solve real worl problems. I'm a big fan of:
* *variational inference*: how to transform an intractable integral into an optimization problem. Classically, people use a method called Variational Bayes (VB) which is based on Jensen inequality, but I found a [new way][vh] of doing using Holder inequality that has much nicer theoretical properties. 
* *stochastic optimization*:  using randomization techniques to learn faster. In particular the concepts of *[learning to sample][awsgd]* and *learning to optimize* seem to be really promising research topics, 
* *factorization model*: why spectral theory appear naturally in many different areas and why embedding models can the seen as [good prior for logical reasoning][signrank].

In natural language processing, I have been interested for many years in flexible models that can learn from a huge amount of 
data. The hope is to automatically learn general facts about the world, without having to specify an intermediary representation, such as grammatical classes or ontologies. This means:
* *language models*: a generative model of text, this can take many different form, but basically, a language model gives you a high score for sentences that are plausible.
* *machine reading*: this can be viewed as a question-answering system where there is some extra information, such as questions about a short story, science exams questions. The real reason why I'm interested in this techniques is that question-answering is the equivalent of "debugging" when you write software code, but this makes life so much easier when the computer speaks your language (and adapts to your language as well...).

If you share any of my research interests, do have a look at my [list of publications][pubs] since 2015 and if you have questions regarding my previous and/or current research, feel free to contact [me][contact]. I'm part of the [UCL Machine Reading Group][uclmr] lead by [Sebastian Riedel][seb]
in the [Department of Computer Science][uclcs]. I received a PhD in 2004 from Institut National de Recherche en Automatique et Informatique ([INRIA][inria]) and [University Joseph Fourier][ujf].

[contact]:   /contact.html
[ml]:        https://en.wikipedia.org/wiki/Machine_learning
[nlp]:       https://en.wikipedia.org/wiki/Natural_language_processing
[pubs]:      /publications.html
[ucl]:       http://www.ucl.ac.uk/
[uclcs]:     http://www.cs.ucl.ac.uk/
[uclmr]:     http://mr.cs.ucl.ac.uk/
[bai]:       http://bloomsbury.ai/
[videobai]:  https://www.youtube.com/watch?v=sKZD8huxjZ0 
[videoefdd]: https://www.youtube.com/watch?v=N0mRn1bQyzU
[xrcegb]:    http://www.xrce.xerox.com/About-XRCE/People/Guillaume-Bouchard
[inria]:     http://www.inria.fr/en/
[ujf]:       https://www.ujf-grenoble.fr/?language=en
[seb]:       http://www.riedelcastro.org/
[vh]:        http://arxiv.org/abs/1506.06100
[awsgd]:     http://arxiv.org/abs/1506.09016
[signrank]:  http://www.aaai.org/ocs/index.php/SSS/SSS15/paper/view/10257
