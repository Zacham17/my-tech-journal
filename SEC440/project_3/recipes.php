<?php

//Set the vars used for your DB connection, using new acct creds
  $username="zachary";
  $password='*********';
  $database='zach_db';
  $host='10.0.6.10';
//Acquire the recipe's name from your html POST
  $name=$_POST['name'];
//Establish MySQL connection called $mysqli
  $mysqli=new mysqli($host,$username,$password,$database);

//Define your query - pay close attention to ' and "!
  $query="SELECT * from recipes where name='".$name."'";
//Run query - result is reurned as a resource id
//If query has error, _LINE_ will print the error from mysql
  $result=$mysqli->query($query) or die($mysqli->error.__LINE__);

//Resource id results must be iterpreted
//This while loop will run thru the results row by row & echo name & birth fields
if ($result->num_rows > 0) {
  while($row=$result->fetch_assoc()) {
  echo $row['name']." is a ".$row['type']."</br>";
  echo " This item takes ".$row['makeTime']." minutes to make </br>";
  echo $row['owner']." added this recipe </br>";
  echo "This recipe was added on ".$row['addedDate']."</br>";
  }
  }
  else {
  echo 'NO RESULTS';
  }
?>
