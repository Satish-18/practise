/*find 5 oldest user*/
SELECT * FROM  USERS order by created_at limit 5;

/*What day of the  week do  most of the user register*/
SELECT username,DAYNAME(created_at) as 'day_name', count(*) as total FROM  USERS group by day_name order by total desc limit 2;

/*find the user who never post a photo(user with no photo)*/
select username,image_url from users left join photos on users.id=photos.user_id where photos.id is null;

/*find the most liked photoes in the database and user who created it*/
SELECT 
    username,
    photos.id,
    photos.image_url, 
    COUNT(*) AS total
FROM photos
INNER JOIN likes
    ON likes.photo_id = photos.id
INNER JOIN users
    ON photos.user_id = users.id
GROUP BY photos.id
ORDER BY total DESC
LIMIT 1;

/*how many times the average user post  photo(average photo per user)*/
SELECT (SELECT Count(*) 
        FROM   photos) / (SELECT Count(*) 
                          FROM   users) AS avg; 
                          
/*find 5 most commmonly used hastags */
SELECT tags.tag_name, 
       Count(*) AS total 
FROM   photo_tags 
       JOIN tags 
         ON photo_tags.tag_id = tags.id 
GROUP  BY tags.id 
ORDER  BY total DESC 
LIMIT  5;  

/*find a user who has liked every single photo on the site*/
SELECT username, 
       Count(*) AS num_likes 
FROM   users 
       INNER JOIN likes 
               ON users.id = likes.user_id 
GROUP  BY likes.user_id 
HAVING num_likes = (SELECT Count(*) 
                    FROM   photos); 