<?php
/*

Aqui foi criado uma classe Form do Cadastre-se que age com a função alert, que verifica se algum erro foi criado pelo usuário,
se sim, ele aparecerá uma mensagem predefinida no index.php, 
Exemplo:
Se o email estiver vazio, ela irá imprimir:
O email está vazio.

Nesta classe Form, também fica a parte dos INSERT, na função cadastrar, que faz os INSERT'S dos atributos do cliente no banco de dados petshop, na tabela cliente.

*/

class ClienteController{

    public static function alert($tipo, $mensagem){
        if($tipo == 'erro'){
            echo '<div>'.$mensagem.'</div>';
            return false;
        } elseif($tipo == 'sucesso'){
            echo '<div>'.$mensagem.'</div>';
            return true;
        }
    }

    public static function cadastrar($nome, $email, $senha){
        include('../../../Models/conect.php');
        $sql = "INSERT INTO cliente (nome, email, senha) VALUES (?, ?, ?)";
        $stmt = $connect->prepare($sql);
        if(!$stmt){
            echo'Erro na preparação da consulta: ' . $connect->error;
        } else {
            $stmt->bind_param("sss", $nome, $email, $senha);
        }

        if($stmt->execute()){
            header("Location: ../login/Login.php");
        } else {
            echo 'Inserção de novo usuário errada. Erro: ' . $stmt->error;

        }
    }
   
}

?>