-- 1 Mostrar la Carta inicial más repetida por cada jugador. (mostrar nombre jugador y carta)
SELECT p.player_name, r.initial_card_id FROM player p
INNER JOIN player p ON p.player_id
INNER JOIN rounds r ON r.player_id=p.player_id
GROUP BY player_name;

-- 2 Jugador que realiza la apuesta más alta por partida. (Mostrar nombre jugador)
SELECT player_name,MAX(bet),cardgame_id
FROM
(
SELECT
CASE
WHEN player_name IS NOT NULL THEN player.username
END
AS player_name,MAX(rounds.bet) AS bet,cardgame.cardgame_id AS cardgame_id FROM player
LEFT JOIN bot ON bot.idbot=player.idbot
LEFT JOIN player ON player.player_id=player.player_id
INNER JOIN player ON player.player_id=player.player_id
INNER JOIN rounds ON player.player_id=rounds.player_id
INNER JOIN game ON rounds.cardgame_id=game.cardgame_id
WHERE rounds.bet IS NOT NULL
GROUP BY game.game_id,player_name
) tabla
WHERE (bet,cardgame_id) IN
(
SELECT
MAX(rounds.bet),game.cardgame_id  AS bet from player
LEFT JOIN bot ON bot.idbot=player.idbot
LEFT JOIN player ON player.player_id=player.player_id
INNER JOIN player ON player.player_id=player.player_id
INNER JOIN rounds ON player.player_id=rounds.player_id
INNER JOIN game ON rounds.cardgame_id=game.cardgame_id
GROUP BY game.game_id
ORDER BY MAX(rounds.bet) DESC
)
GROUP BY cardgame_id limit 5;

-- 3 Jugador que realiza apuesta más baja por partida. (Mostrar nombre jugador)
SELECT player_name,MIN(bet),cardgame_id
FROM
(
SELECT
CASE
WHEN player_name IS NOT NULL THEN player.username
END
AS player_name,MIN(rounds.bet) AS bet,cardgame.cardgame_id AS cardgame_id FROM player
LEFT JOIN bot ON bot.idbot=player.idbot
LEFT JOIN player ON player.player_id=player.player_id
INNER JOIN player ON player.player_id=player.player_id
INNER JOIN rounds ON player.player_id=rounds.player_id
INNER JOIN game ON rounds.cardgame_id=game.cardgame_id
WHERE rounds.bet IS NOT NULL
GROUP BY game.game_id,player_name
) tabla
WHERE (bet,cardgame_id) IN
(
SELECT
MIN(rounds.bet),game.cardgame_id  AS bet from player
LEFT JOIN bot ON bot.idbot=player.idbot
LEFT JOIN player ON player.player_id=player.player_id
INNER JOIN player ON player.player_id=player.player_id
INNER JOIN rounds ON player.player_id=rounds.player_id
INNER JOIN game ON rounds.cardgame_id=game.cardgame_id
GROUP BY game.game_id
ORDER BY MIN(rounds.bet) DESC
)
GROUP BY cardgame_id limit 5;

-- 4 Porcentaje de rondas ganadas por jugador en cada partida(%), así como su apuesta media de la partida.

-- 5 Lista de partidas ganadas por Bots.

-- 6 Cuantas rondas gana la banca en cada partida, PUEDE QUE NO GANE NINGUNA y también se ha de mostrar.
SELECT round_num, cardgame_id FROM rounds
WHERE result = 'gana el turno' and is_bank = 1
GROUP BY cardgame_id;

-- 7 Cuántos usuarios han sido la banca en cada partida.
SELECT COUNT(is_bank), cardgame_id FROM rounds
WHERE is_bank = 1
GROUP BY cardgame_id;

-- 8 Calcular la apuesta media por partida.
SELECT AVG(bet), cardgame_id FROM rounds
GROUP BY cardgame_id;


-- 9 Calcular la apuesta media de la primera ronda de cada partida.
SELECT AVG(bet), cardgame_id FROM rounds
WHERE rounds = 1
GROUP BY cardgame_id;

-- 10 Calcular la apuesta media de la última ronda de cada partida.

