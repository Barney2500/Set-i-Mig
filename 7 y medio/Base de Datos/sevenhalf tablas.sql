DROP DATABASE IF EXISTS sevenhalf;
CREATE DATABASE sevenhalf CHARACTER SET utf8mb4;
USE sevenhalf;

CREATE TABLE player (
  player_id VARCHAR(25) PRIMARY KEY,
  player_name VARCHAR(40),
  player_risk TINYINT,
  human TINYINT(1)
  );
  
CREATE TABLE cardgame (
  cardgame_id INT PRIMARY KEY,
  players TINYINT,
  rounds TINYINT,
  start_hour DATETIME,
  end_hour DATETIME,
  deck_id CHAR(3)
  );
  
  CREATE TABLE player_game (
  cardgame_id INT,
  player_id VARCHAR(25),
  initial_card_id CHAR(3),
  starting_points TINYINT,
  ending_points TINYINT(1)
  );
  
  CREATE TABLE player_game_round (
  cardgame_id INT,
  round_num TINYINT PRIMARY KEY,
  player_id VARCHAR(25),
  is_bank TINYINT(1),
  bet_points TINYINT,
  cards_value DECIMAL(4,1),
  starting_round_points TINYINT,
  ending_round_points TINYINT(1)
  );
  
  CREATE TABLE deck (
  deck_id CHAR PRIMARY KEY,
  deck_name VARCHAR(25)
  );
  
  CREATE TABLE card (
  card_id CHAR(3) PRIMARY KEY,
  card_name VARCHAR(25),
  card_value DECIMAL(3,1),
  card_priority TINYINT,
  card_real_value TINYINT,
  deck_id CHAR(3)
  );