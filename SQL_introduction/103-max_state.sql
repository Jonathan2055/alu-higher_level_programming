-- displays the top 3 of cities temperature during July and August ordered by temperature --
SELECT `state`, MAX(`value`) AS `max_temp` FROM `temperatures` GROUP BY `state` ORDER BY `state`;
