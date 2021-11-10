# Report by Noor Buchi

## Completed Timeline (Due by Monday, October 25 11:30am)


| Timeline  | Tasks |
| ----------- | ----------- |
|   10/27    |    Complete data collection  |
|   10/29    |    Implement Text Generation  |
|   11/01    |    Assessment of Model  |
|   11/03    |    Simple demo  |
|   11/05    |    Model Adjustments  |
|   11/08    |    Final Changes  |

## Progress Update (due on October 29 by 11:30am)

So far, I created a movie and TV show data set. Additionally, I collected and stored all the plot and synopsis for each movie and show. They are ready for the next steps which is preprocessing. I'm a little behind on the schedule but I'm planning to catch up as soon as I can.

## Data

The data used to train the ai model is the synopsis of hand selected movies and
shows. A list of the movies and shows can be found in the `dataset.yaml` file.
The items were selected based on it's genre, if a movie or a show contained
sci-fi elements such as robots, ai, time travel or other futuristic concept,
then it was included in the list. Once the list was created, I used
[IMDbPY](https://imdbpy.github.io/) to make requests and get the synopsis to
each data item. For each item the database returned multiple synopsis that were
phrased somewhat differently. All of them were kept for the purposes of training
the model. Additionally, for tv shows, the data miner iterated through every
season and episode of the show and retrieved the individual synopsis of each episode.

## Text Generation

Describe the techniques used for an automated generation of your script synopsis. Cite (provide a link to) any sources you have used. Include your generated text (or its snippet) below.

In order to train the AI model that generates the text
[aitexgen](https://github.com/minimaxir/aitextgen) was used. It makes text
generation very easy by abstracting many details that can be challenging to
implement. The training phase took about 3 hours to complete and produced a
model object where the `.generate()` function can be called on. Two similar
models were trained for this lab, the first one, stored in
`model with shows/my_model.pkl` includes fewer movies but also contains the 3
listed shows in `dataset.yaml`. The second one, however, only contains the
movies listed in the dataset. This was done after noticing that the data
collected from the shows sometimes overwhelmed the generated output due to it's
over representation. To use these models, they can be uploaded to Google Colab
in addition to `generator.ipynb`. The last section contains code to deserialize
and use the stored model.

The most accurate and meaningful generated text by the technique I used is
listed here. It's a mixture of strings generated at different phases with some
minimal reformatting and small fixes. The text is:

```
It starts with world; Dolores has trouble separating her dreams from reality; The Man in Black looks to the past.
Bernard discusses with Dr. Ford asking why he forced him to kill his beloved
Theresa. Dolores and Bernard reconnect with their pasts. Delos, Charlotte prambles to protect Delos' most prized asset; Bernard gets closer to the truth.
An enigmatic figure becomes the centre of Delos' secret project; The Man in
Black and Lawrence follow the clues.
```

Other generated text is also listed below. Although it's not
coherent and contains many mistakes, it's interesting and sometimes funny. Here
are some honorable mentions:

```
In a world of the monolith, beneath the surface of the planet in a mission to evolution, Sometime in the earthlings have moved to Saturn's moon Titor.
==========
After the Artificial Intelligence, working to create a sentient machine that
combines the hosting. Sarah Conrings are under suspected. The Man in
Black seeks help from a conddemn
==========
before the numbing in the world.
PA young, Imperial Foster must discover the new programmer at the first of the planet in the fate of the diplity and Earth has become cosuring everyolonized that yet import
==========
when a resistance against the machines, conquertects, Smperor --Kyle coper's son embark on a question - even embles who will stop at him to exploit the fate of space.
==========
thoughts working ged by law enforcing robot capable against the Death Star
before it can annihilate all hope of restoring freedom to the galaxy.
==========
```

## Text Analysis

TODO:
Describe the techniques used for an automated text analysis of your automated script synopsis. Cite (provide a link to) any sources you have used. Include a graph or textual output of your analysis. Include your output below.

```
Output Here
```

## Experimental Analysis

TODO:
Describe the experiments you conducted to evaluate text generation and text analysis.

## Supplemental Production

TODO:
Describe the supplemental production you have created. Include an image if relevant.

## Challenges and Learning Experiences

TODO:
Discuss any challenges you have encountered during the work on this lab and  describe what have you learned.

## Ethical Benefits and Implications

TODO:
If you are unable to discern specific themes related to future technology use from your synopsis, provide a manually edited version of your synopsis below.

```
(Optional) Modified Synopsis
```

Then, hypothesizing on the issues highlighted in your generated (or modified) text, answer the following questions.

1. What future technology is featured in your synopsis?

2. What are the potential social implications and/or ethical issues and/or regulatory challenges with this technology?

3. What do you think might be a cautionary tale related to this technology?

4. What fictional person in the future could best illustrate this caution?

5. What is their story?

6. Now, consider what benefit can come out of the  technology featured in the story and how can we work towards preventing the negative consequences of the future they envision?
