<?php
// pega a variável 'pergunta' do POST; se não existir, usa string vazia
$pergunta = $_POST['pergunta'] ?? '';

// verifica se a pergunta não foi enviada
if (!$pergunta) {
    // retorna um JSON de erro e encerra o script
    echo json_encode(["erro" => "Pergunta não recebida"]);
    exit;
}

// monta um JSON com a pergunta para enviar à API externa
$payload = json_encode(["pergunta" => $pergunta]);

// inicia uma sessão cURL apontando para o servidor Flask rodando em localhost:5000
$ch = curl_init('http://127.0.0.1:5000/responder');

// define que o resultado da requisição deve ser retornado como string
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

// define que será uma requisição POST
curl_setopt($ch, CURLOPT_POST, true);

// adiciona o corpo da requisição (payload em JSON)
curl_setopt($ch, CURLOPT_POSTFIELDS, $payload);

// define os headers HTTP (tipo de conteúdo e tamanho do corpo)
curl_setopt($ch, CURLOPT_HTTPHEADER, [
    'Content-Type: application/json',
    'Content-Length: ' . strlen($payload)
]);

// executa a requisição e guarda a resposta do servidor Flask
$resposta = curl_exec($ch);

// fecha/libera o recurso cURL
curl_close($ch);

// envia a resposta do Flask de volta ao cliente (normalmente já em JSON)
echo $resposta;
