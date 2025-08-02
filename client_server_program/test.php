<?php 
    $_POST = json_decode(file_get_contents('php://input'), true);
    $arr = [];
    
    require __DIR__ . '/validatation.php';
    
    foreach($_POST as $X => $X_val){
        if (!validateInfo($X, $X_val)){
            echo $X . " is invalid: " . $X_val;
            header($X . " is invalid", true, 400);
            exit();
        }
    }

    $arr[sizeof($arr)] = $_POST;
    header("Content-Type: application/json");
    echo json_encode($arr[sizeof($arr) - 1]);
?>