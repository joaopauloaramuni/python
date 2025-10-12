-- Comandos CREATE TABLE (Estrutura do BD)

-- Comando para criar a tabela: clientes
CREATE TABLE IF NOT EXISTS clientes (
    cliente_id INT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    data_cadastro DATE DEFAULT CURRENT_DATE
);

-- Comando para criar a tabela: produtos
CREATE TABLE IF NOT EXISTS produtos (
    produto_id INT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    preco DECIMAL(10, 2) NOT NULL,
    estoque INT DEFAULT 0
);

-- Comando para criar a tabela: pedidos
CREATE TABLE IF NOT EXISTS pedidos (
    pedido_id INT PRIMARY KEY,
    cliente_id INT NOT NULL,
    data_pedido TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status VARCHAR(50) DEFAULT 'Pendente',
    FOREIGN KEY (cliente_id) REFERENCES clientes(cliente_id)
);


-- Comandos INSERT INTO (Dados de Exemplo)


-- Dados de exemplo para a tabela: clientes
INSERT INTO clientes (nome, email, data_cadastro) VALUES
('Erick Montenegro', 'ERROR_FAKE_email', '2025-08-01'),
('Mariah Carvalho', 'ERROR_FAKE_email', '2025-01-10'),
('Sophia Silveira', 'ERROR_FAKE_email', '2025-01-19'),
('Caroline Gonçalves', 'ERROR_FAKE_email', '2025-01-27'),
('Raul Moura', 'ERROR_FAKE_email', '2025-03-26'),
('Lavínia Albuquerque', 'ERROR_FAKE_email', '2025-02-20'),
('Dra. Nina Cardoso', 'ERROR_FAKE_email', '2025-07-20'),
('André Pires', 'ERROR_FAKE_email', '2025-01-25'),
('Daniela Casa Grande', 'ERROR_FAKE_email', '2025-08-06'),
('Luiz Gustavo Martins', 'ERROR_FAKE_email', '2025-02-27'),
('Melissa Vargas', 'ERROR_FAKE_email', '2025-08-14'),
('Nathan Castro', 'ERROR_FAKE_email', '2025-05-24'),
('Théo Sousa', 'ERROR_FAKE_email', '2025-01-01'),
('Lucca Cavalcanti', 'ERROR_FAKE_email', '2025-05-20'),
('Luiza Cunha', 'ERROR_FAKE_email', '2025-04-23'),
('Luan Sá', 'ERROR_FAKE_email', '2025-03-05'),
('Bernardo Porto', 'ERROR_FAKE_email', '2025-01-19'),
('Luiz Felipe Freitas', 'ERROR_FAKE_email', '2025-04-07'),
('Kaique da Mota', 'ERROR_FAKE_email', '2025-04-28'),
('Raquel Rios', 'ERROR_FAKE_email', '2025-03-24');


-- Dados de exemplo para a tabela: produtos
INSERT INTO produtos (nome, preco, estoque) VALUES
('quibusdam', 147.77, 79),
('facilis', 571.40, 26),
('sequi', 974.04, 8),
('aut', 179.34, 50),
('quidem', 237.45, 47),
('tenetur', 211.30, 47),
('iste', 804.35, 50),
('magnam', 868.29, 47),
('aperiam', 349.08, 12),
('delectus', 725.03, 26),
('rem', 651.52, 73),
('necessitatibus', 399.26, 90),
('consequatur', 473.94, 46),
('alias', 178.35, 51),
('harum', 370.86, 36),
('pariatur', 327.41, 70),
('dicta', 349.01, 14),
('assumenda', 190.72, 95),
('corporis', 377.33, 44),
('neque', 951.01, 54);


-- Dados de exemplo para a tabela: pedidos
INSERT INTO pedidos (data_pedido, status) VALUES
('2025-09-21 21:24:54.652256', 'Pendente'),
('2025-10-03 17:09:30.301672', 'Pendente'),
('2025-10-06 03:46:09.904085', 'Pendente'),
('2025-09-18 03:06:17.902463', 'Aprovado'),
('2025-10-04 20:47:11.215295', 'Cancelado'),
('2025-09-21 22:22:48.752059', 'Aprovado'),
('2025-09-15 08:54:35.407976', 'Pendente'),
('2025-10-05 15:07:54.707824', 'Pendente'),
('2025-09-20 12:53:33.495248', 'Cancelado'),
('2025-10-08 15:03:56.154823', 'Cancelado'),
('2025-09-26 00:47:43.800222', 'Aprovado'),
('2025-09-30 17:00:55.991757', 'Aprovado'),
('2025-09-23 03:54:31.688408', 'Pendente'),
('2025-10-08 09:25:59.721555', 'Aprovado'),
('2025-09-20 18:45:50.498497', 'Aprovado'),
('2025-10-05 17:28:24.729691', 'Cancelado'),
('2025-10-03 10:49:17.219356', 'Pendente'),
('2025-09-23 15:06:28.812627', 'Aprovado'),
('2025-09-30 18:35:17.947954', 'Aprovado'),
('2025-10-09 03:00:16.633064', 'Aprovado');