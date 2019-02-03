# Projet5 - Welcome to Pure Beurre!

This is the fifth project of the OpenClassrooms' python developper trainee.
It consists of returning a better substitute with a better nutrition grade to a product from a choosen category.

This program interact with the french [OpenFoodFacts](https://fr.openfoodfacts.org) API.

## Installation

First, you should install _[MySql](https://www.mysql.com)_ that is a DBMS (*DataBase Management System*) and create a user and a database. checkout the documentation to see how to do this.

Then create three environment variables:

```bash
$ export DB_NAME='your_database_name'
$ export DB_USER='your_database_user_username'
$ export DB_PASSWORD='your_database_user_password'
```

Now you can run the database.py script to create the tables and populate the database. note that you just have to run this script once at the first time you install the program.

## Example

To launch the program make sure you in the right directory and run the program.py

```bash
$ python program.py
```

You'll be prompted with the following in the CLI:

```
Welcome to Pure_Beurre!
-----------------------
What do you want to do?

  1. Find a substitute.
  2. Review substitutes.
```
If you choose the first option for example it provides you with a sample of 5 categories of product as what follow:

```
Select a category:

1 Produits laitiers
2 Plats préparés
3 Boissons sans alcool
4 Aliments à base de fruits et de légumes
5 Viandes
```

Choose a category entering the corresponding number, let's say 1 :

```
Select a product:

1 Lait Bio Demi-Écrémé
2 J'aime le lait d'ici
3 Chavroux Pur Chèvre
4 Danette noir extra
5 Kiri à la crème de lait (8 Portions)
6 Le Yaourt à la Grecque, Nature
7 Lait Demi écrémé
8 Philadelphia
9 Emmental Français
10 Lait Demi-écrémé avec Vitamine D
11 Camembert (20 % MG)
12 Camembert Auguste Lepetit & fils (21 % MG)
13 Velouté Nature
14 Activa (Nature) 12 Pots
15 Le Beurre Moulé Demi-Sel (80 % MG)
16 Yaourt Nature
17 Comté AOP au lait cru 34%MG
18 Kiri à la crème de lait
19 Parmigiano Reggiano râpé frais
20 Le Beurre léger 41% MG Demi-écrémé Doux
21 Le Fromage Fouetté Madame Loïk, Nature au sel de Guérande (24 % MG)
22 Lait GrandLait demi-écrémé
23 La Vache qui rit® 32 Portions (19 % MG)
24 La Faisselle
25 Framboise Délicate
26 Apéricube Tonic
27 Beurre président gastronomique demi sel
28 Lait viva
29 Le Beurre Moulé Doux (82 % MG)
30 Perle de Lait (Nature) 8 Pots
31 Creme Saint Agur 25%
```

let's now enter the number of the product we want a substitute of and the program returns:

```
Select a Substitute:

1 Yaourt Nature | A
2 Lait Bio Demi-Écrémé | B
3 J'aime le lait d'ici | B
```
 
 now you can choose on of them and decide to record it to database:

 ```
Substitue details:

name :  Yaourt Nature
nutriscore :  a
stores :  Auchan

Record to database? (Y/N)
```

## Author



