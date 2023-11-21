/*PRINT each shows with ratings*/
select title,rating from series join reviews on series.id=reviews.series_id;

/*PRINT average ratings of all shows*/
select title ,avg(rating) as avg_rating from series join reviews on series.id=reviews.series_id
	group by title order by avg_rating asc;
    
/*PRINT name of reviewers with corresponding rating*/
select first_name, last_name,rating from reviewers join reviews on reviewers.id=reviews.reviewer_id;

/*PRINT UNREVIEWEED SERIES*/
select title,rating from series left join reviews on series.id=reviews.series_id where rating is null;


/*PRINT GENRE AND ITS CORRESPONDING RATINGS*/
select genre,
round(
avg(rating),2 )
as avg_ratings from series  inner join reviews on series.id=reviews.series_id group by genre;


/*PRINT MAKER FIRST AND LAST NAME AND COUNT THE
 NO OF RATING ,MIN ,MAX AND AVERAGE RATING AND IF RATED SHOW ACTIVE ELSE INAACTIVE*/
 select first_name, last_name,count(rating),
 ifnull(min(rating),0) as 'min',ifnull(max(rating),0) as 'max',
	round(ifnull(avg(rating),0),2) as 'avg',
    /*if works for only two cases */
    if (count(rating)>=1, 'active','inactive')
     as status
	from reviewers left join reviews on reviewers.id=reviews.reviewer_id
	group by reviewers.id;
    
/*using case statement*/
SELECT first_name, 
       last_name, 
       Count(rating)                    AS COUNT, 
       Ifnull(Min(rating), 0)           AS MIN, 
       Ifnull(Max(rating), 0)           AS MAX, 
       Round(Ifnull(Avg(rating), 0), 2) AS AVG, 
       CASE 
         WHEN Count(rating) >= 10 THEN 'POWER USER' 
         WHEN Count(rating) > 0 THEN 'ACTIVE' 
         ELSE 'INACTIVE' 
       end                              AS STATUS 
FROM   reviewers 
       LEFT JOIN reviews 
              ON reviewers.id = reviews.reviewer_id 
GROUP  BY reviewers.id; 

/*putting all three table with corresponding title,rating & reviewer*/
select title,rating,concat(first_name, 
       last_name) as 'name' from reviewers
		inner join reviews on reviewers.id = reviews.reviewer_id 
		inner join series on series.id=reviews.series_id;