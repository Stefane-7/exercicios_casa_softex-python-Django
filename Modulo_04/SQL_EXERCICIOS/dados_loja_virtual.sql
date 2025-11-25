CREATE TABLE Clientes(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE
);

CREATE TABLE Produtos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    preco FLOAT NOT NULL,
    estoque INTEGER NOT NULL
);

CREATE TABLE Pedidos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    data_compra TEXT,
    total REAL NOT NULL,
    id_cliente INTEGER,
    FOREIGN KEY (id_cliente) REFERENCES Clientes(id)
);

CREATE TABLE Itens_Pedido(
    id INTEGER PRIMARY KEY,
    id_pedido INTEGER,
    id_produto INTEGER,
    quantidade INTEGER NOT NULL,
    FOREIGN KEY (id_pedido) REFERENCES Pedidos(id),
    FOREIGN KEY (id_produto) REFERENCES Produtos(id)
)

INSERT INTO Clientes(nome, email) VALUES ('João', 'joão321@gmail.com');
INSERT INTO Clientes(nome, email) VALUES ('Maria', 'maria123@gmai.com');
INSERT INTO Clientes(nome, email) VALUES ('Lucia', 'lucia456@gmai.com');

INSERT INTO Produtos(nome, preco, estoque) VALUES ('teclado', 150.99, 15);
INSERT INTO Produtos(nome, preco, estoque) VALUES ('mouse', 65.50, 30);
INSERT INTO Produtos(nome, preco, estoque) VALUES ('monitor', 780.99, 5);

INSERT INTO Pedidos(data_compra, total, id_cliente) VALUES (datetime('now', 'localtime'), 281.99, 2);

INSERT INTO Itens_Pedido (id, id_pedido, id_produto, quantidade) VALUES (1, 1, 1, 1);

INSERT INTO Itens_Pedido (id, id_pedido, id_produto, quantidade) VALUES (2, 1, 2, 2);

SELECT nome, preco FROM Produtos WHERE preco > 100;

SELECT c.nome, p.id, p.data_compra
FROM Pedidos p
JOIN Clientes c ON p.id_cliente = c.id
WHERE c.nome = 'Maria';

UPDATE Produtos
SET preco = preco * 1.10
WHERE nome = 'mouse';

UPDATE Produtos
SET estoque = estoque - 2
WHERE id = 2;


DELETE FROM Clientes
WHERE nome = 'João';

DELETE FROM Itens_Pedido
WHERE id = 1;

SELECT * FROM Produtos;

SELECT * FROM Itens_Pedido;





