<html>
<head>
    <title>
        Vulcan's webserver
    </title>
</head>
<body>
<center>
<?php echo "<h2>Welcome to vulcan's webserver</h2>";
?>
<?php
date_default_timezone_set("America/New_York");
?>
</center>
<form action="/images">
    <input type="submit" value="Open directory to images" style="position: absolute; z-index: 3; left: 1300px; top:   150px">
</form>
<center>
<form action="ListOfCommands.txt">
    <input type="submit" value="Open List Of Commands" style="position: absolute; z-index: 3; left: 1300px; top:   250px">
</form>
<center>
<form action="myprocessingscript.php" method="POST">
    Type Command: <input name="field1" type="text" />
    <input type="submit" name="submit" value="Send Command">
<center>
    
</center>
</form>

<img src="<?php echo "/Vulcan.jpg";?>">
<?php
if (file_exists('images/PhotoCommand.jpeg')){
    echo "<p align='left'> <font color=red  size='4pt'>Command Recieved, please goto your image directory </font> </p>";
} else {
    echo "";
}
?>
 

</body>
</html>