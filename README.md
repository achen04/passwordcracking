<h2> Where Deep Learning Meets Password Cracking </h2>

This year, for my Cybersecurity class at Tufts University, I wrote a paper on a deep learning approach to password cracking by using Generative Adversarial Networks (GANs). What caught my attention in the beginning and inspired me to write a paper on this topic was PassGAN (https://arxiv.org/abs/1709.00440). I read through the works by the authors of PassGAN and thought that this was quite novel, using GANs for password cracking. It was a good intersection between my interest for machine learning and cybersecurity. I decided to dive deeper into the topic and explored the work along with the implications of this. 

As supporting material for my paper, I downloaded PassGAN (https://github.com/brannondorsey/PassGAN) and experimented with it to see how it performs on different password sets. The authors had used lists from RockYou and LinkedIn, but I wanted to see how PassGAN performs on smaller/less popular sets of passwords. 

My hypothesis was that PassGAN would not perform very well as a smaller set of password is likely to contain a larger variety of passwords and perhaps more outliers than what PassGAN can capture with its deep learning model (that was pretrained on a different set). 


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
After poking around the web, I found a list of MD5 password hashes that were leaked from coutnerstrike.cn which has 239,525 hashes (https://hashes.org/leaks.php?id=674). This is a considerably smaller dataset than the other ones that were tested in the PassGAN paper (RockYou had around 32 million, LinkedIn 6.5 million). I then opened up HashCat and started cracking, by running

```hashcat -m 0 hashes_parsed.txt passgan_gen_passwords.txt  -o cracked_hashes.txt```

Using the list of PassGAN's passwords, PassGAN was able to crack: 10,073 / 236,525, which is about 4.26%.

Here are some sample cracks (`hash:plaintext`)

```
aa47f8215c6f30a0dcdb2a36a9f4168e:daniel
e10adc3949ba59abbe56e057f20f883e:123456
9cbe9648489f5179555dd1e231476bde:123223
96fddc1d238e5b8a9a5fa1e2dd3bd296:121221
eb35422d524597fe2e060035d76a585a:love12
25f9e794323b453885f5181f1b624d0b:123456789
dd00462cc87475cd6e12e78f0f801020:7856123
d0763edaa9d9bd2a9516280e9044d885:monkey
5e0c656a3bba29081fa0bcdf7ba4f994:123056
f25a2fc72690b780b2a14e140ef6a9e0:iloveyou
4428c6c474502e61151877825bb41961:23456789
61d474d48cbaf0eda36d0795a24d4e25:011200
b9041ad28a0468f531d34279f133891a:121012
f74a10e1d6b2f32a47b8bcb53dac5345:loveyou
f1887d3f9e6ee7a32fe5e76f4ab80d63:123457
6b1628b016dff46e6fa35684be6acc96:summer
e36a2f90240e9e84483504fd4a704452:1234569
74d738020dca22a731e30058ac7242ee:loveme
```

Though the results do not sound impressive, but it was along the lines of what I hypothesized, the PassGAN would not perform very well with a small dataset due to the variability of the passwords. 

Furthermore, what I later realized from looking at the list of hashes and plaintext cracked passwords that can be downloaded from the original hashes.org website, was that because this site was operating in China, most of its users were most likely Chinese and thus many passwords were actually in Chinese, and not real English words (i.e. `zhangjinhao`, `zhaozhiyin1`, `caonima0476`). This can be one huge factor that played into the underperformance of PassGAN on this password set. Because PassGAN was trained on RockYou, a password list with predominately English-speaking users, most of the passwords that PassGAN was learning from are based on English words, not Chinese. Had I discovered this earlier, a different dataset of passwords would have been more ideal to actually test the performance of PassGAN. Thus, it makes sense why the cracked words are mostly common English phrases or numbers. I would not have imagined PassGAN generating Chinese words when it's training data was in English. Though, if PassGAN was trained on a Chinese list of passwords, this would be a different story.


<h3> Future works </h3>
If this CounterStrike dataset was bigger, I would have trained the model with this dataset in order to produce more accurate results. However, given the size of the dataset (236,199), I decided this wasn't large enough to split into both training and testing datasets. In the future, it would be interesting to see how PassGAN performs when trained with different datasets!

As well, to my knowledge, PassGAN does not sort the results to the most probable passwords at the top of the generated list. It would be a good addition to sort the results based on the probability the model believes the password to have, since if the user is on a limited time period and does not have time to run through the whole word list, this feature could be beneficial.

Lastly, when thinking about the set of counterstrike.cn passwords, if PassGAN was trained on a set of passwords coming from a Chinese-based audience, I speculate that PassGAN would do much better than a simple dictionary wordlist or the RockYou list, since it would actually be generating Chinese passwords. This then leads to the question, would PassGAN be able to learn from any language then? Theortically, the answer is yes, since as a deep learning model, it teaches itself from the dataset. And if the dataset was in Chinese, or Spanish, or any other language, it would generate its passwords based on the structure of that language. A very interesting thought indeed...And a dangerous one too, because that means when a non-English password database is leaked out from a different country, malicious attackers now have more tools to exploit the passwords. This means that passwork cracking and the boundaries we have once associated with it could very well have opened up.
