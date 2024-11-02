
## Desafio #### 06) Crie um crawler (aplicação de busca de informação na web) que leia as 3 primeiras notícias do site g1.globo.com e organize em um JSON contendo o título, subtitulo (se tiver) e url da imagem de destaque (se tiver).   
A proposta foi feita em Python com [Scrappy](https://scrapy.org/)     
    
Requisitos:    
 - Python    
     
A saída das noticias é feita no próprio terminal como no exemplo abaixo:  
   

    2019-11-28 14:07:58 [scrapy.core.scraper] DEBUG: Scraped from <200 https://g1.globo.com/>
    {'Título': 'MPF questiona se caso dos brigadistas presos no Pará cabe à Justiça Estadual', 'Subtitulo': 'Advogados pede libertação dos \nbrigadistas detidos', 'Url Imagem': None}
    2019-11-28 14:07:58 [scrapy.core.scraper] DEBUG: Scraped from <200 https://g1.globo.com/>
    {'Título': 'STF retoma logo mais julgamento sobre dados fiscais sigilosos ', 'Subtitulo': 'Tribunal já tem maioria a favor de compartilhar informações com o MP.', 'Url Imagem': 'h
    ttps://s2.glbimg.com/RfAIp5py5xANntwvOC9biuTfJpE=/0x0:2000x1344/540x304/smart/http://s2.glbimg.com/vu3XbBjFLoj65s5pMS-4YgdQv1E=/0x0:2000x1344/2000x1344/s.glbimg.com/jo/g1/f/origin
    al/2019/11/27/stf_Lm2iWeh.jpg'}
    2019-11-28 14:07:58 [scrapy.core.scraper] DEBUG: Scraped from <200 https://g1.globo.com/>
    {'Título': 'EDITORIAL: As barreiras institucionais contra o autoritarismo', 'Subtitulo': 'Apesar da solidez das instituições, acenos ao AI-5 e avanços sobre leis têm de ser critic
    ados com vigor.', 'Url Imagem': None}
    2019-11-28 14:07:58 [scrapy.core.engine] INFO: Closing spider (finished)

  
> Um [ambiente virtual de python](https://docs.python.org/3/library/venv.html) é recomendado, porem não é obrigatório para os passos abaixo.  
> <br> Lembre-se de estar na pasta /crawler/ ao executar os comandos abaixo:  
 1. `pip install -r requirements.txt` para instalar as dependências   
 2. `scrapy runspider crawler.py` para executar o servidor na porta :8000  
  
