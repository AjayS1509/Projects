<?php
$con = mysqli_connect('localhost','root','Ajay@1509');

if($con){
  echo "Connection Succesfully!";
}else{
  echo "Connected Not Sucessfully!";
}
mysqli_select_db($con,'blog');
$user = $_POST['user'];
$email = $_POST['email'];
$mobile = $_POST['mobile'];
$comment = $_POST['comment'];

$query = "insert into userinfodata (user,email,mobile,comment) values('$user','$email','$mobile','$comment') ";
echo "$query";
mysqli_query($con,$query);

 ?>
