<?php

/*

Código para sair da sua sessão

*/


if(!isset($_SESSION)){
    session_start();
}

session_destroy();

header("Location: Login.php");

?>