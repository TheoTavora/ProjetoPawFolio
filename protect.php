<?php
/*

Verifica se você está logado ou não para acessar uma tela

*/


if(!isset($_SESSION)){
    session_start(); 
} 

if(!isset($_SESSION['user'])){
    die(boxpopup("Você não pode acessar a página porque não está logado"));
}

?>