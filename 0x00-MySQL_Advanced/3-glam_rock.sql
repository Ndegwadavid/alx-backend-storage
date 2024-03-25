--  lists all bands with Glam rock as their main style, ranked by their longevity
<<<<<<< HEAD
SELECT band_name, (2022 - split - formed) AS lifespan
FROM bands
WHERE main_style = 'Glam rock'
=======
SELECT band_name AS band_name, IFNULL(split, 2020) - IFNULL(formed, 0) AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
>>>>>>> 2514f448f4a044fe2bc90d9608aad608d5652f4b
ORDER BY lifespan DESC;
