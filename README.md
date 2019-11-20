# desafio1
Desafio 1

## Sumário

## 0. Equipe

* <a href="mailto:elmon.noronha@gmail.com">Elmon Noronha</a>

## 1. Introdução

### 1.1 Apresentação do desafio e objetivos

O _web crawling_ (e também o _web scraping_) são ferramentas indispensáveis para a aquisição de grandes massas de dados de forma mais automatizada e flexível, sobretudo a partir de plataforma tão heterogênea e mutante quanto a _web_.

Há que se destacar as diferenças entre _web crawling_ e _scraping_, determinantes na escolha da metodologia/ferramentas para captura de dados, conforme discutido adiante.

O _web crawling_ resume-se a navegar entre páginas através da busca de links em cada uma analisada e, de certa forma, a **indexar** o conjunto de páginas por onde navegou. Já o _web scraping_ busca extrair dados das páginas individuais<sup>[1](#ref1)</sup>. Na prática, ambas as ferramentas costumam realizar a função uma da outra, mas pode ser necessário complementá-las.     

O objetivo principal deste projeto parte daí: o desafio consiste em, partindo de portais concorrentes de notícias sobre automóveis, adquirir dados e estruturar informações de notícias.

Os objetivos específicos do projeto são:

* adquirir e estruturar dados de notícias em portais sobre automóveis, utilizando _web crawlers_ e _scrapers_, além de solução de persistência de dados e de métricas das buscas;
* documentar o _worklog_ e processo de tomada de decisões sobre o projeto, bem como as informações colhidas e as métricas selecionadas de aquisição/estruturação dos dados;
* e apresentar alternativas para escalar a solução implementada e para análises que podem ser realizadas sobre dados/métricas.     

Este relatório em formato de README.md está disposto em seções que demonstram como (metodologia) será implementada a solução, qual o formato (arquitetura) decidido para a solução, e de que forma esta poderá ser aperfeiçoada em termos de software e processo. 

## 2. Metodologia

### 2.1 Dados
https://www.webmotors.com.br/
https://www.vrum.com.br/
http://www.icarros.com.br/‎
https://quatrorodas.abril.com.br/
https://carros.ig.com.br/
https://www.uol.com.br/carros/ultimas/
https://jornaldocarro.estadao.com.br/carros/
https://noticias.r7.com/carros/
https://motorshow.com.br/
https://revistacarro.com.br/


### 2.2 Ferramentas de software
Apache HBase
Apache Gora
Python
Scrapy
Docker

## 3. Proposta de solução
xxx

### 3.1 Arquitetura

Docker > Scrapy (Python) >  > HBase  

#### 3.1.1 Estrutura de dados

#### 3.1.2 Metadados

#### 3.1.3 Métricas de engajamento

### 3.2 _Build_

### 3.3 Monitoramento

### 3.4 Desempenho

### 3.5 Estratégia de _deploy_

## 4. Conclusões e melhorias futuras
zzz
Apache Gora
Apache Nutch
PySpark (Python)
Apache Spark
## Referências
<a name="ref1">1</a>: https://www.skylynapps.com/scrapemate/learn/help/general/difference-between-crawler-and-scraper.php

## Apêndice - Worklog
Data de início | Atividade | Duração
------------- | :-------------: | :-----:
xx/xx/xxxx | right-aligned | xx:xx
yy/yy/yyyy | centered      | yy:yy
zz/zz/yyyy | are neat      | zz:zz