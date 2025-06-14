<p align="center"><img src="https://github.com/tassiovirginio/jnose/blob/master/src/main/webapp/logo.png?raw=true" width="70"></p>

# JNose
Java TestSmells Detection

JNose Test is a tool developed to automatically detect test smells in test code, and to collect coverage metrics. JNose test is an extension of the Test Smell Detector. Besides presenting the number of test smells detected by class, our tool shows the collection of code metrics and test coverage using the JaCoCo library; a unified result for all projects under analysis; and a graphical interface. In addition, the project uses the Apache Maven to manage all library dependencies and support the compilation and execution of the JNose Test tool.

___

<a target="_blank" href="http://jnose.herokuapp.com/">
  Demo Jnose Heroku
</a>

---

## CBSoft 2020
<img src="https://github.com/tassiovirginio/jnose/blob/master/docs/premio.jpeg?raw=true">

## Videos
[![JNose Test](https://img.youtube.com/vi/6qrglBetOSc/0.jpg)](https://www.youtube.com/watch?v=6qrglBetOSc)

[![JNose Test](https://img.youtube.com/vi/BfYtwqQeqHc/0.jpg)](https://www.youtube.com/watch?v=BfYtwqQeqHc)


___
OBS: 
<a target="_blank" href="https://github.com/arieslab/jnose">
  Dependence on Project (JNose-Core)
</a>

It is necessary to install the "jnose-core" dependency for JNose to work. Below is the step by step to install, before installing Jnose.

```shell
git clone https://github.com/arieslab/jnose-core
cd jnose-core
mvn install
```


## Tutorials
 - <a href="TUTORIAL_pt-br.md">Tutorial PT-BR</a>
 - <a href="TUTORIAL_eng.md">Tutorial English</a>

## Papers

- JNose: Java Test Smell Detector
Tássio Virgínio, Luana Almeida Martins, Larissa Rocha Soares, Railana Santana, Adriana Priscila Santos Cruz, Heitor Costa, Ivan Machado (2020): http://cbsoft2020.imd.ufrn.br/artigos.php?evento=sbes-ferramentas

- An Empirical Study of Automatically-Generated Tests from the Perspective of Test Smells
Tássio Virgínio, Luana Martins, Larissa Soares, Railana Santana, Heitor Costa, Ivan Machado (2020): http://cbsoft2020.imd.ufrn.br/artigos.php?evento=sbes-pesquisa

 - Used to detect TestSmells and Coverage in the article (2019):
https://dl.acm.org/citation.cfm?doid=3350768.3350775

___

<table>
<tr>
<td>
<img src="http://cbsoft2019.ufba.br/assets/images/logo.png" width="400">
</td>
<td>
<img src="https://github.com/tassiovirginio/jnose/blob/master/src/main/webapp/cbsoft.jpeg?raw=true" width="400">
</td>
</tr>
<tr>
<td colspan="2">
Apresentação no CBSoft 2019 - Salvador - Bahia - Brazil<br>
  <a href="http://cbsoft2019.ufba.br">http://cbsoft2019.ufba.br</a>
</td>
</tr>
</table>


## Feature requests

Please, feel very welcome to create new issues on this project to request new features and report bugs. 

## Contributors
 - <a target="_blank" href="https://github.com/tassiovirginio">Tássio Virgínio</a>
 - <a target="_blank" href="https://github.com/danielevalverde">Daniele Valverde</a>
 - <a target="_blank" href="https://github.com/luana-martins">Luana Martins</a>
 - <a target="_blank" href="https://github.com/Railana">Railana Santana</a>
 - <a target="_blank" href="https://github.com/jonathanbisp">Jonathan Bispo</a>
 
## Contributing

- Create an issue on this repository
- Fork this repository
- create a branch and link the name to the related issue
- git commit -m 'description about what this commit does'
- git push origin your-branch-name
- Open a Pull Request

### Contact email:
- tassiovirginio@gmail.com

# Docker

```shell
docker build -t jnose .
docker run -dp "8080:8080" -v "$HOME/.m2":/root/.m2 --name jnose jnose:latest
docker logs -f jnose # para ver os logs, caso queira
```
# Dockerhub

https://hub.docker.com/r/tassiovirginio/jnose

```shell
docker pull tassiovirginio/jnose
```

