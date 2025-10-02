<?php

include('../../../Models/conect.php');// Conexta o BD
include('../../../Controllers/ClienteController.php') // Inclue Cadastrar o Cliente

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <link rel="stylesheet" href="../../static/CSS/subheader.css">
    <link rel="stylesheet" href="../../static/CSS/cadastro.css">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="icon" type="image/png" href="../../static/imgs/logopawfoliomenor.png"/>

    <title>Cadastro do cliente PawFolio</title>
    
</head>
    <body>
    <?php 
    include '../partials/navbar.php'; 
    ?>
        <div class="form_cd">

    <?php
    if (isset($_POST['acao']) && $_POST['form'] === 'c_form') {
        // Sanitização básica dos inputs
        $nome   = trim($_POST['name'] ?? '');
        $email  = trim($_POST['email'] ?? '');
        $senha  = trim($_POST['senhaC'] ?? '');

        // Lista de campos obrigatórios
        $camposObrigatorios = [
            'nome'  => $nome,
            'email' => $email,
            'senha' => $senha,
        ];

        // Validação
        foreach ($camposObrigatorios as $campo => $valor) {
            if (empty($valor)) {
                ClienteController::alert('erro', "O campo {$campo} está vazio.");
                return;
            }
        }

        // Chamada ao controller
        ClienteController::cadastrar($nome, $email, $senha);
        ClienteController::alert('sucesso', "Cadastro de {$nome} efetuado com sucesso!");
    }
    ?>

            <form method="POST">
            <h1 style="color: white;">Cadastre-se</h1>
                    <div><input type="text" name="name" placeholder="Nome"></div>
                    <div><input type="text" name="email" placeholder="E-mail"></div>
                    <div><input type="text" name="senhaC" placeholder="Senha"></div>
                    <div><input type="submit" name="acao" value="Cadastrar" class="submit-button"></div>
                    <div><input type="hidden" name="form" value="c_form"></div>
                <div class="whiteline"></div>
                <p>Já tem uma conta?</p>    
                <a href="../login/Login.php">Fazer Login</a>   
            </form>
        </div>
<?php 
    include '../partials/footer.php'; 
?>
    </body>

</html>