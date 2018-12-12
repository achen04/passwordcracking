<h2> Where Deep Learning Meets Password Cracking </h2>

This year, for my Cybersecurity class at Tufts University, I wrote a paper on a deep learning approach to password cracking by using Generative Adversarial Networks (GANs). What caught my attention in the beginning and inspired me to write a paper on this topic was PassGAN (https://arxiv.org/abs/1709.00440). I read through the works by the authors of PassGAN and thought that this was quite novel, using GANs for password cracking. It was a good intersection between my interest for machine learning and cybersecurity. I decided to dive deeper into the topic and explored the work along with the implications of this. 

As supporting material for my paper, I decided to download PassGAN (https://github.com/brannondorsey/PassGAN) and experiment with it to see how it compares to other tools like HashCat in generating a high-quality word list of password guesses. The authors had used lists from RockYou and LinkedIn, but I wanted to see how PassGAN performs on smaller/less popular sets of passwords. 

My hypothesis was that PassGAN would not perform very well as a smaller set of password is likely to contain a larger variety of passwords and perhaps more outliers than what PassGAN can capture with its deep learning model. 


<h3> PassGAN's generated wordlist </h3>

After running PassGAN with their pretrained model, it generated a list of of around 32 million passwords. Some of the passwords are:

```ca³jame
maina
ruga41000
aauraka
hello
barkyan
ibb12
tigbie97
malayhy
120030 
```
The full list can be found in the file `passgan_gen_passwords.txt`.


<h3> Cracking counterstrike.cn password hashes </h3>
After poking around the web, I found a list of MD5 password hashes that were leaked from coutnerstrike.cn which has 239,525 hashes (https://hashes.org/leaks.php?id=674). This is a considerably smaller dataset than the other ones that were tested in the PassGAN paper (RockYou had around 32 million, LinkedIn 6.5 million). 

Using the list of PassGAN's passwords, PassGAN was able to crack: 10,073 / 236,525, which is about 4.26%.



What I later realized from looking at the list of hashes and plaintext cracked passwords that can be downloaded from the original hashes.org website, was that because this site was operating in China, most of its users were most likely Chinese and thus many passwords were actually in Chinese, and not real English words (i.e. `zhangjinhao`, `zhaozhiyin1`, `caonima0476`). This can be one huge factor that played into the underperformance rate of PassGAN on this password set. Because PassGAN was trained on RockYou, a password list with predominately English-speaking users, most of the passwords that PassGAN was learning from are based on English words, not Chinese. Had I discovered this earlier, a different dataset of passwords would have been more ideal to actually test the performance of PassGAN. Nonetheless, this was an interesting observeration. 



<h3> Future Works </h3>
If this CounterStrike dataset was bigger, I would have trained the model with this dataset in order to produce more accurate results. However, given the size of the dataset (236,199), I decided this wasn't large enough to split into both training and testing datasets. In the future, it would be interesting to see how PassGAN performs when trained with different datasets!

As well, to my knowledge, PassGAN does not sort the results to the most probable passwords at the top of the generated list. It would be a good addition to sort the results based on the probability the model believes the password to have, since if the user is on a limited time period and does not have time to run through the whole word list, this feature could be beneficial.
