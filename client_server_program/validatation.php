<?php 

function  validateInfo($match, $param){
    switch ($match) {
        case "username":
            $exp = "/^[a-zA-Z][a-zA-Z0-9]{5,}$/i";
            return preg_match($exp, $param);
        
        case "password":
            $exp1 = "/[ .,!@#$%^&*()-+\/:;\"'<>?]+/";
            $exp2 = "/\d+/";
            $exp3 = "/[a-z]+/";
            $exp4 = "/[A-Z]+/";
            if(strlen($param) < 8){
                return false;    
            }
            return preg_match($exp1, $param) && preg_match($exp2, $param) && preg_match($exp3, $param) && preg_match($exp4, $param);

        case "name":
            $exp = "/^[A-Z ]+$/i";
            return preg_match($exp, $param);

        case "company":
            $exp = "/^[A-Za-z. ]+$/i";
            return preg_match($exp, $param);

        default: //city
            return true;
    }
}
?>