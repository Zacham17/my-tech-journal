<?php
// Set the vars used for your DB connection, using new account credentials
$username = "zachary";
$password = '********';
$database = 'zach_db';
$host = '10.0.6.10';

// Acquire the recipe's data from your HTML POST
$name = $_POST['name'];
$type = $_POST['type'];
$owner = $_POST['owner'];
$makeTime = $_POST['makeTime'];

// Establish MySQL connection called $conn
$conn = new mysqli($host, $username, $password, $database);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Prepare the SQL statement with placeholders
$sql = $conn->prepare("INSERT INTO recipes (name, type, owner, makeTime, addedDate) VALUES (?, ?, ?, ?, ?)");

// Bind the parameters to the statement
$sql->bind_param("sssss", $name, $type, $owner, $makeTime, $addedDate);

// Get the current date in 'Y-m-d' format
$addedDate = date("Y-m-d");

// Execute the prepared statement
if ($sql->execute()) {
    echo "New record created successfully";
} else {
    echo "Error: " . $sql->error;
}

// Close the statement and database connection
$sql->close();
$conn->close();
?>
