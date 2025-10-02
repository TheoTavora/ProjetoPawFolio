<?php

session_start(); // Inicia a sessão no começo do arquivo

include('../../../Models/conect.php'); // Conecta ao banco de dados

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $email = trim($_POST['email'] ?? '');
    $senha = $_POST['senha'] ?? '';

    if ($email === '' || $senha === '') {
        exit('preencha e-mail e senha.');
    }

    // consulta simples
    $sql = "SELECT nome, email, senha FROM cliente WHERE email = ? AND senha = ? LIMIT 1";
    $stmt = $connect->prepare($sql);
    if (!$stmt) {
        exit('erro na preparação: ' . $connect->error);
    }
    $stmt->bind_param('ss', $email, $senha);
    $stmt->execute();
    $res = $stmt->get_result();

    if ($row = $res->fetch_assoc()) {
        // login deu certo
        session_regenerate_id(true);
        $_SESSION['user_email'] = $row['email'];
        $_SESSION['user_nome'] = $row['nome'];
        header('Location: ../index.php');
        exit;
    } else {
        echo 'falha ao logar: e-mail ou senha incorretos.';
    }
}
?>

<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" type="text/css" href="../../static/CSS/subheader.css">
        <link rel="stylesheet" type="text/css" href="../../static/CSS/login.css">
        <link rel="icon" type="image/png" href="../../static/imgs/logopawfoliomenor.png"/>
        <title>Entrar em sua conta</title>
    </head>
    <header>
            <img src="../../static/imgs/logopawfoliomenor.png" alt="logo" />
    </header>
    <body>
    
        <div class="form_login">
            <form action = "" method="POST">
                <h1 style="color: white;">Seja bem-vindo!</h1>
                <span>Faça login para acessar a página inicial.</span>
                    <div class="whiteline"></div>
                        <div><input type="email" name="email" placeholder="seu e-mail"></div>
                        <div><input type="password" name="senha" placeholder="senha"></div>
                        <div><input type="submit" name="Confirmar" value="Confirmar"></div>
                        <div><input type="hidden" name="form" value="L_form"></div> 
                    <div class="whiteline"></div>
                <p class="cta">Não tem uma conta?</p>
                <a href="../register/teladecadastro.php">Cadastre-se</a>
            </form>


        </div>
    </body>

</html>

