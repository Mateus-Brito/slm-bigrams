# Análise de Frequência de Bigrams

Este projeto realiza a análise de frequência de bigramas em um conjunto de dados textuais, permitindo observar as combinações mais comuns de palavras. O código foi adaptado de um tutorial disponível no seguinte vídeo: [Tutorial NLTK - Bigramas](https://www.youtube.com/watch?v=OaLemi9JIl8) e usa textos gerados a partir do site [Lero Lero](https://lerolero.bgnweb.com.br/).

## Visão Geral do Projeto

No projeto, os arquivos de texto são armazenados na pasta "data". O código carrega esses arquivos, realiza a limpeza dos dados e extrai bigramas, permitindo a análise estatística da estrutura e uso de palavras. Além disso, o projeto gera sentenças com base nos bigramas mais frequentes, oferecendo uma compreensão prática de como as palavras se conectam em diferentes contextos.

## Funcionalidade do Código

O código executa as seguintes etapas:

1. **Download de Dados Necessários**: Faz o download dos recursos necessários da biblioteca NLTK.
2. **Carregamento e Limpeza de Dados**: Carrega os dados textuais da pasta "data",remove pontuações e ignora linhas vazias.
3. **Extração de Bigrams**: Tokeniza o texto e gera bigramas.
4. **Cálculo da Distribuição de Frequência**: Calcula a distribuição de frequência dos bigramas extraídos.
5. **Filtragem de Bigrams**: Obtém os top K bigramas para cada palavra inicial, permitindo análises mais significativas.
6. **Geração de Sentenças**: Utiliza os bigramas filtrados para gerar sentenças começando com uma palavra específica.

## Exemplo de Saída

O código gera saídas como as apresentadas abaixo, onde frases são geradas com base na frequência dos bigramas:

```
======= Examples =======
incentivo ao avanço tecnológico assim mesmo modo a longo prazo . o significado destes problemas 
incentivo ao estabelecimento dos pontos do remanejamento dos quadros funcionais envolvidos . o significado destes 
incentivo ao avanço tecnológico assim como um todo . é importante questionar o que o 
```

## Executar o Código

Para executar o código, execute o comando abaixo:

```bash
make run
```

## Conclusão

Este projeto fornece uma abordagem poderosa para análise de textos usando bigramas, permitindo uma exploração mais profunda da estrutura linguística dos dados analisados.
