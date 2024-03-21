--  lists all bands with Glam rock as their main style, ranked by their longevity
SELECT band_name, (2022 - split - formed) AS lifespan
FROM bands
WHERE main_style = 'Glam rock'
ORDER BY lifespan DESC;
