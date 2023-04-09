SELECT * FROM TBL_MONITORS WHERE QUALIFICATION = '5';


SELECT * FROM TBL_USERS;


INSERT INTO tbl_users (name, lastname, username, password)
VALUES ('Justyn', 'Meza', 'ADMIN', 'admin');

SELECT USERNAME, PASSWORD FROM TBL_USERS WHERE USERNAME = 'ADMIN' and PASSWORD = 'admin';

/*marca mas vendida*/
SELECT brand, COUNT(*) as count
FROM tbl_monitors
GROUP BY brand
ORDER BY count DESC
LIMIT 1;

/*calificacion mas alta*/
SELECT MAX(qualification) as max_qualification
FROM tbl_monitors;

/*total de registros*/
SELECT COUNT(*) as total_records
FROM tbl_monitors;

/*valor total de todos los precios*/
SELECT SUM(price) as total_price
FROM tbl_monitors;

/*GRAFICAS*/

/*todas las marcas*/
SELECT DISTINCT brand
FROM tbl_monitors
ORDER BY brand ASC;

/*cantidad vendida por cada marca*/
SELECT brand, COUNT(*) as count
FROM tbl_monitors
GROUP BY brand;

/*3 marcas mas vendidas*/
SELECT brand, COUNT(*) as count
FROM tbl_monitors
GROUP BY brand
ORDER BY count DESC
LIMIT 3;

/*los precios de cada una de las 3 marcas mas vendidas*/
SELECT m.brand, GROUP_CONCAT(m.price ORDER BY m.price ASC SEPARATOR ', ') AS prices
FROM tbl_monitors m
INNER JOIN (
    SELECT brand, COUNT(*) AS count
    FROM tbl_monitors
    GROUP BY brand
    ORDER BY count DESC
    LIMIT 3
) b ON m.brand = b.brand
GROUP BY m.brand;

/*precio x pulgada*/
SELECT size_screen, GROUP_CONCAT(price SEPARATOR ', ') AS prices
FROM tbl_monitors
GROUP BY size_screen
ORDER BY size_screen;


/*tasas de refresco*/
SELECT update_rate, COUNT(*) AS cantidad
FROM tbl_monitors
GROUP BY update_rate;


