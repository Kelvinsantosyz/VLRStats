

# VLR Stats

Este é um projeto que utiliza a biblioteca [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) para realizar scraping de dados de partidas do jogo [Valorant](https://playvalorant.com/pt-br/).

Com esse projeto, é possível obter estatísticas de jogadores e equipes, além de resultados de partidas e mapas jogados.

## Pré-requisitos

Antes de começar, é necessário ter o Python 3 instalado na sua máquina.

## Instalação

1. Clone o repositório para o seu computador.
2. Instale as dependências do projeto utilizando o comando `pip install -r requirements.txt`.

## Utilização

Para utilizar o projeto, siga os seguintes passos:

1. Execute o arquivo `main.py`.
2. Insira a URL da partida que deseja analisar. Exemplo: `https://www.vlr.gg/197245/rebels-velvet-vs-cba-game-changers-2023-series-i-emea-groups-r7`.
3. Escolha qual tipo de análise deseja realizar:

- Informações da equipe e elenco: `Get_team_stats(url)`
  - `current_rank()` - classificação atual da equipe

- Mapas jogados e agentes de partida: `TeamStats(url)`

- Estatísticas gerais da partida: `MatchAnalyzer(url)`
  - `players()` - lista dos jogadores da equipe
  - `agents()` - taxa de vitórias por agente utilizado
  - `rating_all()` - rating geral da equipe em todas as partidas
  - `rating_all_ct()` - rating geral da equipe jogando como CT
  - `rating_all_tr()` - rating geral da equipe jogando como TR
  - `acs_all()` - ACS (Average Combat Score) geral da equipe em todas as partidas
  - `acs_all_ct()` - ACS geral da equipe jogando como CT
  - `acs_all_tr()` - ACS geral da equipe jogando como TR
  - `kda_all()` - KDA (Kill/Death/Assist) geral da equipe em todas as partidas
  - `kda_all_ct()` - KDA geral da equipe jogando como CT
  - `kda_all_tr()` - KDA geral da equipe jogando como TR
  - `fk_fd_all()` - First Kills/First Deaths geral da equipe em todas as partidas
  - `fk_fd_ct_all()` - First Kills/First Deaths geral da equipe jogando como CT
  - `fk_fd_tr_all()` - First Kills/First Deaths geral da equipe jogando como TR

- Estatísticas do primeiro mapa: `MatchAnalyzer_map1(url)`
  - `result_map1()` - resultado do primeiro mapa

- Estatísticas do segundo mapa: `MatchAnalyzer_map2(url)`
  - `result_map2()` - resultado do segundo mapa

- Estatísticas do terceiro mapa: `MatchAnalyzer_map3(url)`
  - `result_map3()` - resultado do terceiro mapa (caso tenha sido jogado)



