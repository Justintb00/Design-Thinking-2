<?php
date_default_timezone_set("America/New_York");
?>
<?php
if(isset($_POST['field1'])) {
    $data = $_POST['field1'];
    $date = date("m/d/Y ") . date("h:i:sa: ");
    $CommandList = fopen("ListOfCommands.txt","a") or die("Unable to open file!!");
    $ret = file_put_contents('Command.txt', $data, LOCK_EX);
    
    if($ret === false) {
        die('There was an error writing this file');
    }
    else {
        fwrite($CommandList, $date);
        fwrite($CommandList, $data);
        fwrite($CommandList, "\n");
        fclose($CommandList);
        echo "$ret bytes written to file";
    }
}
else {
   die('no post data to process');
}
?>
<form action='/'>
    <input type="submit" value="Go back to main webpage" style="position: absolute; z-index: 3; left: 1300px; top:   150px">
</form>
