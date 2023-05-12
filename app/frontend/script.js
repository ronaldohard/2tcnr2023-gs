// Obter o formulário de cadastro de alunos
const form = document.querySelector('#cadastro-aluno');

// Adicionar um evento de envio do formulário
form.addEventListener('submit', (event) => {
    // Impedir o envio do formulário por padrão
    event.preventDefault();

    // Obter os dados do formulário
    const nome = form.elements['nome'].value;
    const email = form.elements['email'].value;
    const telefone = form.elements['telefone'].value;
    const endereco = form.elements['endereco'].value;
    const curso = form.elements['curso'].value;
    const turma = form.elements['turma'].value;
    const ano = form.elements['ano'].value;

    // Criar um objeto com os dados do aluno
    const dados = {
        nome,
        email,
        telefone,
        endereco,
        curso,
        turma,
        ano
    };

    function exibirMensagemSucesso() {
        var mensagem = document.getElementById('mensagem');
        mensagem.innerHTML = 'Importação concluída com sucesso!';
        mensagem.style.color = 'green';
    }

    function limparCampos() {
        document.getElementById('nome').value = '';
        document.getElementById('email').value = '';
        document.getElementById('telefone').value = '';
        document.getElementById('endereco').value = '';
        document.getElementById('curso').value = '';
        document.getElementById('turma').value = '';
        document.getElementById('ano').value = '';
        // Limpar outros campos conforme necessário
    }

    // Fazer uma solicitação AJAX para o servidor Flask
    fetch('http://172.19.125.250/cadastro', {
            method: 'POST',
            body: JSON.stringify(dados),
            headers: {
                'Content-Type': 'application/json'
            },
            mode: 'cors' // permitir requisições CORS
        })
        .then(response => response.json()) // obter a resposta como JSON
        .then(data => {
            limparCampos();
            exibirMensagemSucesso();
            // Exibir a resposta no console
            console.log(data);
        })
        .catch(error => {
            // Manipular erros de solicitação AJAX
            console.error(error);
        });
});