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

Este relatório em formato de README.md está disposto em seções que demonstram a maneira (metodologia) como será implementada a solução, qual o formato (arquitetura) decidido para a solução, e de que forma esta poderá ser aperfeiçoada em termos de software e processo.

Doravante, a solução aqui proposta será denominada **_desafio1_**. 

## 2. Metodologia

### 2.1 Dados

Conforme supracitado, as bases selecionadas para o projeto de aquisição/estruturação de dados serão sites de notícias brasileiros sobre automóveis, dentre os 5 mais populares.  

* [iCarros](https://www.icarros.com.br/noticias/arquivo.jsp)

* [Quatro Rodas](https://quatrorodas.abril.com.br/noticias/)

* [Carros iG](https://carros.ig.com.br/noticias/)

* [UOL Carros](https://www.uol.com.br/carros/ultimas/)

* [Jornal do Carro](https://jornaldocarro.estadao.com.br/carros/noticias/)

Os dados mínimos a serem coletados de cada notícia de cada portal serão: **título** (_string_), **corpo do texto** (_string_), **autor** (_string_), **data** (_timestamp_), **url** (_string_), e **tags** (_string_).

Outros dados, quando disponíveis, serão capturados para composição de métricas de metacaracterísticas (palavras por artigo) e de engajamento (_likes_ ou número de compartilhamentos).

Todos os dados coletados serão dispostos em armazenamento persistente, ou seja, banco de dados para subseqüentes análises dos artigos.

Por fim, deseja-se guardar os metadados das aquisições, para posteriores manutenções da base de dados.

### 2.2 Ferramentas de software

Para que seja facilitado os posteriores deploy e migração para serviços de nuvem, foi decidido que a solução de _web crawling/scraping_ **desafio1** deve ser implementada sobre serviço de contêiner em plataforma Linux. Assim, o pacote [**_Docker_**](https://www.docker.com/) será adotada, devido a sua ampla participação e maturidade em ambientes de nuvem e por sua integração a boas práticas de _DevOps_.

A solução _desafio1_ será implementada na linguagem de programação [**_Python_**](https://www.python.org/), versão 3.7.3, complementada com os pacotes **_Scrapy_** e **_phoenixdb_**, a serem integrados nas images dos conteineres de aplicação.

O _framework_ [**_Scrapy_**](https://scrapy.org/) é uma das alternativas mais populares para _web crawling/scraping_ disponíveis para a comunidade Python, mas também razão de muitos projetos transferirem sua tecnologia para essa linguagem, devido a sua facilidade e sua riqueza de funcionalidades.

Já o pacote [**_phoenixdb_**](https://phoenix.apache.org/python.html) foi escolhido por ser o driver nativo de acesso, pela linguagem _Python_, ao _Apache Phoenix_, apresentado em seqüência.

Pela quantidade massiva de dados que o _web crawling/scraping_ é designado para coletar, deve ser determinada uma solução de persistência de armazenamento de dados que tenha boa escalabilidade, acesso _real-time_ e distribuído, flexibilidade de estrutura tipo _NoSQL_ e maturidade de mercado, bem como boa integrabilidade com os serviços de nuvem mais populares. Assim, elegeu-se o [**_Apache HBase_**](https://hbase.apache.org/), parte do ecossistema _Apache Hadoop_, como a ferramenta de banco de dados para este projeto. 

Por outro lado, o HBase pode não ter a interface de consulta mais amigável para desenvolvedores habituados ao mundo relacional --- ou mesmo a outras plataformas _NoSQL_---, sobretudo por prover poucas operações do tipo _CRUD_ e por restringir seu tipo de dados apenas a _arrays_ de _bytes_. Assim, foi desenvolvida a solução [**_Apache Phoenix_**](https://phoenix.apache.org/), cujo objetivo é servir de _query engine_ relacional (via SQL), ou camada relacional, para as chamadas nativas ao HBase, além de paralelizar o acesso ao banco. Portanto, o _Apache Phoenix_ foi eleito como camada de acesso ao HBase para este projeto.

As versões utilizadas para todo software mencionado aqui serão as mais recentes.

As ferramentas para análise dos dados recolhidos serão definidas _a posteriori_, recorrendo-se, no momento, a consultas individuais ao banco via Phoenix.  

## 3. Proposta de solução

### 3.1 Arquitetura

De forma "macro", observa-se que os artigos de portais sobre automóveis não costumam ter alta freqüência de postagem. De fato, pode-se dizer que são lançamento de notícias sazonalmente, com pico nos último trimestre do ano, quando são divulgados novos lançamentos no mercado para o ano seguinte e as avaliações do tipo "melhor do ano". Logo, é seguro recorrer à estratégia do **processamento _batch_** da aquisição dos dados desses portais.

Além disso, para melhor integração e modularização da solução _desafio1_, bem como melhor adequação às boas práticas do _Scrapy_, estabeleceu-se que cada _spider_ (_crawler_) para cada portal ficaria em contêiner separado dos outros. Desta forma, serão criado 5 conteineres, 1 para cada portal. Sobre estas 5 imagens, serão instalados os pacotes _Scrapy_ e _phoenixdb_, e será copiada a estrutura de diretórios _/desafio1/src/desafio1crawlers_, igual para cada imagem, mas a ser acionada por _spiders_ diferentes cada uma, referente ao portal em questão. A imagem base será adquirida do [**_Docker Hub_**](https://hub.docker.com/), mais especificamente a imagem [**_python_**](https://hub.docker.com/_/python).

Por fim, será criada uma imagem única para o HBase e o Phoenix, a partir daquela disponível no _Docker Hub **[harisekhon/hbase](https://hub.docker.com/r/harisekhon/hbase)**_.

A figura abaixo ilustra, de forma esquemática, a arquitetura:

![Arquitetura de _desafio1_](/images/arquitetura.png)

#### 3.1.1 Estrutura de dados

Metadados

Métricas de engajamento

### 3.2 _Build_

Dockerfiles

### 3.3 Monitoramento

### 3.4 Desempenho

### 3.5 Estratégia de _deploy_

## 4. Conclusões e melhorias futuras

* Apache Gora

* Apache Spark

* Apache Nutch

* PySpark (Python) 

## Referências
<a name="ref1">1</a>: https://www.skylynapps.com/scrapemate/learn/help/general/difference-between-crawler-and-scraper.php

## Apêndice - Worklog
Data de início | Atividade | Duração
------------- | ------------- | -----
13/11/2019 | Análise e entendimento do desafio proposto | 1:00
13/11/2019 | Criação do repositório _desafio1_ no GitHub | 0:10
17/11/2019 | Revisão das melhores ferramentas para _web crawling/scraping_ | 4:00
17/11/2019 | Atualização sobre funcionalidades do _Scrapy_ | 1:00
18/11/2019 | Revisão sobre funcionalidades do Apache HBase e Apache Phoenix | 2:00
18/11/2019 | Documentação do projeto, arquitetura e módulos (início) | 2:00
19/11/2019 | Criação do projeto no _Scrapy_ denominado _desafio1crawlers_ | 0:10
18/11/2019 | Revisão sobre arquiteturas possíveis para projeto | 4:00
19/11/2019 | Documentação do projeto, arquitetura e módulos (continuação) | 2:00
20/11/2019 | Documentação do projeto, arquitetura e módulos (continuação) | 3:00